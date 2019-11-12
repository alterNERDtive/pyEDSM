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
    with self.assertRaises(exception.SystemNotFoundError):
      System.getSystem("Lol")

  def test_getIds_Sol(self):
    json = System.getIds("Sol")

    # ids
    self.assertEqual(27, json['id'])
    self.assertEqual(10477373803, json['id64'])

  def test_getIds_Beagle(self):
    json = System.getIds("Beagle Point")

    # ids
    self.assertEqual(124406, json['id'])
    self.assertEqual(81973396946, json['id64'])

  def test_getIds_invalidName(self):
    with self.assertRaises(exception.SystemNotFoundError):
      System.getIds("Lol")

  def test_getCoordinates_Sol(self):
    json = System.getCoordinates("Sol")

    # coordinates
    self.assertTrue(json['coords'])
    self.assertEqual(json['coords']['x'], 0)
    self.assertEqual(json['coords']['y'], 0)
    self.assertEqual(json['coords']['z'], 0)

  def test_getCoordinates_Beagle(self):
    json = System.getCoordinates("Beagle Point")

    # coordinates
    self.assertTrue(json['coords'])
    self.assertEqual(json['coords']['x'], -1111.5625)
    self.assertEqual(json['coords']['y'], -134.21875)
    self.assertEqual(json['coords']['z'], 65269.75)

  def test_getCoordinates_invalidName(self):
    with self.assertRaises(exception.SystemNotFoundError):
      System.getCoordinates("Lol")

  def test_getPermit_Sol(self):
    json = System.getPermit("Sol")

    # permit
    self.assertTrue(json['requirePermit'])
    self.assertEqual("Sol", json['permitName'])

  def test_getPermit_Beagle(self):
    json = System.getPermit("Beagle Point")

    # permit
    self.assertFalse(json['requirePermit'])

  def test_getPermit_invalidName(self):
    with self.assertRaises(exception.SystemNotFoundError):
      System.getPermit("Lol")

  def test_getInformation_Sol(self):
    json = System.getInformation("Sol")

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

  def test_getInformation_Beagle(self):
    json = System.getInformation("Beagle Point")

    # information
    self.assertFalse(json['information'])

  def test_getInformation_invalidName(self):
    with self.assertRaises(exception.SystemNotFoundError):
      System.getInformation("Lol")

  def test_getPrimaryStar_Sol(self):
    json = System.getPrimaryStar("Sol")

    # primaryStar
    self.assertTrue(json['primaryStar'])
    self.assertEqual("G (White-Yellow) Star", json['primaryStar']['type'])
    self.assertEqual("Sol", json['primaryStar']['name'])
    self.assertTrue(json['primaryStar']['isScoopable'])

  def test_getPrimaryStar_Beagle(self):
    json = System.getPrimaryStar("Beagle Point")

    # primaryStar
    self.assertTrue(json['primaryStar'])
    self.assertEqual("K (Yellow-Orange) Star", json['primaryStar']['type'])
    self.assertEqual("Beagle Point", json['primaryStar']['name'])
    self.assertTrue(json['primaryStar']['isScoopable'])

  def test_getPrimaryStar_invalidName(self):
    with self.assertRaises(exception.SystemNotFoundError):
      System.getPrimaryStar("Lol")

  def test_wonkySystemNames(self):
    System.getSystem("BD+49 1280")
    # FIXXME: I remember finding a system with “[]” in the name, but can’t
    # remember … and the search function in the usual tools aren’t very helpful
    # :)
