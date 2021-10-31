import nltk
from nltk.corpus import PlaintextCorpusReader

nltk.download('gutenberg')

corpus0 = PlaintextCorpusReader("data/prepared_texts/", "dune.txt")
corpus = nltk.Text(corpus0.words())
print(corpus.concordance('Idaho'))
