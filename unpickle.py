import pickle

# load character positions
with open('character_positions.pickle', 'rb') as handle:
    character_positions = pickle.load(handle)

qwerty = character_positions['qwerty']

# load corpus
f = open('static/1000.txt')
corpus = f.read().split('\r\n')
set_corpus = set(corpus)

# populate results object
for word in range(len(corpus)):
    print corpus[word]