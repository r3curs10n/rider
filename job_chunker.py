import pickle
from os import listdir
from os.path import isfile, join, exists

def load_state():
	jc = {'dir_num':0, 'file_num':0}
	if not exists('job_data'):
		return jc
	f = open('job_data', 'rb')
	jc = pickle.load(f)
	f.close()
	return jc

def get_file_list(path):
	return sorted([path+'/'+x for x in listdir(path) if isfile(path+'/'+x) and x.isdigit()], key=lambda x: int(x.split('/')[-1]))

def get_files(n):

	jc = load_state()

	path = jc['dir_num']
	offset = jc['file_num']
	acc = []
	while len(acc) < n:
		files = get_file_list(str(path))[offset:]
		if len(files) > n-len(acc):
			acc += files[:n-len(acc)]
			break
		else:
			acc += files
			offset = 0
			path += 1
	return acc

def done(n):

	jc = load_state()

	path = jc['dir_num']
	offset = jc['file_num']

	acc = []
	while len(acc) < n:
		files = get_file_list(str(path))[offset:]
		if len(files) > n-len(acc):
			acc += files[:n-len(acc)]
			offset += n-len(acc)
			break
		else:
			acc += files
			offset = 0
			path += 1

	jc['dir_num'] = path
	jc['file_num'] = offset
	f=open('job_data', 'wb')
	pickle.dump(jc, f)
	f.close()