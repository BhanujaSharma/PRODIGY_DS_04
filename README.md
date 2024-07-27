
**Task-04**
Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes towards specific topics or brands.

Sample Dataset :- https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis

This project involves analyzing sentiment in tweets related to various topics using a dataset that contains information on the topic, sentiment, and content of each tweet. Here's a detailed breakdown of the project's objectives, methods, and key visualizations:

### Objectives
1. **Data Cleaning**:
   - Remove rows with missing data and duplicates to ensure data quality.
   
2. **Exploratory Data Analysis (EDA)**:
   - Understand the distribution of topics and sentiments within the dataset.
   - Identify patterns and insights regarding the relationship between different topics and sentiments.

3. **Visualization**:
   - Create various plots to visually represent the distribution and relationships in the data.

### Methods

1. **Data Loading and Cleaning**:
   - The dataset is loaded using Pandas and columns are named as 'ID', 'Topic', 'Sentiment', and 'Text'.
   - Rows with missing values and duplicate entries are dropped to ensure a clean dataset.

2. **Exploratory Data Analysis (EDA)**:
   - **Topic Frequency**: A bar plot shows the count of tweets for each topic, providing an overview of the most discussed topics.
   - **Sentiment Distribution**: Both bar plots and pie charts are used to visualize the proportion of different sentiments (e.g., Positive, Negative, Neutral, Irrelevant) in the dataset.
   - **Sentiment Distribution by Topic**: A grouped bar plot highlights how different sentiments are distributed across various topics, allowing for comparison.
   - **Tweet Length Analysis**: Histograms and boxplots analyze the distribution of tweet lengths and how they vary across different sentiments.

3. **Detailed Analysis on Specific Topics**:
   - The dataset is filtered to examine sentiment distribution for specific topics like "Google" and "Microsoft," providing insights into how these companies are perceived in the tweets.

4. **WordClouds**:
   - Two WordCloud visualizations are generated:
     - One for the topics to visualize the most frequently mentioned topics.
     - Another for the entire text corpus to highlight the most common words used in the tweets.

5. **Additional Analysis**:
   - A heatmap visualizes the cross-tabulation of topics and sentiments, illustrating the intensity and distribution of sentiments across different topics.

### Key Visualizations
1. **Bar Plot for Topic Frequency**: Shows which topics are most frequently discussed in the dataset.
2. **Sentiment Distribution**: Visualized using both a bar plot and a pie chart, showing the overall distribution of sentiments.
3. **Sentiment Distribution by Topic**: A detailed view of how sentiments vary across different topics, which can be useful for identifying trends and anomalies.
4. **Tweet Length Distribution**: Provides insights into the nature of tweets by sentiment, such as whether certain sentiments are associated with longer or shorter tweets.
5. **WordClouds**: Visual representation of the most common topics and words, providing a quick way to grasp the dominant themes and keywords.

### Conclusion
This project provides a comprehensive overview of the sentiment landscape across various topics based on Twitter data. It uses various data visualization techniques to uncover patterns and insights that might be useful for understanding public opinion, brand perception, and more. The results can help businesses, researchers, and analysts to gauge the public's mood on different topics and adjust strategies accordingly.
