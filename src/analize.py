from unidecode import unidecode
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter
import codecs
import nltk
import re

filename = '/home/rmartinez/reggaetonsentiment/canciones/songs.txt'

def remove_garbage(text):
        """Remove html tags from a string"""
        import re
        clean = re.compile('(\.|\!|\?|\,|\=|\[|\]|\)|\(|\:|\-)')
        return re.sub(clean, '', text)

with codecs.open(filename, encoding='utf-8') as f:
	content = f.read()
	content = remove_garbage(content.lower())

# toker = RegexpTokenizer(r'\W+|(,.;)+', gaps=True)
#     	nc = p.word_tokenize(content)

# nc = toker.tokenize(content)

nc = word_tokenize(content, 'spanish')

filtered_words = [w for w in nc if not w in stopwords.words('spanish')]

contador = Counter(filtered_words)

print '\n' + 'MOST COMMON' + '\n'

for w, n in contador.most_common(15):
		print('{0}: {1}'.format(w, n))


bigrams = ngrams(filtered_words, 2)

bigCount = Counter(bigrams)

bM = bigCount.most_common(10)

print '\n' + 'BIGRAMS' + '\n'

for i,j in bM:
	text = ''
	for x in i:
		text += x + ' '
	print('{0}: {1}'.format(text, j))


trigrams = ngrams(filtered_words, 3)

trigCount = Counter(trigrams)

tM = trigCount.most_common(10)

print '\n' + 'TRIGRAMS' + '\n'

for i,j in tM:
	text = ''
	for x in i:
		text += x + ' '
	print '%s: %d' % (text, j)