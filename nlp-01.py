import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("SpaCy is working!")
print([token.text for token in doc])