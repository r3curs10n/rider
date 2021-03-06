
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x91\\\x98rH\xbf\xab\xbf_M\xb1\xeaO\x9f\x14\xf4'
    
_lr_action_items = {'AND':([1,3,4,5,6,10,11,12,13,],[-2,-3,7,7,7,-4,-5,7,7,]),'TERM':([0,1,2,7,8,9,],[1,1,1,1,1,1,]),'RP':([1,3,5,6,10,11,12,13,],[-2,-3,-1,10,-4,-5,-7,-6,]),'LP':([0,1,2,7,8,9,],[2,2,2,2,2,2,]),'NOT':([1,3,4,5,6,10,11,12,13,],[-2,-3,8,8,8,-4,-5,-7,-6,]),'PHRASE':([0,1,2,7,8,9,],[3,3,3,3,3,3,]),'OR':([1,3,4,5,6,10,11,12,13,],[-2,-3,9,9,9,-4,-5,9,-6,]),'$end':([1,3,4,5,10,11,12,13,],[-2,-3,0,-1,-4,-5,-7,-6,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,1,2,7,8,9,],[4,5,6,11,12,13,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> TERM query','query',2,'p_query_terms','/home/shreyas/code/rider/query_eval.py',56),
  ('query -> TERM','query',1,'p_query_term','/home/shreyas/code/rider/query_eval.py',60),
  ('query -> PHRASE','query',1,'p_query_phrase','/home/shreyas/code/rider/query_eval.py',64),
  ('query -> LP query RP','query',3,'p_query_par','/home/shreyas/code/rider/query_eval.py',68),
  ('query -> query AND query','query',3,'p_query_bool','/home/shreyas/code/rider/query_eval.py',72),
  ('query -> query OR query','query',3,'p_query_bool','/home/shreyas/code/rider/query_eval.py',73),
  ('query -> query NOT query','query',3,'p_query_bool','/home/shreyas/code/rider/query_eval.py',74),
]
