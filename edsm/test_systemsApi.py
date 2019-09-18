import unittest
from . import exception
from .systemsApi import System

class SystemTest(unittest.TestCase):

  def test_getSystem_Sol(self):
    json = System.getSystem("Sol")

    self.assertEqual("Sol", json['name'])

    # ids
    self.assertEqual(27, json['id'])
    self.assertEqual(10477373803, json['id64'])

    # coordinates
    self.assertTrue(json['coords'])
    self.assertEqual(json['coords']['x'], 0)
    self.assertEqual(json['coords']['y'], 0)
    self.assertEqual(json['coords']['z'], 0)

    # permit
    self.assertTrue(json['requirePermit'])
    self.assertEqual("Sol", json['permitName'])

    # information
    self.assertTrue(json['information'])
    self.assertEqual("Federation", json['information']['allegiance'])
    self.assertTrue('government' in json['information'])
    self.assertTrue('faction' in json['information'])
    self.assertTrue('factionState' in json['information'])
    self.assertTrue('population' in json['information'])
    self.assertTrue('security' in json['information'])
    self.assertTrue('economy' in json['information'])
    self.assertTrue('secondEconomy' in json['information'])
    self.assertTrue('reserve' in json['information'])

    # primaryStar
    self.assertTrue(json['primaryStar'])
    self.assertEqual("G (White-Yellow) Star", json['primaryStar']['type'])
    self.assertEqual("Sol", json['primaryStar']['name'])
    self.assertTrue(json['primaryStar']['isScoopable'])

  def test_getSystem_Beagle(self):
    json = System.getSystem("Beagle Point")

    self.assertEqual("Beagle Point", json['name'])

    # ids
    self.assertEqual(124406, json['id'])
    self.assertEqual(81973396946, json['id64'])

    # coordinates
    self.assertTrue(json['coords'])
    self.assertEqual(json['coords']['x'], -1111.5625)
    self.assertEqual(json['coords']['y'], -134.21875)
    self.assertEqual(json['coords']['z'], 65269.75)

    # permit
    self.assertFalse(json['requirePermit'])

    # information
    self.assertFalse(json['information'])

    # primaryStar
    self.assertTrue(json['primaryStar'])
    self.assertEqual("K (Yellow-Orange) Star", json['primaryStar']['type'])
    self.assertEqual("Beagle Point", json['primaryStar']['name'])
    self.assertTrue(json['primaryStar']['isScoopable'])

  def test_getSystem_invalidName(self):
    with self.assertRaises(exception.systemNotFoundError):
      System.getSystem("Lol")
