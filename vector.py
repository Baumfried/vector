# -*- coding: utf-8 -*-
"""
Provides a vector class and basic methods
"""

from math import sqrt, acos
from itertools import zip_longest

class Vector:
    eps = 1e-15
    
    def __init__(self, *dimensions):
        self.dimensions = list(dimensions)
        for i in range(len(self.dimensions)):
            comp = self.dimensions[i]
            if type(comp) is not int and abs(comp - round(comp)) < Vector.eps:
                self.dimensions[i] = round(comp)

    def __str__(self):
        s = ''
        for component in self.dimensions:
            s += str(component) + '\n'
        return s
    def __repr__(self):
        return repr(self.dimensions)
    def __eq__(self, other):
        return self.equiv(other)
    def __ne__(self, other):
        return not self.equiv(other)
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __le__(self, other):
        return abs(self) <= abs(other)
    def __ge__(self, other):
        return abs(self) >= abs(other)
    def __gt__(self, other):
        return abs(self) > abs(other)    
    def __abs__(self):
        return sqrt(self*self)    
    def __pos__(self):
        return Vector(*self.dimensions)    
    def __neg__(self):
        return Vector(*[-component if component else 0
                        for component in self.dimensions])
    
    def __add__(self, other):
        try:
            dims_added = list()
            for comp1, comp2 in zip_longest(self.dimensions, other.dimensions):
                if comp1 == None: comp1 = 0
                if comp2 == None: comp2 = 0
                dims_added.append(comp1 + comp2)
        except AttributeError:
            dims_added = [component + other if component else other
                          for component in self.dimensions]
        return Vector(*dims_added)
    
    def __sub__(self, other):
        try:
            dims_subtracted = list()
            for comp1, comp2 in zip_longest(self.dimensions, other.dimensions):
                if comp1 == None: comp1 = 0
                if comp2 == None: comp2 = 0
                dims_subtracted.append(comp1 - comp2)
        except AttributeError:
            dims_subtracted = [component - other if component else -other
                               for component in self.dimensions]
        return Vector(*dims_subtracted)
    
    def __mul__(self, other):
        try:
            scalar_product = 0
            for comp1, comp2 in zip_longest(self.dimensions, other.dimensions):
                if comp1 == None: comp1 = 0
                if comp2 == None: comp2 = 0
                scalar_product += comp1 * comp2
            if abs(scalar_product - round(scalar_product)) < Vector.eps:
                scalar_product = round(scalar_product)
            return scalar_product
        except AttributeError:
            return Vector(*[component * other if component else 0
                           for component in self.dimensions])
    
    def __truediv__(self, other):
        return Vector(*[component / other if component else 0
                        for component in self.dimensions])
    
    def __floordiv__(self, other):
        return Vector(*[component // other if component else 0
                        for component in self.dimensions])
    
    def __mod__(self, other):
        return Vector(*[component % other if component else 0
                        for component in self.dimensions])
    
    def __radd__(self, other):
        return self + other
    def __rsub__(self, other):
        return -self + other
    def __rmul__(self, other):
        return self * other
    
    def __iadd__(self, other):
        self = self + other
        return self
    def __isub__(self, other):
        self = self - other
        return self
    def __imul__(self, other):
        self = self * other
        return self
    def __itruediv__(self, other):
        self = self / other
        return self
    def __ifloordiv__(self, other):
        self = self // other
        return self
    def __imod__(self, other):
        self = self % other
        return self
    
    def equil(self, other):
        return abs(self) == abs(other)
    
    def equiv(self, other):
        for comp1, comp2 in zip_longest(self.dimensions, other.dimensions):
            if not (
                (comp1 == comp2) or
                (comp1 == 0 and comp2 == None) or
                (comp1 == None and comp2 == 0)
            ):
                return False
        return True
    
    def angle(self, *other):
        if len(other) == 0:
            other = Vector(1)
        else:
            other = other[0]
        return acos(self*other/(abs(self)*abs(other)))
    
    def unit(self):
        return Vector(*[component/abs(self) if component else 0
                        for component in self.dimensions])