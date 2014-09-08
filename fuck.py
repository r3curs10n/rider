from nltk import clean_html
import job_chunker
from os.path import getsize
import signal
import sys

def handler(signum, frame):
  raise Exception('duh')

files = job_chunker.get_files(1580000)
print 'sdfaf'

signal.signal(signal.SIGALRM, handler)

i=0
for f in files:
  if getsize(f) > 3000000:
    continue
  signal.alarm(2)
  ff = open(f)
  src = ff.read()
  ff.close()
  try:
    clean_html(src)
  except:
    sys.stderr.write('>>' + f)
    print f
  i+=1
  signal.alarm(0)
  if i%1000==0:
    sys.stderr.write(str(i)+'\n')
    
  
