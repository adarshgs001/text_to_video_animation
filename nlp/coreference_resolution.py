# import spacy

# # Assuming spaCy with neuralcoref
# def resolve_coreferences(text):
#     nlp = spacy.load('en_core_web_trf')  # Transformer-based model
#     doc = nlp(text)

#     if doc._.has_coref:
#         resolved_text = doc._.coref_resolved  # Resolved text with coreferences replaced
#     else:
#         resolved_text = text

#     return resolved_text


# from transformers import pipeline

# def resolve_coreferences(text):
#     # Load a coreference resolution pipeline from Hugging Face
#     coref_pipeline = pipeline("coreference-resolution", model="allenai/coref-spanbert-large")

#     # Perform coreference resolution on the text
#     coref_result = coref_pipeline(text)
    
#     # Assuming the pipeline returns resolved text (adjust as per the API's output structure)
#     resolved_text = coref_result[0]["resolved_text"]

#     return resolved_text

from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

def resolve_coreferences(text):
    # Load another model for coreference resolution
    tokenizer = AutoTokenizer.from_pretrained("bert-large-cased")
    model = AutoModelForTokenClassification.from_pretrained("bert-large-cased")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    coref_result = nlp(text)

    # Process the result and return resolved text (placeholder logic)
    resolved_text = text  # Replace with actual coreference resolution logic based on the model output
    
    return resolved_text
