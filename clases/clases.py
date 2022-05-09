from argparse import ArgumentError


import math

class Circulo(object):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        self._radio = r

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, r):
        if r <= 0:
            raise ValueError("El radio debe ser mayor a 0.")
        else:
            self._radio = r

    def get_radio(self):
        return math.pi * (self._radio**2)

    def get_perimeter(self):
        return 2 * math.pi * self._radio
        
    def __str__(self):
        return "Circulo(radio=%d)" % self._radio

    def __mul__(self, other):
        if other <= 0:
            raise ValueError("No se puede multiplica el radio por 0 o menos.")
        new_radio = self._radio * other
        return Circulo(r=new_radio)

