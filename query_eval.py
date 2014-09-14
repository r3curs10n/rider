from tokenizem import base, is_stop_word
import tf_score
import re

tokens = (
    'TERM','PHRASE',
    'OR','AND','LP','RP',
    'NOT',
    )

# Tokens

t_OR = r'\|'
t_AND = r'\*'
t_LP = r'\('
t_RP = r'\)'
t_NOT = r'\!'

def t_PHRASE(t):
    r'\".*?\"'
    t.value = map(base, t.value[1:-1].lower().split())
    return t

def t_TERM(t):
    r'[^()" \t!|*]+'
    t.value = base(t.value.lower())
    print t.value
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left','NOT'),
    ('left','OR'),
    ('left','AND'),
    )

# dictionary of names
names = { }

def p_query_terms(t):
    'query : TERM query'
    t[0] = tf_score.merge_or(tf_score.get_scored_list(t[1]), t[2])

def p_query_term(t):
    'query : TERM'
    t[0] = tf_score.get_scored_list(t[1])

def p_query_phrase(t):
    'query : PHRASE'
    t[0] = tf_score.phrasal(t[1])

def p_query_par(t):
    'query : LP query RP'
    t[0] = t[2]

def p_query_bool(t):
    '''query : query AND query
             | query OR query
             | query NOT query'''
    if t[2] == '*':
        t[0] = tf_score.merge_and(t[1], t[3])
        print 'AND called'
    elif t[2] == '|':
        t[0] = tf_score.merge_or(t[1], t[3])
        print 'OR called'
    else:
        t[0] = tf_score.merge_not(t[1], t[3])

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

def gen_result(r, titles):
    title = 'untitled'
    if titles=='true':
        f = open('%d/%d'%(r['d']//10000,r['d']))
        src = f.read()
        f.close()
        title = re.search(r'\<title\>(.*)\</title\>', src, re.DOTALL|re.IGNORECASE)
        if title:
            title = ' '.join(title.group(1).replace('"', '')[:50].split())
        else:
            title = 'Unnamed'
        print "##", title
    return '{"title": "%s", "d": "%d", "tf": "%f", "tfidf": "%f", "bm25": "%f"}' % (title, r['d'], r['tf_score'], r['tfidf_score'], r['bm25_score'])

def query_eval(query, mx, ofst, score_by, titles):
    query = query.lower()
    res = sorted(yacc.parse(query), key=lambda x: -x[score_by])[ofst:ofst+mx]
    resd = [gen_result(x, titles) for x in res]
    print 'lol'
    return '[%s]' % ','.join(resd)

if __name__ == '__main__':
    while 1:
        try:
            s = raw_input('query > ')   # Use raw_input on Python 2
        except EOFError:
            break
        #res = sorted(yacc.parse(s), key=lambda x: -x['score'])[:5]
        #print res
        #tf_score.open_doc(res[0]['d'])
        print query_eval(s)