from tobinary import get_list
import pickle
import os

(wdict, cc) = pickle.load(open('wdict', 'rb'))
f = open('index')
print 'loaded'

def open_doc(doc_id):
	dir_num = doc_id // 10000
	file_num = doc_id
	print 'firefox %d/%d' % (dir_num, file_num)
	os.system('firefox %d/%d' % (dir_num, file_num))

while True:
	query = raw_input()
	if query not in wdict:
		print '0'
		continue
	(doc_count, head_ptr) = wdict[query]
	print 'docs found: %d' % doc_count
	pl = get_list(f, head_ptr)
	pl.sort(key=lambda x: -x['t'])
	print len(pl)
	print 'tf %d' % pl[0]['t']
	open_doc(pl[0]['d'])
