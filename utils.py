#! /usr/bin/python
import sys,os
import time

arg = sys.argv[1]

files = ['wdict', 'index', 'job_data']

if arg == 'cleanup':
  os.system('rm %s' % ' '.join(files))
elif arg == 'backup':
  bkpdir = 'backup/%s' % str(time.time())
  os.system('mkdir %s' % bkpdir)
  for f in files:
    os.system('cp %s %s' % (f, bkpdir + '/' + f))
else:
  print 'invalid arg'

