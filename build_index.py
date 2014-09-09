from nltk import clean_html
import filter_html, tokenizem, job_chunker
from os import listdir
from os.path import isfile, join, getsize
import cPickle
from tobinary import *
import sys
import cStringIO
import signal

def handler(signum, frame):
  raise Exception('timeout')

signal.signal(signal.SIGALRM, handler)

pickle = cPickle

chunk = 470000

fcs = 5000
fcs_i = 0
dpl = []

cc = 0
wl = {}
i=0

nxt=0

index_f = open('index', 'a')
prev_index_size = nxt = getsize('index')

if isfile('wdict'):
	(wl, cc) = pickle.load(open('wdict', 'rb'))

file_list = job_chunker.get_files(chunk)
#file_list = ['test1.html', 'test2.html']

def flush_pls(dpl):
	global nxt
	nodes = {}
	for (doc_id, l) in dpl:
		doc_id = int(doc_id)
		for w in l:
			e = serialize_entry(l[w], doc_id)
			if w not in nodes:
				nodes[w] = []
			nodes[w].append(e)
	for w in nodes:
		if w not in wl:
			wl[w] = (len(nodes[w]), nxt)
			block = serialize_node(-1, nodes[w])
			index_f.write(block)
			nxt += len(block)
		else:
			(doc_count, prev_offset) = wl[w]
			block = serialize_node(prev_offset, nodes[w])
			index_f.write(block)
			wl[w] = (doc_count+len(nodes[w]), nxt)
			nxt += len(block)

def begin_indexing():
	global file_list
	global wl
	global fcs
	global fcs_i
	global dpl
	global cc
	global i
	global nxt
	global chunk
	global prev_index_size
	global index_f
	for f in file_list:
		doc_id = f.split('/')[-1]
		if fcs_i == fcs:
			fcs_i = 0
			flush_pls(dpl)
			dpl = []
		local_pl = {}
		if getsize(f) > 3000000:
			continue
		fptr = open(f)
		src = fptr.read().lower()
		fptr.close()
		signal.alarm(2)
		try:
			src = clean_html(src)
		except Exception, e:
			continue
		signal.alarm(0)
		toks = tokenizem.get_tokens(src)
		for (pos, t) in toks:
			if len(t) > 15:
				continue
			if t not in local_pl:
				local_pl[t] = [pos]
			else:
				local_pl[t].append(pos)
		dpl.append((doc_id,local_pl))
		i += 1
		fcs_i += 1
		#sys.stderr.write(str(i) + '\n')
		if i % 1000 == 0:
		  print i
	flush_pls(dpl)
try:
	begin_indexing()
	pass
except:
	index_f.truncate(prev_index_size)
	index_f.close()
	print 'indexing failed'
	sys.exit(1)
job_chunker.done(chunk)
dd = open('wdict', 'wb')
pickle.dump((wl,cc), dd)

index_f.close()
dd.close()
