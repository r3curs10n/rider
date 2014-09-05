def serialize_entry(pl, doc_id):
	return 'd/%d|t/%d|l/%s' % (doc_id, len(pl), ','.join([str(x) for x in pl]))

def serialize_node(prev, entry_list):
	return 'p/%d@%s#' % (prev, '$'.join(entry_list))

def deserialize(block):
	fields = block.split('|')