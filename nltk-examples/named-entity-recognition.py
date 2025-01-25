import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Barack Obama was born in Hawaii and became the President of the United States.")
for ent in doc.ents:
    print(ent.text, ent.label_)