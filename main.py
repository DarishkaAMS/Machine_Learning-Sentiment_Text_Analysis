from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

url = 'https://en.wikipedia.org/wiki/Cartier_(jeweler)'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
print(text)
