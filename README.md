# EWMA Wastewater Monitoring Tool

This Python script provides a visual and statistical tool for monitoring wastewater viral load using Exponentially Weighted Moving Averages (EWMA). It helps identify potential outbreaks by detecting unusual trends and excursions beyond control limits.

## Key Features

* **Data Aggregation:** Automatically aggregates wastewater data by date to calculate the average viral load.
* **EWMA Calculation:** Implements the EWMA algorithm to smooth out fluctuations and highlight underlying trends.
* **Control Limits:** Determines upper and lower control limits (UCL, LCL) based on the EWMA trend and data variability.
* **Interactive Visualization:** Generates an interactive Plotly chart displaying:
    * Average wastewater viral load (raw data)
    * EWMA trend line
    * Upper and lower control limits (horizontal lines)
* **Customization:** Allows adjusting the EWMA smoothing parameter (`alpha`) and standard deviation multiplier for control limits.

## Dependencies

* pandas
* numpy
* plotly

## How to Use

1. **Data Preparation:** Ensure your wastewater data is in a CSV file named `data.csv` with the following columns:
   * `Date` (datetime format: YYYY-MM-DD)
   * `Wastewater_Viral_Load` (numeric)

2. **Installation:** Install the required libraries:

   ```bash
   pip install pandas numpy plotly
3. **Run the Script:** Execute the Python script from your terminal:

   ```bash
   python ewma_wastewater_monitoring.py  

4. **Interactive Chart:** The script will open an interactive Plotly chart in your web browser. Explore the data by hovering over points to see specific values and trends.

## Interpretation

* EWMA Line: The EWMA line represents the smoothed trend of wastewater viral load. Observe its direction (increasing, decreasing, stable) to assess the overall situation.

* Control Limits: Pay attention to points where the raw data or EWMA line crosses the control limits. Excursions beyond these limits may signal a significant change or potential outbreak.

* Outbreak Identification: Consistent upward trends in the EWMA line, especially with data points exceeding the upper control limit (UCL), may suggest an increased risk of an outbreak. Conversely, a sustained downward trend below the lower control limit (LCL) could indicate a decrease in viral prevalence.

* Points Outside Control Limits: While occasional points outside the control limits are expected due to random variation, a pattern of points outside these limits, especially if they occur consecutively, warrants further investigation. This could be a sign of a true change in viral load, a data quality issue, or an unusual event affecting the wastewater system.

## Customization

* Smoothing Parameter (alpha): Adjust the alpha value (default 0.3) to control how much weight is given to recent data. Higher values (e.g., 0.5) emphasize recent trends, while lower values (e.g., 0.1) produce smoother, less reactive EWMA lines.

* Control Limit Width: Modify the std_dev_multiplier (default 2) to adjust the width of the control limits. A higher multiplier (e.g., 3) creates wider limits, reducing the sensitivity to short-term fluctuations.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve this script.

## PLot output
![image](https://github.com/vinayrajput0005/EWMA-Wastewater-Monitoring/assets/54147406/81923fed-c966-4c40-9566-ca47ea4cdb20)


