def serialize(prev, pl):
	return 'p/%d|t/%d|l/%s$' % (prev, len(pl), ','.join([str(x) for x in pl]))

def deserialize(block):
	fields = block.split('|')