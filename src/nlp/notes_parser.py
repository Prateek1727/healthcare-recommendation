import spacy

nlp = spacy.load("en_core_web_sm")

def extract_conditions(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ in ("DISEASE", "CONDITION")]