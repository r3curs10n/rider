
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x11\xfe\x180$\x88\xf8\xbd\xa5\xd6\xb3eW\xe2\xce]'
    
_lr_action_items = {'AND':([1,3,4,5,9,10,11,12,],[-1,-2,6,6,-3,-4,6,6,]),'TERM':([0,2,6,7,8,],[1,1,1,1,1,]),'RP':([1,3,5,9,10,11,12,],[-1,-2,9,-3,-4,-6,-5,]),'LP':([0,2,6,7,8,],[2,2,2,2,2,]),'NOT':([1,3,4,5,9,10,11,12,],[-1,-2,7,7,-3,-4,7,-5,]),'PHRASE':([0,2,6,7,8,],[3,3,3,3,3,]),'OR':([1,3,4,5,9,10,11,12,],[-1,-2,8,8,-3,-4,8,-5,]),'$end':([1,3,4,9,10,11,12,],[-1,-2,0,-3,-4,-6,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,2,6,7,8,],[4,5,10,11,12,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> TERM','query',1,'p_query_term','query_eval.py',77),
  ('query -> PHRASE','query',1,'p_query_phrase','query_eval.py',81),
  ('query -> LP query RP','query',3,'p_query_par','query_eval.py',85),
  ('query -> query AND query','query',3,'p_query_bool','query_eval.py',89),
  ('query -> query OR query','query',3,'p_query_bool','query_eval.py',90),
  ('query -> query NOT query','query',3,'p_query_bool','query_eval.py',91),
]
