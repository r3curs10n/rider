import re
import sys
sys.path.append('/home/shreyas/')
import nltk
rd = None

def fill_whitespace(m):
  rep = []
  for i in xrange(len(m.group(0))):
    r.append(' ')
  return ''.join(rep)

def wipe_tag(tag, str):
  r = re.compile(r'\<' + tag + r'.*?\>', re.IGNORECASE|re.MULTILINE|re.DOTALL)
  str = r.sub(fill_whitespace, str)
  r = re.compile(r'\</' + tag + r'\>', re.IGNORECASE|re.MULTILINE)
  str = r.sub(fill_whitespace, str)
  return str

def wipe_tag_and_contents(tag, str):
  r = re.compile(r'\<' + tag + r'.*?\>.*?\</' + tag + r'\>', re.IGNORECASE|re.MULTILINE|re.DOTALL)
  str = r.sub(fill_whitespace, str)
  return str

def wipe_comments(str):
  r = re.compile(r'\<!--.*?--\>', re.MULTILINE|re.DOTALL)
  str = r.sub(fill_whitespace, str)
  return str

src = '''
hello world <script src="asdf">slkj sldfj sdlf</script> world hello
'''
#src = open('0/4').read()

tags = ['style', 'center', 'font', 'head', 'body', 'div', 'table', 'p', 'tr', 'td', 'th', 'b', 'i', 'strong', 'span', '    title', 'meta', 'a', 'link', 'html', '!doctype', 'ul', 'ol', 'li', 'sup', 'sub', 'h1', 'h2', 'h3', 'h4', 'h5']
ctags = ['script', 'form', 'em']

def wipe_html(src):
  return nltk.clean_html(src)
  global rd
  global tags
  global ctags
  if rd == None:
    print 'sfdsafsfdsaf'
    rd = {}
    rd['comment'] = re.compile(r'\<!--.*?--\>', re.MULTILINE|re.DOTALL)
    for t in tags:
      rd['o_'+t] = re.compile(r'\<' + t + r'.*?\>', re.IGNORECASE|re.MULTILINE|re.DOTALL)
      rd['c_'+t] = r = re.compile(r'\</' + t + r'\>', re.IGNORECASE|re.MULTILINE)
    for t in ctags:
      rd[t] = re.compile(r'\<' + t + r'.*?\>.*?\</' + t + r'\>', re.IGNORECASE|re.MULTILINE|re.DOTALL)

  for t in tags:
    src = rd['o_'+t].sub(' ', src)
    src = rd['c_'+t].sub(' ', src)

  for t in ctags:
    src = rd[t].sub(' ', src)

  src = rd[t].sub(' ', src)
  return src

#print wipe_html(src)
