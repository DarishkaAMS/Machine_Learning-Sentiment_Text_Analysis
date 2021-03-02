from textblob import TextBlob

with open('Machine_Learning-Sentiment_Text_Analysis\own_text.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
