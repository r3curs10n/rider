import filter_html, tokenize, job_chunker
from os import listdir
from os.path import isfile, join, getsize
import pickle
from tobinary import *
import sys
import cStringIO

chunk = 10000

fcs = 2000
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

try:
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
				wl[w] = (1, nxt)
				block = serialize_node(-1, nodes[w])
				index_f.write(block)
				nxt += len(block)
			else:
				(doc_count, prev_offset) = wl[w]
				block = serialize_node(prev_offset, nodes[w])
				index_f.write(block)
				wl[w] = (doc_count+1, nxt)
				nxt += len(block)


	for f in file_list:
		doc_id = f.split('/')[-1]
		if fcs_i == fcs:
			fcs_i = 0
			flush_pls(dpl)
			dpl = []
		local_pl = {}
		src = open(f).read()
		src = filter_html.wipe_html(src)
		toks = tokenize.get_tokens(src)
		for (pos, wpos, t) in toks:
			if t not in local_pl:
				local_pl[t] = [(pos, lpos)]
			else:
				local_pl[t].append((pos, lpos))
		dpl.append((doc_id,local_pl))
		i += 1
		fcs_i += 1
		sys.stderr.write(str(i) + '\n')
	flush_pls(dpl)
except:
	index_f.truncate(prev_index_size)

job_chunker.done(chunk)
pickle.dump((wl,cc), open('wdict', 'wb'))
