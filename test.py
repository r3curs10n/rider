import pickle
from tobinary import deserialize

(wl, cc) = pickle.load(open('wdict', 'rb'))

index = open('index').read()

def extract(i):
	global index
	t = index[i:]
	j = 0
	while (t[j] != '$'):
		j+=1
	t = t[:j]
	t = t.split('|')
	dic = {}
	for x in t:
		(k, v) = x.split('/')
		if k=='l':
			dic[k] = [int(cc) for cc in v.split(',')]
		else:
			dic[k] = int(v)
	return dic


for word in wl:
	(c, nxt) = wl[word]
	print word
	blk = extract(nxt)
	while True:
		print blk
		if blk['p'] < 0:
			break
		blk = extract(blk['p'])
	break