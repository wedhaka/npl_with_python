import spacy
nlp = spacy.load("en_core_web_sm")

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

pattern_1 = [{'LOWER': 'solarpower'}]
pattern_2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]
pattern_3 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]


matcher.add('SolarPower', [pattern_1, pattern_2, pattern_3])

doc = nlp(u"The Solar power industry continues to grow a solarpower inscreases, Solar-power is")

found_matches = matcher(doc)

print(found_matches)

for match_id, start, end in found_matches: 
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)


pattern_4 = [{'LOWER': 'solarpower'}]
pattern_5 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '*'}, {'LOWER': 'power'}]

matcher.add('SolarPower', [pattern_4, pattern_5])
doc2 = nlp(u"Solar--power is solarpower yay!")

found_matches_1 = matcher(doc2)

print(found_matches_1)

for match_id, start, end in found_matches_1: 
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]
    print(match_id, string_id, start, end, span.text)
