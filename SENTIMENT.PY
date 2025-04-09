from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😀"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Input
text = input("Enter a sentence to analyze: ")
result = analyze_sentiment(text)
print("Sentiment:", result)
