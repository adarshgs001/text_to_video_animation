import spacy

# Load a pre-trained custom model (assuming you trained a custom NER model)
def custom_entity_recognition(text):
    nlp = spacy.load("path_to_your_custom_model")  # Load your custom model
    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
