import unittest

from .base import Positionable
from .models import Commander, System

class BaseTest(unittest.TestCase):

  class Thing(Positionable):
    def __init__(self, coords):
      self.x = coords['x']
      self.y = coords['y']
      self.z = coords['z']

    @property
    def coords(self):
      return {'x': self.x, 'y': self.y, 'z': self.z}

  @classmethod
  def setUpClass(cls):
    cls.nullCoords = {'x': 0, 'y': 0, 'z': 0}
    cls.coords1 = {'x': 471.8999, 'y': 246.4735, 'z': 896.999}
    cls.coords2 = {'x': 939.4226, 'y': 376.74, 'z': 629.0827}
    cls.nullThing = cls.Thing(cls.nullCoords)
    cls.thing1 = cls.Thing(cls.coords1)
    cls.thing2 = cls.Thing(cls.coords2)

  def test_Positionable_distanceTo_withCoords(self):
    self.assertEqual(1043.09, self.thing1.distanceTo(self.nullCoords))
    self.assertEqual(1043.1, self.thing1.distanceTo(self.nullCoords, roundTo=1))

    self.assertEqual(1191.72, self.thing2.distanceTo(self.nullCoords))
    self.assertEqual(1192, self.thing2.distanceTo(self.nullCoords, roundTo=0))

    n = self.thing1.distanceTo(self.thing2.coords)
    self.assertEqual(554.37, n)
    self.assertEqual(n, self.thing2.distanceTo(self.thing1.coords))

    n = self.thing1.distanceTo(self.thing2.coords, roundTo=0)
    self.assertEqual(554, n)
    self.assertEqual(n, self.thing2.distanceTo(self.thing1.coords, roundTo=0))

  def test_Positionable_distanceTo_withPositionable(self):
    self.assertEqual(1043.09, self.thing1.distanceTo(self.nullThing))
    self.assertEqual(1043.1, self.thing1.distanceTo(self.nullThing, roundTo=1))

    self.assertEqual(1191.72, self.thing2.distanceTo(self.nullThing))
    self.assertEqual(1192, self.thing2.distanceTo(self.nullThing, roundTo=0))

    n = self.thing1.distanceTo(self.thing2)
    self.assertEqual(554.37, n)
    self.assertEqual(n, self.thing2.distanceTo(self.thing1))

    n = self.thing1.distanceTo(self.thing2, roundTo=0)
    self.assertEqual(554, n)
    self.assertEqual(n, self.thing2.distanceTo(self.thing1, roundTo=0))

  def test_Positionable_distanceTo_invalidCoords(self):
    invalidCoords = {'x': 0, 'y': 0}
    with self.assertRaises(ValueError):
      self.thing1.distanceTo(invalidCoords)

    invalidCoords = {'x': 0, 'z': 0}
    with self.assertRaises(ValueError):
      self.thing1.distanceTo(invalidCoords)

    invalidCoords = {'z': 0, 'y': 0}
    with self.assertRaises(ValueError):
      self.thing1.distanceTo(invalidCoords)

  def test_Positionable_distanceTo_invalidCoordsObject(self):
    with self.assertRaises(ValueError):
      self.thing1.distanceTo("hello world")
