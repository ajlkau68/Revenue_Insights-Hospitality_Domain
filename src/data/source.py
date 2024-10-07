from __future__ import annotations
from dataclasses import dataclass
import math
import pandas as pd
import numpy as np
from .loader import DataSchema
from typing import Optional

# Helper function
def human_format(num):
    if num == 0:
        return "0"

    magnitude = int(math.log(num, 1000))
    mantissa = str(int(num / (1000 ** magnitude)))
    return mantissa + ["", "K", "M", "B", "T", "P"][magnitude]

# Create a dataclass that handles all the logic of the app which is all the pandas operations
@dataclass
class DataSource:
    _data: pd.DataFrame   

    # Filter by month and city
    def filter(self,
                months: Optional[list[str]],
                cities: Optional[list[str]]) -> DataSource:

            if months is None:
                months = self.unique_months

            if cities is None:
                cities = self.unique_cities

            filtered_data = self._data.query('booking_month in @months and city in @cities')

            return DataSource(filtered_data)

    # Filter by month
    def month_filter(self,
               months: Optional[list[str]]) -> DataSource:

        if months is None:
            months = self.unique_months

        filtered_month = self._data.query('booking_month in @months')

        return DataSource(filtered_month)
    
    
    # Create functions to handle pandas operations needed in callback functions
    # Get Metrics for text cards
    def get_text_data(self):
        # Total Revenue
        revenue = self._data['revenue_realized'].sum()

        # Total Bookings
        bookings = self._data['booking_id'].count()
        
        # Occupancy %
        capacity = 232576
        occupancy_pcnt = round((bookings/capacity) * 100, 2)

        # Average Ratings
        avg_rating = str(round(np.mean(self._data['ratings_given']),2))
        
        # Cancellation %
        cancelled_bookings = self._data.query("booking_status == 'Cancelled'").shape[0]
        cancellation_pcnt = str(round((cancelled_bookings/bookings) * 100, 2))

        # Number of Hotels
        num_hotels = self._data['hotel_name'].nunique()

        return human_format(revenue), occupancy_pcnt, avg_rating, human_format(bookings), cancellation_pcnt, num_hotels

    # Get revenue per city
    def get_city_revenue(self) -> pd.DataFrame:
        city_data = self._data.pivot_table(
            values=[DataSchema.REVENUE_REALIZED],
            index=[DataSchema.CITY], 
            aggfunc='sum').reset_index()
        # city_data[DataSchema.REVENUE_REALIZED] = city_data[
        #     DataSchema.REVENUE_REALIZED].apply(lambda x: human_format(x))
        return city_data
    
    # Get bookings per city
    def get_city_bookings(self) -> pd.DataFrame:
        bookings_data = self._data.pivot_table(
            values=[DataSchema.BOOKING_ID],
            index=[DataSchema.CITY], 
            aggfunc='count').reset_index()
        # bookings_data[DataSchema.BOOKING_ID] = bookings_data[
        #     DataSchema.BOOKING_ID].apply(lambda x: human_format(x))
        return bookings_data
    
    # Get average ratings per city
    def get_city_ratings(self) -> pd.DataFrame:
        ratings_data = self._data.pivot_table(
            values=[DataSchema.RATINGS_GIVEN],
            index=[DataSchema.CITY], 
            aggfunc='mean').reset_index()
        ratings_data[DataSchema.RATINGS_GIVEN] = round(ratings_data[DataSchema.RATINGS_GIVEN], 2)
        return ratings_data
    
    # Get bookings per day type
    def get_booking_day_type(self) -> pd.DataFrame:
        day_type_data = round(self._data[DataSchema.DAY_TYPE].
                              value_counts(normalize=True) * 100, 2).to_frame().reset_index().sort_values(
                                  by=DataSchema.PROPORTION, ascending=True
                              )
        return day_type_data
    
    # Get bookings per platform
    def get_booking_platform(self) -> pd.DataFrame:
        platform_data = round(self._data[DataSchema.BOOKING_PLATFORM].
                              value_counts(normalize=True) * 100, 2).to_frame().reset_index().sort_values(
                                  by=DataSchema.PROPORTION, ascending=True
                              )
        return platform_data

    def get_table_data(self) -> pd.DataFrame:
        table_data = self._data.pivot_table(
            values=[DataSchema.REVENUE_REALIZED, DataSchema.BOOKING_ID, DataSchema.RATINGS_GIVEN],
            index=[DataSchema.PROPERTY_ID, DataSchema.CITY, DataSchema.BOOKING_MONTH, DataSchema.HOTEL_NAME],
            aggfunc={DataSchema.REVENUE_REALIZED:'sum', DataSchema.BOOKING_ID:'count', 
                     DataSchema.RATINGS_GIVEN:'mean'}, sort=False)
        table_data[DataSchema.RATINGS_GIVEN] = round(table_data[DataSchema.RATINGS_GIVEN], 2)
        table_data = table_data.iloc[:, 0:].reset_index()
        table_data = table_data.rename(
            {DataSchema.BOOKING_MONTH:'month',
              DataSchema.HOTEL_NAME:'hotel',
              DataSchema.REVENUE_REALIZED:'revenue',
              DataSchema.BOOKING_ID:'bookings',
              DataSchema.RATINGS_GIVEN:'avg_rating'},
              axis=1).sort_values(by='revenue', ascending=False)
        
        return table_data
    

    @property
    def row_count(self) -> int:
        return self._data.shape[0]


    @property
    def all_months(self) -> list[str]:
        return self._data[DataSchema.BOOKING_MONTH].tolist()

    @property
    def all_cities(self) -> list[str]:
        return self._data[DataSchema.CITY].tolist()

    @property
    def all_status(self) -> list[str]:
        return self._data[DataSchema.BOOKING_STATUS].tolist()
    
    @property
    def all_platforms(self) -> list[str]:
        return self._data[DataSchema.BOOKING_PLATFORM].tolist()


    @property
    def unique_months(self) -> list[str]:
        return sorted(set(self.all_months))

    @property
    def unique_cities(self) -> list[str]:
        return sorted(set(self.all_cities))
    
    @property
    def unique_status(self) -> list[str]:
        return sorted(set(self.all_status))
    
    @property
    def unique_platforms(self) -> list[str]:
        return sorted(set(self.all_platforms))
    
    
    
