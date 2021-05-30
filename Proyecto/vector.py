 import collections
import math

class vector(collections.Sequence):
    PRECISION = 6
    _slots_ = ('_x', '_y', '_hash')

    def _init_(self, x, y):
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)
# constructor vector, parametros x, y

    @property #get x
    def x(self):
        return self._x

    @x.setter #set x
    def x(self, value):
        if self._hash is not None:
            raise ValueError('cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @property #get y
    def y(self):
        return self._y

    @y.setter #set y
    def y(self, value):
        if self._hash is not None:
            raise ValueError('cannot set y after hashing')
        self._y = round(value, self.PRECISION)


    def _hash_(self):
        #val (x,y)
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def _len_(self):
        #longitud vec (x,y)=2
        return 2

    def _getitem_(self, index):
        #get1= x ; get2=y
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def copy(self):
        #copia el vector
        type_self = type(self)
        return type_self(self.x, self.y)