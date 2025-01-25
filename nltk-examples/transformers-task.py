from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline
classifier = pipeline('sentiment-analysis')

# Analyze sentiment
result = classifier("I love NLP!")
print(result)