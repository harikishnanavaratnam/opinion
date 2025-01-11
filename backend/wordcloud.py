from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

combined_df =  pd.read_csv('C:\Users\HARI\Desktop\Saru\Opinion\backend\clustered_combined_data.csv')

# Function to Generate and Display Word Cloud for a Specific Theme
def generate_word_cloud(theme, data):
    # Filter data for the specific theme
    theme_data = data[data['Assigned_Theme'] == theme]['Cleaned_Text']
    theme_text = ' '.join(theme_data)
    
    # Generate Word Cloud
    wordcloud = WordCloud(
        width=800, 
        height=400, 
        background_color='white', 
        colormap='viridis', 
        max_words=200
    ).generate(theme_text)
    
    # Display the Word Cloud
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for Theme: {theme}", fontsize=16)
    plt.savefig("{theme}.png")
    plt.close()

# List of Themes
themes = combined_df['Assigned_Theme'].unique()

# Generate Word Clouds for All Themes
for theme in themes:
    if theme != "Other":  # Skip the 'Other' category if needed
        generate_word_cloud(theme, combined_df)