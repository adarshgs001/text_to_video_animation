# multilingual_ner.py

from transformers import pipeline

def multilingual_ner(text, language="en"):
    """
    Performs Named Entity Recognition (NER) in multiple languages.
    
    Args:
        text (str): The input text.
        language (str): The language code (default is 'en' for English).
    
    Returns:
        entities (list): A list of extracted entities with labels.
    """
    
    # Use a multilingual NER model from Hugging Face
    if language == "en":
        model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
    elif language == "de":
        model_name = "dbmdz/bert-large-cased-finetuned-conll03-german"
    else:
        model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"  # Default to English
    
    # Initialize the NER pipeline
    nlp = pipeline("ner", model=model_name)
    
    # Perform NER
    entities = nlp(text)
    
    return [(ent['word'], ent['entity']) for ent in entities]
