import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Example sentence
sentence = "The quick brown foxes are running quickly."

# Tokenization
tokens = word_tokenize(sentence)

# Removing stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Stemming
ps = PorterStemmer()
stemmed_tokens = [ps.stem(token) for token in filtered_tokens]

print(stemmed_tokens)