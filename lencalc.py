import cPickle
from os import listdir
from os.path import isfile, join, exists, getsize
import tokenizem
from nltk import clean_html
import signal
import re

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
		title=''
		try:
			title = re.search(r'\<title\>(.*)\</title\>', src, re.DOTALL|re.IGNORECASE)
			title = ' '.join(title.group(1).replace('"', '')[:50].split())
		except Exception, e:
			continue
		signal.alarm(0)
		dl[int(f)] = title
		print f
	print i

f = open('doc_titles', 'wb')
cPickle.dump(dl, f)
f.close()
