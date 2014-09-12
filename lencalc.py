import cPickle
from os import listdir
from os.path import isfile, join, exists, getsize
import tokenizem
from nltk import clean_html
import signal

def handler(signum, frame):
  raise Exception('timeout')

signal.signal(signal.SIGALRM, handler)

dl = [(0,0)]*1620000

for i in xrange(162):
	path = str(i)
	files = [x for x in listdir(path) if isfile(path+'/'+x) and x.isdigit()]
	for f in files:
		fn = '%d/%s' % (i, f)
		if getsize(fn) > 3000000:
			continue
		fp = open(fn)
		src = fp.read()
		fp.close()
		signal.alarm(2)
		try:
			src = clean_html(src)
		except Exception, e:
			continue
		signal.alarm(0)
		dl[int(f)] = tokenizem.get_tok_count(src)
	print i

f = open('doc_lengths', 'wb')
cPickle.dump(dl, f)
f.close()
