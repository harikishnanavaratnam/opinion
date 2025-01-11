import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd

combined_df = pd.read_csv(r'C:\Users\HARI\Desktop\Saru\Opinion\backend\clustered_combined_data.csv')

plt.figure(figsize=(10, 6))
sns.histplot(combined_df['VADER_sentiment'], kde=True, color='blue', label='VADER Sentiment')
sns.histplot(combined_df['Huggingface_sentiment'].map(lambda x: 1 if x == 'POSITIVE' else -1), kde=True, color='orange', label='Huggingface Sentiment')
plt.title("Sentiment Distribution (VADER vs Huggingface)")
plt.legend()
plt.savefig('sentiment.png')
plt.close()

