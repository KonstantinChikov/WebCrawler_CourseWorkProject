import nltk

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

tags_dict = {
    "CC": "conjuction",
    "CD": "numeral",
    "DT": "determiner",
    "EX": "existential there",
    "IN": "preposition",
    "JJ": "adjective",
    "JJR": "comparative adjective",
    "JJS": "superlative adjective",
    "NN": "noun",
    "VB": "verb",
    "VBZ": "present tense verb, 3rd person singular",
    ".": "punctuation"
}
 
pos_tags_descriptive = []
for (word, tag) in pos_tags:
    pos_tags_descriptive.append((word, tags_dict[tag]))

print(pos_tags_descriptive)