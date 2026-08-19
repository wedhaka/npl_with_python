import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(u"I am a runner running in a race because I love to run since i ran today")

# for token in doc : 
    # print(token.text, '\t', token.pos_, token.lemma, '\t', token.lemma_)

def show_lemmas(text) :
    for token in text : 
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')


doc2 = nlp(u"I saw ten mice today!")

show_lemmas(doc2)