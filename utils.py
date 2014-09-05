#! /usr/bin/python
import sys,os
import time

arg = sys.argv[1]

files = ['wdict', 'index', 'job_data']

if arg == 'cleanup':
  os.system('rm %s' % ' '.join(files))
elif arg == 'backup':
  bkpdir = 'backup/%s' % str(time.time())
  for f in files:
    os.system('mkdir %s' % bkpdir)
    os.system('mv %s %s' % (f, bkpdir + '/' + f))
else:
  print 'invalid arg'

