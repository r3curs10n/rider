import pickle
from os import listdir
from os.path import isfile, join, exists

def load_state():
	jc = {'dir_num':0, 'file_num':0}
	if not exists('job_data'):
		return jc
	f = open('job_data', 'rb')
	jc = pickle.load(f)
	return jc

def get_files(n):

	jc = load_state()

	path = str(jc['dir_num'])
	offset = jc['file_num']
	files = sorted([path+'/'+x for x in listdir(path) if isfile(path+'/'+x) and x.isdigit()], key=lambda x: int(x.split('/')[1]))
	files = files[offset:]
	if len(files)>n:
		return files[:n]
	path = str(jc['dir_num']+1)
	files2 = sorted([path+'/'+x for x in listdir(path) if isfile(path+'/'+x) and x.isdigit()], key=lambda x: int(x.split('/')[1]))
	return files + files2[:n-len(files)]

def done(n):

	jc = load_state()

	path = str(jc['dir_num'])
	offset = jc['file_num']
	files = sorted([path+'/'+x for x in listdir(path) if isfile(path+'/'+x) and x.isdigit()], key=lambda x: int(x.split('/')[1]))
	files = files[offset:]
	if len(files)>n:
		jc['file_num'] += n
	else:
		jc['dir_num'] += 1
		jc['file_num'] = n-len(files)
	f = open('job_data', 'wb')
	pickle.dump(jc, f)