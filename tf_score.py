from tobinary import get_list
import pickle

(wdict, cc) = pickle.load(open('wdict', 'rb'))
f = open('index')

while True:
	query = raw_input()
	if query not in wdict:
		print '0'
		continue
	(doc_count, head_ptr) = wdict[query]
	pl = get_list(f, head_ptr)
	pl.sort(key=lambda x: -x['t'])
	print pl[:5]