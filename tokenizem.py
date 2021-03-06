import re
from stemming.porter2 import stem
import sys
sys.path.insert(0, '/home/shreyas/')
#from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = None

fa = sys.argv[1]

def base(s):
	global fa
	global stemmer
	if fa != 'stemmed':
		return s
	if stemmer == None:
		stemmer = PorterStemmer()
	ss = s
	try:
		ss = stemmer.stem(s)
	except:
		pass
	return ss

stopwords = None

def is_stop_word(w):
	global stopwords
	if stopwords == None:
		sl = ["a","able","about","across","after","all","almost","also","am","among","an","and","any","are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either","else","ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how","however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might","most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own","rather","said","say","says","she","should","since","so","some","than","that","the","their","them","then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when","where","which","while","who","whom","why","will","with","would","yet","you","your","ain't","aren't","can't","could've","couldn't","didn't","doesn't","don't","hasn't","he'd","he'll","he's","how'd","how'll","how's","i'd","i'll","i'm","i've","isn't","it's","might've","mightn't","must've","mustn't","shan't","she'd","she'll","she's","should've","shouldn't","that'll","that's","there's","they'd","they'll","they're","they've","wasn't","we'd","we'll","we're","weren't","what'd","what's","when'd","when'll","when's","where'd","where'll","where's","who'd","who'll","who's","why'd","why'll","why's","won't","would've","wouldn't","you'd","you'll","you're","you've"]
		sl += []
		stopwords = {}
		for s in sl:
			stopwords[s] = True
	return w in stopwords

def get_tokens(src):
	src = src.lower()
	r = re.compile('[a-z][a-z\']*[a-z]')
	tok_list = []
	i = -1
	for x in r.finditer(src):
		i+=1
		tok_list.append((i, (x.group(0))))
	return tok_list

def get_tok_count(src):
	src = src.lower()
	r = re.findall('[a-z][a-z\']*[a-z]', src, re.DOTALL)
	cns = 0
	cal = 0
	for x in r:
		cal += 1
		if not is_stop_word(x):
			cns += 1
	return (cns, cal)