from tobinary import get_list
from math import log
import cPickle
import os
import sys

from nltk.stem import PorterStemmer

stemmer = None

def base(s):
	global stemmer
	if stemmer == None:
		stemmer = PorterStemmer()
	ss = s
	try:
		ss = stemmer.stem(s)
	except:
		pass
	return ss

(wdict, cc) = (None, None)
f = None
fa = sys.argv[1]
if fa == 'stemmed':
	f = open('index')
	(wdict, cc) = cPickle.load(open('wdict', 'rb'))
else:
	f = open('backup/no_stem_stop_removed/index')
	(wdict, cc) = cPickle.load(open('backup/no_stem_stop_removed/wdict', 'rb'))
print 'index loaded'

doc_lengths = cPickle.load(open('doc_lengths', 'rb'))
avgdl = 0
docsc = 0
for (i,j) in doc_lengths:
	avgdl += i
	if i>0:
		docsc += 1
avgdl = avgdl/docsc

def bm25(dl, tf, idf):
	global avgdl
	k = 1.5
	b = 0.75
	return idf * tf * (k+1) / (tf + k*(1-b+b*dl/avgdl))

def open_doc(doc_id):
	dir_num = doc_id // 10000
	file_num = doc_id
	print 'firefox %d/%d' % (dir_num, file_num)
	os.system('firefox file:///home/shreyas/code/rider/%d/%d' % (dir_num, file_num))


def get_scored_list(term):
	global wdict
	if term not in wdict:
		print term + ' not in'
		return []
	(doc_count, head_ptr) = wdict[term]
	pl = get_list(f, head_ptr)
	for i in pl:
		i['score'] = i['t'] * log(1600000/doc_count, 2.7)
		i['tfidf_score'] = i['t'] * log(1600000/doc_count, 2.7)
		i['tf_score'] = i['t'] + 0.0
		i['bm25_score'] = bm25(doc_lengths[i['d']][0], i['t'], log(1600000/doc_count, 2.7))
	print 'sz: %d' % len(pl)
	return pl
	
def merge_or(pl1, pl2, msf=lambda x,y: x+y):
	i=0
	j=0
	merged = []
	n1 = len(pl1)
	n2 = len(pl2)

	while i<n1 or j<n2:
		if i<n1 and j<n2 and pl1[i]['d'] == pl2[j]['d']:
			md = {
				'd': pl1[i]['d'],
				'score': msf(pl1[i]['score'], pl2[j]['score']),
				'tf_score': msf(pl1[i]['tf_score'], pl2[j]['tf_score']),
				'tfidf_score': msf(pl1[i]['tfidf_score'], pl2[j]['tfidf_score']),
				'bm25_score': msf(pl1[i]['bm25_score'], pl2[j]['bm25_score']),
			}
			merged.append(md)
			i+=1
			j+=1
		elif i<n1 and j==n2 or i<n1 and j<n2 and pl1[i]['d'] > pl2[j]['d']:
			merged.append(pl1[i])
			i+=1
		else:
			merged.append(pl2[j])
			j+=1
	return merged

def merge_and(pl1, pl2, msf=lambda x,y: x*y/(x+y)):
	i=0
	j=0
	merged = []
	n1 = len(pl1)
	n2 = len(pl2)

	while i<n1 or j<n2:
		if i<n1 and j<n2 and pl1[i]['d'] == pl2[j]['d']:
			md = {
				'd': pl1[i]['d'],
				'score': msf(pl1[i]['score'], pl2[j]['score']),
				'tf_score': msf(pl1[i]['tf_score'], pl2[j]['tf_score']),
				'tfidf_score': msf(pl1[i]['tfidf_score'], pl2[j]['tfidf_score']),
				'bm25_score': msf(pl1[i]['bm25_score'], pl2[j]['bm25_score']),
			}
			merged.append(md)
			i+=1
			j+=1
		elif (i<n1 and j==n2) or (i<n1 and j<n2 and pl1[i]['d'] > pl2[j]['d']):
			i+=1
		else:
			j+=1
	return merged

def merge_not(pl1, pl2):
	i=0
	j=0
	merged = []
	n1 = len(pl1)
	n2 = len(pl2)

	while i<n1 or j<n2:
		if i<n1 and j<n2 and pl1[i]['d'] == pl2[j]['d']:
			i+=1
			j+=1
		elif (i<n1 and j==n2) or (i<n1 and j<n2 and pl1[i]['d'] > pl2[j]['d']):
			merged.append(pl1[i])
			i+=1
		else:
			j+=1
	return merged

def phnxt(l1, l2):
	i=0
	j=0
	l1 = l1['l']
	l2 = l2['l']
	n1 = len(l1)
	n2 = len(l2)
	acc=[]
	while i<n1 or j<n2:
		if i<n1 and j<n2 and l1[i]+1 == l2[j]:
			acc.append(l2[j])
			i+=1
			j+=1
		elif (i<n1 and j==n2) or (i<n1 and j<n2 and l1[i]+1 < l2[j]):
			i+=1
		else:
			j+=1
	return acc

def phrasal(terms, msf=lambda x, y: x+y):
	t1l = get_scored_list(terms[0])
	for t in terms[1:]:
		acc = []
		nl = get_scored_list(t)
		i=0
		j=0
		n1 = len(t1l)
		n2 = len(nl)
		while i<n1 or j<n2:
			if i<n1 and j<n2 and t1l[i]['d'] == nl[j]['d']:
				x = phnxt(t1l[i], nl[j])
				if len(x) > 0:
					nl[j]['l'] = x
					nl[j]['score'] = len(x)
					nl[j]['tf_score'] = len(x)
					nl[j]['tfidf_score'] = len(x)
					nl[j]['bm25_score'] = len(x)
					acc.append(nl[j])
				i+=1
				j+=1
			elif (i<n1 and j==n2) or (i<n1 and j<n2 and t1l[i]['d'] > nl[j]['d']):
				i+=1
			else:
				j+=1
		t1l = acc
	return t1l

def andal(terms):
	merged = merge_and(get_scored_list(terms[0]), get_scored_list(terms[1]))
	for t in terms[2:]:
		merged = merge_and(merged, get_scored_list(t))
	return merged

def oral(terms):
	merged = merge_and(get_scored_list(terms[0]), get_scored_list(terms[1]))
	for t in terms[2:]:
		merged = merge_and(merged, get_scored_list(t))
	return merged

if __name__ == '__main__':
	while True:
		query = map(base, raw_input().split())
		print query
		#merged = merge_and(get_scored_list(query[0]), get_scored_list(query[1]))
		#for q in query[2:]:
		#	merge_and(merged, get_scored_list(q))
		merged = andal(query)
		temp = sorted(merged, key=lambda x: -x['score'])[:5]
		print temp
		open_doc(temp[0]['d'])
