import filter_html, tokenize, job_chunker
from os import listdir
from os.path import isfile, join, getsize
import pickle
from tobinary import serialize, deserialize
import sys

chunk = 5000

cc = 0
wl = {}
i=0

nxt=0

index_f = open('index', 'a')
nxt = getsize('index')

if isfile('wdict'):
	(wl, cc) = pickle.load(open('wdict', 'rb'))

file_list = job_chunker.get_files(chunk)
#file_list = ['test1.html', 'test2.html']
for f in file_list:
	src = open(f).read()
	src = filter_html.wipe_html(src)
	toks = tokenize.get_tokens(src)
	local_pl = {}
	for (pos, t) in toks:
		if t not in local_pl:
			local_pl[t] = [pos]
		else:
			local_pl[t].append(pos)
	for w in local_pl:
		if w not in wl:
			wl[w] = (1, nxt)
			block = serialize(-1, local_pl[w])
			index_f.write(block)
			nxt += len(block)
		else:
			(sz, prev_block_pos) = wl[w]
			wl[w] = (sz+1, nxt)
			block = serialize(prev_block_pos, local_pl[w])
			index_f.write(block)
			nxt += len(block)
	i += 1
	sys.stderr.write(str(i) + '\n')

job_chunker.done(chunk)
pickle.dump((wl,cc), open('wdict', 'wb'))