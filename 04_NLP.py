import spacy

nlp = spacy.load("en_core_web_sm")

mystring = 'We\'

doc = nlp(u"Tesla is looking at buying U.S. Startup for $6 million")