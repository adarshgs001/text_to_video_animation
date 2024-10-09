from transformers import pipeline

# Load the sentiment analysis pipeline and force it to run on CPU
sentiment_pipeline = pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment", device=-1)

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text.
    """
    result = sentiment_pipeline(text)[0]
    return {
        "sentiment": result['label'],
        "confidence": result['score']
    }
