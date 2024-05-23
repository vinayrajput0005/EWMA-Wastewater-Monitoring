import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


# Load Data from CSV
df = pd.read_csv('data.csv', parse_dates=['Date'])

# Aggregate data by Date and calculate mean Wastewater_Viral_Load
df_agg = df.groupby('Date')['Wastewater_Viral_Load'].mean().reset_index()

# EWMA Calculation Function 
def calculate_ewma(series, alpha=0.3):
    ewma = [series[0]] 
    for i in range(1, len(series)):
        ewma.append(alpha * series[i] + (1 - alpha) * ewma[i - 1])
    return ewma

# Calculate EWMA Trends for Aggregated Data
df_agg['EWMA_Wastewater'] = calculate_ewma(df_agg['Wastewater_Viral_Load'])

# Calculate Control Limits
def calculate_control_limits(series, ewma, alpha=0.3, std_dev_multiplier=2):
    std_dev = series.std()
    upper_limit = ewma + std_dev_multiplier * std_dev * np.sqrt(alpha / (2 - alpha))
    lower_limit = ewma - std_dev_multiplier * std_dev * np.sqrt(alpha / (2 - alpha))
    return upper_limit, lower_limit

# Calculate Control Limits for Wastewater using Aggregated Data
df_agg['Wastewater_UCL'], df_agg['Wastewater_LCL'] = calculate_control_limits(df_agg['Wastewater_Viral_Load'], df_agg['EWMA_Wastewater'])

# Create Interactive Plot with Plotly
fig = go.Figure()

# Add Traces (Lines and Control Limits) for Wastewater Only - Using Aggregated Data
fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['Wastewater_Viral_Load'], mode='markers+lines', name='Avg Wastewater Viral Load', line=dict(width=1)))
fig.add_trace(go.Scatter(x=df_agg['Date'], y=df_agg['EWMA_Wastewater'], mode='lines', name='EWMA Wastewater', line=dict(width=2)))

# Add Straight Horizontal Lines for Control Limits (Wastewater Only)
fig.add_shape(type="line", x0=df_agg['Date'].min(), y0=df_agg['Wastewater_UCL'].mean(), x1=df_agg['Date'].max(), y1=df_agg['Wastewater_UCL'].mean(),
              line=dict(color="Red", width=1, dash="dash"), name='Wastewater UCL')
fig.add_shape(type="line", x0=df_agg['Date'].min(), y0=df_agg['Wastewater_LCL'].mean(), x1=df_agg['Date'].max(), y1=df_agg['Wastewater_LCL'].mean(),
              line=dict(color="Red", width=1, dash="dash"), name='Wastewater LCL')

# Customize Layout (increased plot size)
fig.update_layout(
    title='', 
    xaxis_title='Date',
    yaxis_title='Wastewater Viral Load',
    hovermode='x unified',
    width=1000,
    height=800,
    
    # Add axis lines
    xaxis=dict(showline=True, linewidth=1, linecolor='black'),
    yaxis=dict(showline=True, linewidth=1, linecolor='black'),
    
    # Remove background colors
    plot_bgcolor='white',   
    paper_bgcolor='white'   
)

fig.show()

pio.write_image(fig, 'wastewater_viral_load_highres.png', scale=5)  # Adjust scale as needed
# You can also use .jpeg, .svg, .pdf, etc. for different formats

