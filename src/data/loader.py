import pandas as pd

class DataSchema:
    BOOKING_ID = 'booking_id'
    PROPERTY_ID = 'property_id'
    BOOKING_DATE = 'booking_date'
    CHECK_IN_DATE = 'check_in_date'
    CHECK_OUT_DATE = 'checkout_date'
    NO_GUESTS = 'no_guests'
    ROOM_CATEGORY = 'room_category'
    BOOKING_PLATFORM = 'booking_platform'
    RATINGS_GIVEN = 'ratings_given'
    BOOKING_STATUS = 'booking_status'
    REVENUE_GENERATED = 'revenue_generated'
    REVENUE_REALIZED = 'revenue_realized'
    ROOM_CLASS = 'room_class'
    BOOKING_MONTH = 'booking_month'
    CITY = 'city'
    HOTEL_NAME = 'hotel_name'
    HOTEL_CATEGORY = 'hotel_category'
    WEEKDAY = 'weekday'
    DAY_TYPE = 'day_type'
    WEEK_NO = 'week_no'
    DAY_OF_WEEK = 'day_of_week'
    PROPORTION = 'proportion'

# Create a function that loads the main dataset
def load_data(path: str) -> pd.DataFrame:
    # load the data from the csv file
    data = pd.read_csv(
        path,
        parse_dates=[DataSchema.BOOKING_DATE, 
                     DataSchema.CHECK_IN_DATE, 
                     DataSchema.CHECK_OUT_DATE]

    )
   
    return data
