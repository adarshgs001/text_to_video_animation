# from .custom_ner import custom_entity_recognition
# from .entity_linking import entity_linking
# from .coreference_resolution import resolve_coreferences
# from .multilingual_ner import multilingual_ner

# def extract_entities(text, language="en", use_custom_model=False, link_entities=False, resolve_coref=False):
#     """
#     Extracts entities using different methods based on the input parameters.
    
#     Args:
#         text (str): The input text.
#         language (str): The language for multilingual NER.
#         use_custom_model (bool): Whether to use a custom NER model.
#         link_entities (bool): Whether to link entities to external sources like Wikipedia.
#         resolve_coref (bool): Whether to perform coreference resolution.

#     Returns:
#         dict: A dictionary containing the recognized entities and additional information.
#     """
    
#     # Coreference resolution
#     if resolve_coref:
#         text = resolve_coreferences(text)
    
#     # Custom NER Model
#     if use_custom_model:
#         entities = custom_entity_recognition(text)
#     else:
#         # Multilingual NER or Default English NER
#         entities = multilingual_ner(text, language) if language != "en" else custom_entity_recognition(text)

#     # Entity Linking
#     if link_entities:
#         entities = entity_linking(entities)

#     return entities


# entity_recognition.py

from .coreference_resolution import resolve_coreferences
from .multilingual_ner import multilingual_ner

def extract_entities(text, language="en", use_coref=True):
    """
    Extracts entities using different methods based on the input parameters.
    
    Args:
        text (str): The input text.
        language (str): The language for multilingual NER (default is English).
        use_coref (bool): Whether to perform coreference resolution.
    
    Returns:
        entities (list): A list of entities with their labels.
    """
    
    # Step 1: Coreference Resolution (if enabled)
    if use_coref:
        text = resolve_coreferences(text)
    
    # Step 2: Perform multilingual NER based on the language
    entities = multilingual_ner(text, language)
    
    return entities
