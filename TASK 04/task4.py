import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset and specify column names
columns = ['ID', 'Topic', 'Sentiment', 'Text']
data = pd.read_csv(r"C:\Users\Bhanuja\Desktop\BHANUJA\PROJECTS\TASK 04\twitter_training.csv", names=columns)

# Remove rows with missing data and duplicates
data = data.dropna().drop_duplicates()

# Plotting topic frequency
plt.figure(figsize=(10,12))
sns.countplot(y='Topic', data=data, palette='coolwarm', order=data['Topic'].value_counts().index)
plt.title("Frequency of Topics")
plt.xlabel("Number of Tweets")
plt.ylabel("Topic")
plt.show()

# Visualizing the distribution of sentiments
plt.figure(figsize=(8,6))
sns.countplot(x='Sentiment', data=data, palette='Set2')
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Frequency")
plt.show()

# Pie chart to show the distribution of sentiments
sentiment_counts = data['Sentiment'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette('Set2', len(sentiment_counts)))
plt.title('Proportion of Sentiments')
plt.show()

# Sentiment distribution across different topics
plt.figure(figsize=(20,10))
sns.countplot(x='Topic', data=data, hue='Sentiment', palette='Set2', order=data['Topic'].value_counts().index)
plt.xticks(rotation=90)
plt.title("Sentiment Distribution by Topic")
plt.xlabel("Topic")
plt.ylabel("Count")
plt.show()

# Aggregating sentiment counts per topic
sentiment_summary = data.groupby(["Topic", "Sentiment"]).size().reset_index(name='Count')

# Filtering for the top 5 topics
top_5_topics = data['Topic'].value_counts().nlargest(5).index
top_sentiments = sentiment_summary[sentiment_summary['Topic'].isin(top_5_topics)]

# Visualizing the top 5 topics with negative sentiment
plt.figure(figsize=(12, 8))
sns.barplot(data=top_sentiments[top_sentiments['Sentiment'] == 'Negative'], x='Topic', y='Count', palette='Blues')
plt.title('Top 5 Topics with Negative Sentiment')
plt.xlabel('Topic')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Visualizing the top 5 topics with positive sentiment
plt.figure(figsize=(12, 8))
sns.barplot(data=top_sentiments[top_sentiments['Sentiment'] == 'Positive'], x='Topic', y='Count', palette='Greens')
plt.title('Top 5 Topics with Positive Sentiment')
plt.xlabel('Topic')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Visualizing the top 5 topics with neutral sentiment
plt.figure(figsize=(12, 8))
sns.barplot(data=top_sentiments[top_sentiments['Sentiment'] == 'Neutral'], x='Topic', y='Count', palette='Oranges')
plt.title('Top 5 Topics with Neutral Sentiment')
plt.xlabel('Topic')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Visualizing the top 5 topics with irrelevant sentiment
plt.figure(figsize=(12, 8))
sns.barplot(data=top_sentiments[top_sentiments['Sentiment'] == 'Irrelevant'], x='Topic', y='Count', palette='Purples')
plt.title('Top 5 Topics with Irrelevant Sentiment')
plt.xlabel('Topic')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Sentiment analysis for 'Google'
google_data = data[data['Topic'] == 'Google']
google_sentiments = google_data['Sentiment'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(google_sentiments, labels=google_sentiments.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Sentiment Distribution for "Google"')
plt.show()

# Sentiment analysis for 'Microsoft'
microsoft_data = data[data['Topic'] == 'Microsoft']
microsoft_sentiments = microsoft_data['Sentiment'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(microsoft_sentiments, labels=microsoft_sentiments.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Sentiment Distribution for "Microsoft"')
plt.show()

# Adding a column for tweet length
data['Text_Length'] = data['Text'].apply(len)

# Distribution of tweet lengths
plt.figure(figsize=(10,6))
sns.histplot(data['Text_Length'], bins=30, kde=True, color='purple')
plt.title('Tweet Length Distribution')
plt.xlabel('Length of Tweet')
plt.ylabel('Frequency')
plt.show()

# Boxplot showing tweet length by sentiment
plt.figure(figsize=(10,6))
sns.boxplot(x='Sentiment', y='Text_Length', data=data, palette='Set2')
plt.title('Tweet Length by Sentiment')
plt.xlabel('Sentiment')
plt.ylabel('Length of Tweet')
plt.ylim(0, 300)
plt.show()

# Heatmap for topic vs sentiment distribution
topic_sentiment_heatmap = pd.crosstab(index=data['Topic'], columns=data['Sentiment'])
plt.figure(figsize=(14,10))  
sns.heatmap(topic_sentiment_heatmap, cmap='coolwarm', annot=True, fmt='d', linewidths=.5)
plt.title('Heatmap of Topics and Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Topic')
plt.show()

# WordCloud for Topics
topics_str = ' '.join(topic_sentiment_heatmap.index)
wordcloud_topics = WordCloud(width=1000, height=500).generate(topics_str)
plt.imshow(wordcloud_topics, interpolation='bilinear')
plt.title('WordCloud of Topics')
plt.axis('off')
plt.show()

# WordCloud for Text Corpus
text_corpus = ' '.join(data['Text'])
wordcloud_text = WordCloud(width=1200, height=500, background_color='white').generate(text_corpus)
plt.imshow(wordcloud_text, interpolation='bilinear')
plt.title('WordCloud of Tweet Texts')
plt.axis('off')
plt.show()
