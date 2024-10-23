# Sentiment Analysis on Tweets about the "When We Were Young Festival"

[THIS IS A PROJECT IN PROGRESS]

## Overview
This project involves the extraction and sentiment analysis of tweets regarding the music festival "When We Were Young," which took place in Las Vegas on October 19 and 20, 2024. The festival aims on reuniting classic pop punk and emo bands from the 2000s in one place, featuring major names in the genre and attracting around 60,000 people.


 First, the festival's inaugural edition in 2023 received notable criticism from attendees regarding various aspects of the event. By analyzing the sentiment of tweets from the 2024 edition, this project aims to assess whether public perception has shifted in response to the feedback from the previous year. Understanding these changes can provide valuable insights into the festival's reception and areas for improvement.

 Second, this analysis is situated within the larger context of music festivals, particularly in light of the return of the Warped Tour. While both festivals appeal to similar demographics, they differ in their thematic focus. This comparative approach can help identify trends in audience sentiment and engagement within the festival landscape, contributing to a broader understanding of the evolving dynamics in this segment of the music industry.

 ## Data Collection
 Data was collected using a Python script that performs scraping of tweets related to the festival and saves the results in CSV files. Each file follows the naming pattern of "tweets_QUERY.csv", where QUERY refers to the search term.

For scraping this data, I used the [twikit package](https://twikit.readthedocs.io/en/latest/twikit.html).

 ## Sentiment Analysis
For sentiment analysis, I used a NLP (Natural Language Processing) model called [Twitter-Roberta-Base-Sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment), which is a version of the RoBERTa model adapted for tweets. This model classifies sentiments into three categories: positive, negative, and neutral.

Analysis Steps:
1. Data Loading: Import the CSV files containing the tweets.
2. Tweet Preprocessing: Apply a function that replaces user mentions with @user, links with http, and converts the text to lowercase.
3. Language Detection: Identify the language of the tweets and filter only those in English since RoBERTa is trained only in English.
4. Sentiment Model Application: Use the NLP model to classify each tweet in terms of sentiment.
5. Statistical Analysis: Count the number of tweets in each sentiment category and calculate descriptive statistics of the sentiment scores.


## Interpretation of Results
The average sentiment score suggests that, overall, the tweets reflect a positive perception of the festival, although there is also a considerable amount of negative feedback. This indicates a spectrum of opinions that may reflect both enthusiasm for the event and the criticisms it faced.

## My next steps
- Analyze how the perception of the festival changed over time, especially between its first edition in 2023 and the current 2024 edition.
- Use topic modeling techniques to identify the main themes discussed in the tweets.
- Create interactive charts and graphs to explore sentiment trends in more depth.
- Create and train my own NLP model

## Some materials and artcles I am using to learn
- Get a look at [this notebook](https://www.kaggle.com/code/leonalinlin/natural-language-processing-nlp-for-beginners)!

- Sure you'll find some of [these videos](https://www.youtube.com/playlist?list=PLFD4-YcGPYO017ejo-wSrguR4kU7NsaH0) interesting
