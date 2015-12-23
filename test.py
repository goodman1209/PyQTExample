class A(object):
    def __repr__(self):
       return 'A()'
	# __nonzero__   for python 2
    def __bool__(self):
       return False

class B(object):
    def __repr__(self):
       return 'B()'
    def __len__(self):
       return 0

class C(object):
    def __repr__(self):
       return 'C()'
    def __cmp__(self, other):
       return 0

class D(object):
    def __repr__(self):
       return 'D()'
    def __eq__(self, other):
       return True

for obj in ['', (), [], {}, 0, 0., A(), B(), C(), D(), None]:
    print('%4s: bool(obj) -> %5s, obj == None -> %5s, obj is None -> %5s' %(repr(obj), bool(obj), obj == None, obj is None))