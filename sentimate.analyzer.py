from textblob import TextBlob

# User input
text = input("Enter a sentence: ")

# Analyze sentiment
analysis = TextBlob(text)

# Get polarity score
polarity = analysis.sentiment.polarity

print("\nPolarity Score:", polarity)

# Determine sentiment
if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")