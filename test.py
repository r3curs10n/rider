import pickle
from tobinary import deserialize

(wl, cc) = pickle.load(open('wdict', 'rb'))

index = open('index').read()

def extract(i):
	global index
	t = index[i:]
	j = 0
	while (t[j] != '#'):
		j+=1
	t = t[:j]
	(fst, snd) = t.split('@')
	fst = int(fst.split('/')[-1])
	return {'p': fst, 'v': snd}

cc = 0
for word in wl:
	(c, nxt) = wl[word]
	print word
	blk = extract(nxt)
	while True:
		print blk
		if blk['p'] < 0:
			break
		blk = extract(blk['p'])
	cc+=1
	if c>5:
		break