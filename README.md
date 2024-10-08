# 🏨 **Hotel Revenue Insights - Hospitality Domain**

## Table of Contents
- [Project Overview](#project-overview)
- [Project Goals](#project-goals)
- [Data Source](#data-source)
- [Tools](#tools)
- [Results & Key Insights](#results--key-insights)
- [Recommendations](#recommendations)
- [Conclusion & Next Steps](#conclusion--next-steps)
- [Visualizations](#visualizations)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Screenshots](#screenshots)

## **Project Overview**

AtliQ Grands, a fictitious chain of five-star luxury/business hotels across India, has been facing challenges in maintaining market share and revenue due to competitors' strategic moves and ineffective internal management. To address these issues, the company's revenue management team has initiated a data-driven approach to support business intelligence and regain competitive advantage. This project involves working with a third-party analytics provider to generate insights from historical data and guide AtliQ Grands in making informed strategic decisions.

This repository serves as a roadmap and documentation for the insights required to help AtliQ Grands optimize their operations, improve revenue, and regain market share. 

---

## **Project Goals**
The main goals of this project are to:
- **Maximize Revenue** by optimizing pricing strategies using real-time demand data.
- **Reduce Cancellations** to improve occupancy rates and predict future booking behaviour.
- **Increase Direct Bookings** to lower costs and build customer loyalty.
- **Improve Operational Efficiency** by identifying underperforming properties and recommending targeted actions.
- **Stay Competitive** by using insights to benchmark against market rivals in the luxury/business hotel segment.

---

## **Business Questions**
- What are the peak booking periods across different cities?
- How can pricing be tailored for specific cities, such as higher rates for Mumbai and competitive pricing for Delhi and Hyderabad?
- Which cities or properties have the highest cancellation rates, and what are the reasons behind them?
- How can we reduce cancellations on platforms with the highest rates?
- How can we increase direct bookings and reduce reliance on third-party platforms?
- What percentage of our bookings come from third-party vs. direct platforms, and what is the acquisition cost per channel?
- How can we improve occupancy rates in underperforming cities like Delhi and Hyderabad?
- What is the current breakdown of weekday vs. weekend bookings, and how can we attract more weekend leisure travellers?
- Which properties have the lowest revenue, bookings, and guest satisfaction scores?
- Which properties have the highest return on investment (ROI) and growth potential, and where should we consider expanding or upgrading?
- How can we improve our guest offerings to appeal to business travellers and regain market share?
- What geographic markets or cities offer the best opportunities for growth and new property investments?

---

## **Data Source**
The data for this analysis `full_bookings.csv` is sourced from Atliq Grand's database, which includes booking_date, city, property_id, revenue etc. from April to July.

---

## **Tools**
- `Python` - Data Analysis
- `Dash` - Visualization


## **Results & Key Insights**

### **1. Key Metrics**:
- **Revenue**: $1 Billion
- **Occupancy Rate**: 57.87%
- **Average Rating**: 4.42
- **Total Bookings**: 134,000
- **Cancellation Rate**: 24.83%
- **Number of Hotels**: 7

---

### **2. City-Level Analysis: Performance & Recommendations**

#### **Mumbai**:
- **Revenue**: $668M (66.8% of total revenue)
- **Bookings**: 43K (32% of total bookings)
- **Average Rating**: 4.43

  - **Key Insights**:
    - Mumbai is the top performer in both revenue and bookings.
    - The city commands a significant share of total revenue despite its bookings being relatively proportional to other cities. This likely points to **higher room rates** or more premium offerings in Mumbai hotels.

---

#### **Bangalore**:
- **Revenue**: $420M (42% of total revenue)
- **Bookings**: 32K (23.8% of total bookings)
- **Average Rating**: 4.33

  - **Key Insights**:
    - Bangalore performs well in revenue but is lagging slightly in terms of bookings, indicating potential for further growth.
  
---

#### **Hyderabad**:
- **Revenue**: $325M (32.5% of total revenue)
- **Bookings**: 34K (25.4% of total bookings)
- **Average Rating**: 4.44

  - **Key Insights**:
    - Hyderabad has a relatively high number of bookings but generates lower revenue, suggesting more economical or mid-range pricing.

---

#### **Delhi**:
- **Revenue**: $294M (29.4% of total revenue)
- **Bookings**: 24K (17.9% of total bookings)
- **Average Rating**: 4.48 (highest)

  - **Key Insights**:
    - Delhi has the highest customer satisfaction score but the lowest bookings and revenue. There may be a mismatch between supply and demand, or untapped potential in this city.

---

### **3. Platform-Level Analysis: Bookings & Optimization**

#### **Top Booking Platforms**:
- **Others**: 40.91%
- **makeyoutrip**: 19.99%
- **logtrip**: 10.96%
- **direct online**: 9.94%
- **tripster**: 7.16%
- **journey**: 6.02%
- **direct offline**: 5.02%

  - **Key Insights**:
    - The "others" platform contributes 40.91% of total bookings, but its specifics are unclear. This represents an important revenue stream that should be examined closely.
    - **makeyoutrip** and **logtrip** are the leading platforms contributing almost 31% of all bookings.
    
---

### **4. Day Type Analysis: Weekday vs Weekend Performance**

#### **Bookings per Day Type**:
- **Weekday bookings**: 70.58%
- **Weekend bookings**: 29.42%

  - **Key Insights**:
    - Bookings skew heavily towards weekdays, which likely reflects a higher proportion of business-related travel.

---

### **5. Property Performance: High-Performing Hotels**

#### Top Properties by Revenue:
- **Atliq Exotica (Mumbai)**: Consistently generates high revenue, with May revenue at **$39.57M** and June at **$39.31M**.
- **Atliq Palace (Mumbai)**: Strong performer, with May revenue of **$34.84M** and June at **$34.85M**.

#### Ratings Across Properties:
- The average ratings for the top hotels range between **4.68 and 4.74**, indicating very high customer satisfaction across properties.

  - **Key Insights**:
    - **Atliq Exotica** and **Atliq Palace** in Mumbai are consistently driving revenue and achieving high ratings. These properties are vital to the business's overall success.

---

### **6. Cancellations and Occupancy Analysis**

#### **Cancellation Rate**: 24.83%
- Nearly **1 in 4 bookings are cancelled**, representing lost revenue and possible inefficiencies in the booking process.

  - **Key Insights**:
    - The cancellation rate is high, and reducing this would have a notable impact on confirmed bookings and revenue.

---

## **Recommendations**

### **1. Revenue Optimization and Dynamic Pricing**
- Implement dynamic pricing models to optimize room rates in real-time, based on demand fluctuations and competitor rates.
- Leverage Hyderabad's high customer satisfaction to create loyalty programs for returning customers.
- Consider increasing the room supply in high-demand areas.
- Increase per-booking revenue by offering premium services such as room upgrades, spas, or other amenities.
- Continue investing in customer experience to ensure these high ratings are maintained. Happy customers often lead to repeat bookings and positive reviews.

### **2. Reducing Cancellations**
- Focus on platforms with high cancellation rates and implement customer retention strategies (e.g., flexible policies, and targeted offers).
- Introduce more flexible cancellation policies with partial refunds or rebooking incentives to reduce cancellations.
- Utilize predictive analytics to identify customers most likely to cancel, allowing proactive engagement to reduce cancellations.

### **3. Increasing Direct Bookings**
- Since direct online and offline bookings represent a small portion (15%), invest in marketing campaigns that promote direct bookings and offer exclusive benefits for customers booking through AtliQ Grands’ website.
- Improve the digital experience on the website and mobile platform to increase conversion rates.

### **4. Boosting Weekend Occupancy**
- Target leisure travellers with customized weekend packages and promotions that enhance the guest experience.
- Introduce weekend-specific promotions to increase weekend stays, such as discounted rates, themed weekend getaways, or family packages.
- Strengthen partnerships with local businesses and corporations to secure more weekday bookings through business conferences or corporate travel deals.
  
### **5. Property-Specific Insights**
- Identify underperforming properties and address operational inefficiencies that affect guest satisfaction and revenue.
- Invest in high-performing properties with potential for expansion and growth, replicating successful models like AtliQ Exotica.
- Add more properties or increase hotel capacity in Delhi to meet potential demand.

---

## **Conclusion & Next Steps**:

The Atliq Grands hotels are performing strongly across Mumbai and Bangalore, with opportunities for growth in Delhi and Hyderabad. Focusing on reducing cancellations, boosting weekend stays, and improving direct booking channels can significantly increase overall revenue. The positive customer ratings across properties provide a solid foundation for expansion and continued customer loyalty.

---

## Visualizations
Explore the live interactive dashboard here:
  - [View Dashboard](https://revenue-insights-dashboard-j4uh.onrender.com/)

---

## Installation

If you'd like to analyze the data further or run your visualizations, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/revenue_insights-hospitality_domain.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd revenue_insights-hospitality_domain
   ```

3. **Install dependencies** (if needed):
   The project uses standard data analysis libraries such as `Pandas`, `Plotly`, and `Dash`. Install them via pip:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

To run the analysis or explore the visualizations:
1. Ensure you have the required dependencies installed.
2. Execute the analysis script to generate visualizations.
3. To contribute new analyses or improve on current insights, simply fork the repository, make your changes, and submit a pull request.

---

## **Contributing**

Contributions to this project are welcome! Please open an issue to discuss any major changes or suggestions.

---

## Screenshots

### Dashboard Overview
![AtliQ Grands Dashboard](https://github.com/ajlkau68/Revenue_Insights-Hospitality_Domain/blob/main/src/assets/Atliq-Grands-Dashboard.png)




