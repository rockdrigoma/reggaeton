

from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams
from collections import Counter
import codecs
import nltk
import re

filename = '/home/rmartinez/reggaeton/canciones/re01.txt'

f = codecs.open(filename,'r','utf-8')

content = f.read()

content = content.lower()

toker = RegexpTokenizer(r'\W+|(,.;)+', gaps=True)

nc = toker.tokenize(content)

filtered_words = [w for w in nc if not w in stopwords.words('spanish')]

contador = Counter(filtered_words)

del contador['shaky']
del contador['blam']

print '\n' + 'MOST COMMON' + '\n'

for w, n in contador.most_common(15):
	print '%s: %d' % (w, n)


bigrams = ngrams(filtered_words, 2)

bigCount = Counter(bigrams)

del bigCount['shaky', 'shaky']
del bigCount['blam', 'blam']
del bigCount['oh', 'oh']
del bigCount['ven', 'ven'] 
del bigCount['picky', 'picky']
del bigCount['terremoto', 'terremoto']
del bigCount[u'vaiv\xe9n', 'ven']
del bigCount['vai', u'vaiv\xe9n']
del bigCount['vai', 'vai']
del bigCount['boom', 'vai']
del bigCount['uoh', 'oh']
del bigCount['wo', 'oh']
del bigCount['ven', 'boom']
del bigCount['tras', 'oh']
del bigCount['pa', 'tras']
del bigCount['dale', 'dale']
del bigCount['tras', 'pa']
del bigCount['oh', 'uoh']

bM = bigCount.most_common(10)

print '\n' + 'BIGRAMS' + '\n'

for i,j in bM:
	text = ''
	for x in i:
		text += x + ' '
	print '%s: %d' % (text, j)


trigrams = ngrams(filtered_words, 3)

trigCount = Counter(trigrams)

del trigCount['shaky', 'shaky', 'shaky']
del trigCount['blam', 'blam', 'blam']
del trigCount[u'vaiv\xe9n', 'ven', 'ven']
del trigCount['vai', 'vai', u'vaiv\xe9n']
del trigCount['picky', 'picky', 'picky']
del trigCount['uoh', 'oh', 'oh']
del trigCount['terremoto', 'terremoto', 'terremoto']
del trigCount['vai', u'vaiv\xe9n', 'ven']

tM = trigCount.most_common(10)

print '\n' + 'TRIGRAMS' + '\n'

for i,j in tM:
	text = ''
	for x in i:
		text += x + ' '
	print '%s: %d' % (text, j)