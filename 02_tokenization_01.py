import spacy

nlp = spacy.load("en_core_web_sm")

mystring = '"We\'re mvoing to L.A.!"'

print(mystring)
# doc = nlp(u"Tesla is looking at buying U.S. Startup for $6 million")

doc = nlp(mystring)

for token in doc:
    print(token)


doc2 = nlp(u"We're here to help! Send snail-mail, emai support@oursite.com or visit us at http://oursite.com")

for t in doc2:
    print(t)


doc3 = nlp(u"A 5km NYC cab ride costs $10.30")

for tt in doc3 :
    print(tt)

doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")

for ttt in doc4 : 
    print(ttt)