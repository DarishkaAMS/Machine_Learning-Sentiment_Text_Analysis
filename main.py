from textblob import TextBlob
from newspaper import Article
# import nltk
#
# nltk.download('punkt')

url = 'https://en.wikipedia.org/wiki/Cartier_(jeweler)'  # neutral 0.06818181818181818
# url = 'https://home.kpmg/ua/en/home/media/press-releases/2019/12/improvement-of-legislation-on-amber.html'  # positive 0.21212121212121213
# url = 'https://www.cfr.org/global-conflict-tracker/conflict/conflict-ukraine'  # negative 0.08522727272727272


article = Article(url)

article.download()
article.parse()
article.nlp()

# text = article.text
text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)
