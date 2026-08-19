import spacy

from spacy import displacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(u"Tesla is looking at buying U.S. Startup for $6 million")

print(displacy.render(doc, style='dep', jupyter=True, options={'distance': 110}))

print(displacy.render(doc, style='ent', jupyter=True))

displacy.serve(doc, style='dep')