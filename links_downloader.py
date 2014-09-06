import sys,os

b = int(sys.argv[1])
e = int(sys.argv[2])

path = 'http://172.16.24.76/course/data/aol/'

for i in range(b,e):
  os.system('wget %s%d.tgz --no-proxy' % (path, i))
  os.system('tar xfz %d.tgz' % i)
  print '%d done' % i
