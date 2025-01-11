import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd
combined_df = pd.read_csv(r'C:\Users\HARI\Desktop\Saru\Opinion\backend\clustered_combined_data.csv')


combined_df['Time'] = pd.to_datetime(combined_df['Time'], errors='coerce') 
combined_df = combined_df.dropna(subset=['Time']) 

combined_df['Time'] = pd.to_datetime(combined_df['Time'], utc=True)
combined_df = combined_df.sort_values(by='Time')
theme_trends = combined_df.groupby([pd.Grouper(key='Time', freq='M'), 'Assigned_Theme']).size().unstack(fill_value=0)
theme_trends = theme_trends.drop(columns=['Ethics','Bias','Fairness'], errors='ignore')

theme_trends_smoothed = theme_trends.rolling(window=24, min_periods=1).mean()


plt.figure(figsize=(12, 6))
for theme in theme_trends_smoothed.columns:
    plt.plot(theme_trends_smoothed.index, theme_trends_smoothed[theme], label=theme)

plt.xlabel('Time')
plt.ylabel('Smoothed Number of Mentions')
plt.title('Smoothed Trend of Themes Over Time (Excluding Ethics)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("trend.png")
plt.close()