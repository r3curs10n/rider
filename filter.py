import re

def fill_whitespace(m):
  rep = ''
  for i in range(len(m.group(0))):
    rep += ''
  return rep

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
src = open('0/4').read()

def wipe_html(src):
  tags = ['head', 'body', 'div', 'table', 'p', 'tr', 'td', 'th', 'b', 'i', 'strong', 'span', 'title', 'meta', 'a', 'link', 'html', '!doctype', 'ul', 'ol', 'li', 'sup', 'sub', 'h1', 'h2', 'h3', 'h4', 'h5']
  ctags = ['script', 'form', 'em']

  for t in tags:
    src = wipe_tag(t, src)

  for t in ctags:
    src = wipe_tag_and_contents(t, src)

  src = wipe_comments(src)
  return src

print wipe_html(src)
