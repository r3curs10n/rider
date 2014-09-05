def serialize_entry(pl, doc_id):
	return 'd/%d|t/%d|l/%s' % (doc_id, len(pl), ','.join(['(%d,%d)'%(x[0],x[1]) for x in pl]))

def serialize_node(prev, entry_list):
	return 'p/%d@%s#' % (prev, '$'.join(entry_list))

def deserialize(block):
	fields = block.split('|')