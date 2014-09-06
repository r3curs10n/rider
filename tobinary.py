def serialize_entry(pl, doc_id):
	return 'd/%d|t/%d|l/%s' % (doc_id, len(pl), ','.join(['(%d,%d)'%(x[0],x[1]) for x in pl]))

def serialize_node(prev, entry_list):
	return 'p/%d@%s#' % (prev, '$'.join(entry_list))

def deserialize(block):
	fields = block.split('|')

def get_node(f, head_ptr):
	node_strs = []
	buf_size = 1024
	while True:
		buf = f.read(1024)
		hp = buf.find('#')
		if hp >= 0:
			buf = buf[:hp]
			node_strs.append(buf)
			break
		node_strs.append(buf)
	node_str = ''.join(node_strs)
	(x,y) = node_str.split('@')
	return (int(x.split('/')[-1]), y)


def entrify(doc):
	fields = doc.split('|')
	dic = {}
	for field in fields:
		(k, v) = field.split('/')
		if k=='l':
			v = v
		else:
			v = int(v)
		dic[k] = v
	return dic

def split_node_body(body):
	docs = body.split('$')[::-1]
	return [entrify(x) for x in docs]

def get_list(f, head_ptr):
	acc = []
	while True:
		(next_ptr, body) = get_node(f, next_ptr)
		acc += split_node_body(body)
		if next_ptr == -1:
			break
	return acc