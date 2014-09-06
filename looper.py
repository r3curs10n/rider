import os
import pickle
from os.path import exists
ret_code=0

def load_state():
	jc = {'dir_num':0, 'file_num':0}
	if not exists('job_data'):
		return jc
	f = open('job_data', 'rb')
	jc = pickle.load(f)
	f.close()
	return jc

jc = load_state()
while ret_code == 0:
	ret_code = os.system('time pypy build_index.py')
	jc = load_state()
	print 'next dir: ' + str(jc['dir_num'])
