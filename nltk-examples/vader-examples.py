from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
import asyncio

translator = Translator()
sid = SentimentIntensityAnalyzer()

sentences = [
    # "VADER is smart, handsome, and funny.", # positive sentence example
    # "VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
    # "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
    # "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
    # "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
    # "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
    # "The book was good.",         # positive sentence
    # "The book was kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
    # "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
    # "A really bad, horrible book.",       # negative sentence with booster words
    # "At least it isn't a horrible book.", # negated negative sentence with contraction
    # ":) and :D",     # emoticons handled
    # "",              # an empty string is correctly handled
    # "Today sux",     #  negative slang handled
    # "Today sux!",    #  negative slang with punctuation emphasis handled
    # "Today SUX!",    #  negative slang with capitalization emphasis
    # "Today kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
    "World News for Q1 2025", 
    "Hungary set to lose over a billion euros from EU funding.", 
    "Bulgaria to attempt to join the euro by the first of January 2026!", 
    "Ukraine set to survive another year with help from NATO countries mainly from G7.", 
    "Israel set to continue on its war rampage in an attempt of finding peace.", 
    "Russia to double its production of war gear & equipment, in an attempt to push the Ukrainian army to a breaking poin.", 
    "EU and Mercosur(south american union) signed a landmark free trade agreement.", 
    "Japan & China demographic collapse set to continue in 2025 and beyond."
]

# paragraph = "It was one of the worst movies I've seen, despite good reviews. \
# ... Unbelievably bad acting!! Poor direction. VERY poor production. \
# ... The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"

# from nltk import tokenize
# lines_list = tokenize.sent_tokenize(paragraph)
# sentences.extend(lines_list)

# tricky_sentences = [
#     "Most automated sentiment analysis tools are shit.",
#     "VADER sentiment analysis is the shit.",
#     "Sentiment analysis has never been good.",
#     "Sentiment analysis with VADER has never been this good.",
#     "Warren Beatty has never been so entertaining.",
#     "I won't say that the movie is astounding and I wouldn't claim that \
#     the movie is too banal either.",
#     "I like to hate Michael Bay films, but I couldn't fault this one",
#     "I like to hate Michael Bay films, BUT I couldn't help but fault this one",
#     "It's one thing to watch an Uwe Boll film, but another thing entirely \
#     to pay for it",
#     "The movie was too good",
#     "This movie was actually neither that funny, nor super witty.",
#     "This movie doesn't care about cleverness, wit or any other kind of \
#     intelligent humor.",
#     "Those who find ugly meanings in beautiful things are corrupt without \
#     being charming.",
#     "There are slow and repetitive parts, BUT it has just enough spice to \
#     keep it interesting.",
#     "The script is not fantastic, but the acting is decent and the cinematography \
#     is EXCELLENT!",
#     "Roger Dodger is one of the most compelling variations on this theme.",
#     "Roger Dodger is one of the least compelling variations on this theme.",
#     "Roger Dodger is at least compelling as a variation on the theme.",
#     "they fall in love with the product",
#     "but then it breaks",
#     "usually around the time the 90 day warranty expires",
#     "the twin towers collapsed today",
#     "However, Mr. Carter solemnly argues, his client carried out the kidnapping \
#     under orders and in the ''least offensive way possible.''"
# ]

# sentences.extend(tricky_sentences)

# for sentence in sentences:
#     sid = SentimentIntensityAnalyzer()
#     print(sentence)
#     ss = sid.polarity_scores(sentence)
#     for k in sorted(ss):
#         print('{0}: {1}, '.format(k, ss[k]), end='')
#     print()

async def translate_text(originalText):
    async with Translator() as translator:
        result = await translator.translate(originalText, src='en', dest='bg')

    return result

for sentence in sentences:
    print(f"Original: {sentence}")
   
    # Analyze sentiment
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print(f"{k}: {ss[k]}, ", end='')
    print()
   
    # Translate to Bulgarian
    try:
        translated = asyncio.run(translate_text(sentence))
        print(f"Translated (Bulgarian): {translated.text}\n")
    except Exception as e:
        print(f"Translation failed: {e}\n")