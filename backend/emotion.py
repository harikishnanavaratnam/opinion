import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd

combined_df = pd.read_csv(r'C:\Users\HARI\Desktop\Saru\Opinion\backend\clustered_combined_data.csv')

# Plotting Emotion Counts
plt.figure(figsize=(10, 6))
sns.countplot(x='Detected_Emotion', data=combined_df, palette='viridis')
plt.title("Emotion Detection in AI Ethics Discussions")
plt.savefig("Emotion.png")
plt.close()
