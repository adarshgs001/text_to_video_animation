import spacy

# Load spaCy's language model
nlp = spacy.load("en_core_web_trf")

def extract_verbs(text):
    """
    Extracts simple and multi-word verbs (phrasal verbs) along with their tenses.
    
    Parameters:
        text (str): The input text.
    
    Returns:
        list: A list of tuples containing the verb and its tense.
    """
    doc = nlp(text)
    verbs = []

    for token in doc:
        # Identify verbs and phrasal verbs
        if token.pos_ == "VERB":
            verb = token.text
            tense = token.morph.get("Tense")
            verbs.append((verb, tense))
        
        # Identify phrasal verbs by checking if the verb is followed by a particle
        if token.dep_ == "prt":
            verb_phrase = f"{token.head.text} {token.text}"
            tense = token.head.morph.get("Tense")
            verbs.append((verb_phrase, tense))
    
    return verbs
