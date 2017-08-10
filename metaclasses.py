
# metaclass
class BaseMeta(type):

    # assuring presence of the 'bar' method in lower classes
    def __new__(cls, name, bases, body):

        if name is not 'Base' and not 'bar' in body:
            err_desc = "'bar' method is missing in class '%s'" % name
            raise TypeError( err_desc )

        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):

    # raise assert error by changing to 'food'
    def foo(self):
        return 'foo'

###

# veryfing there is 'foo' method in the superclass
assert hasattr(Base, 'foo'), "'foo' is missing"

class Derived(Base):
    def bars(self):
        return self.foo()

dObj = Derived()

print( dObj.bar() )
