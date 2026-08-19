import spacy
nlp = spacy.load("en_core_web_sm")

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

with open('./Textfiles/reaganomics.txt') as f :
    doc3 = nlp(f.read())

phrase_list = ['Voodo economics', 'supply-side economics', 'trickle-down economics', 'free-market economics']

phrase_patterns = [nlp(text) for text in phrase_list]

matcher.add('EconMatcher', [*phrase_patterns])

found_matcher = matcher(doc3)

print(found_matcher)

for match_id, start, end in found_matcher: 
    string_id = nlp.vocab.strings[match_id]
    span = doc3[start:end]
    print(match_id, string_id, start, end, span.text)
