pickone
=======

PickOne is a small handy library designed let the user choose between a set of
values.

Examples
--------

```python
from pickone import *

PO = PickOne(['foo', 'bar', 'baz'])
PO.ask()
Choose one from [2=baz 0=foo 1=bar]: 1
'bar'

PO.ask()
Choose one from [2=baz 0=foo 1=bar]: foo
'foo'

PO = PickOne({'f': 'foo', 'b': 'bar'}, default='f')
PO.ask()
Choose one from [b=bar f=foo] (default=f): b
'bar'

PO.ask()
Choose one from [b=bar f=foo] (default=f): foo
'foo'

PO.ask()
Choose one from [b=bar f=foo] (default=f): 
'foo'

```
