from textblob import TextBlob



blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
