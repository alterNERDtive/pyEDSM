import unittest
from . import exception
from .systemsApi import System, Systems

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

class SystemsTest(unittest.TestCase):

  def test_getSystems_search(self):
    json = Systems.getSystems("Pho Aoscs AA-A h")

    self.assertEqual(3, len(json))

    system = json[0]
    self.assertEqual("Pho Aoscs AA-A h0", system['name'])
    self.assertEqual(47400376, system['id'])
    self.assertEqual(2394415, system['id64'])

    self.assertEqual(-3270.65625, system['coords']['x'])
    self.assertEqual(3135.5625, system['coords']['y'])
    self.assertEqual(24347.125, system['coords']['z'])

    self.assertFalse(system['requirePermit'])
    self.assertFalse(system['information'])

    self.assertEqual("Wolf-Rayet N Star", system['primaryStar']['type'])
    self.assertEqual("Pho Aoscs AA-A h0 A", system['primaryStar']['name'])
    self.assertFalse(system['primaryStar']['isScoopable'])

    system = json[1]
    self.assertEqual("Pho Aoscs AA-A h1", system['name'])
    self.assertEqual(34320464, system['id'])
    self.assertEqual(10783023, system['id64'])

    self.assertEqual(-3201.15625, system['coords']['x'])
    self.assertEqual(3247.8125, system['coords']['y'])
    self.assertEqual(24244.46875, system['coords']['z'])

    self.assertFalse(system['requirePermit'])
    self.assertFalse(system['information'])

    self.assertEqual("O (Blue-White) Star", system['primaryStar']['type'])
    self.assertEqual("Pho Aoscs AA-A h1", system['primaryStar']['name'])
    self.assertTrue(system['primaryStar']['isScoopable'])

    system = json[2]
    self.assertEqual("Pho Aoscs AA-A h3", system['name'])
    self.assertEqual(29715014, system['id'])
    self.assertEqual(27560239, system['id64'])

    self.assertEqual(-3213.9375, system['coords']['x'])
    self.assertEqual(3225.90625, system['coords']['y'])
    self.assertEqual(24485.21875, system['coords']['z'])

    self.assertFalse(system['requirePermit'])
    self.assertFalse(system['information'])

    self.assertEqual("Black Hole", system['primaryStar']['type'])
    self.assertEqual("Pho Aoscs AA-A h3 A", system['primaryStar']['name'])
    self.assertFalse(system['primaryStar']['isScoopable'])

  def test_getSystems_list(self):
    json = Systems.getSystems("Sol", "Beagle Point")

    sol = json[1]
    self.assertEqual("Sol", sol['name'])

    # ids
    self.assertEqual(27, sol['id'])
    self.assertEqual(10477373803, sol['id64'])

    # coordinates
    self.assertTrue(sol['coords'])
    self.assertEqual(sol['coords']['x'], 0)
    self.assertEqual(sol['coords']['y'], 0)
    self.assertEqual(sol['coords']['z'], 0)

    # permit
    self.assertTrue(sol['requirePermit'])
    self.assertEqual("Sol", sol['permitName'])

    # information
    self.assertTrue(sol['information'])
    self.assertEqual("Federation", sol['information']['allegiance'])
    self.assertTrue('government' in sol['information'])
    self.assertTrue('faction' in sol['information'])
    self.assertTrue('factionState' in sol['information'])
    self.assertTrue('population' in sol['information'])
    self.assertTrue('security' in sol['information'])
    self.assertTrue('economy' in sol['information'])
    self.assertTrue('secondEconomy' in sol['information'])
    self.assertTrue('reserve' in sol['information'])

    # primaryStar
    self.assertTrue(sol['primaryStar'])
    self.assertEqual("G (White-Yellow) Star", sol['primaryStar']['type'])
    self.assertEqual("Sol", sol['primaryStar']['name'])
    self.assertTrue(sol['primaryStar']['isScoopable'])

    beagle = json[0]
    self.assertEqual("Beagle Point", beagle['name'])

    # ids
    self.assertEqual(124406, beagle['id'])
    self.assertEqual(81973396946, beagle['id64'])

    # coordinates
    self.assertTrue(beagle['coords'])
    self.assertEqual(beagle['coords']['x'], -1111.5625)
    self.assertEqual(beagle['coords']['y'], -134.21875)
    self.assertEqual(beagle['coords']['z'], 65269.75)

    # permit
    self.assertFalse(beagle['requirePermit'])

    # information
    self.assertFalse(beagle['information'])

    # primaryStar
    self.assertTrue(beagle['primaryStar'])
    self.assertEqual("K (Yellow-Orange) Star", beagle['primaryStar']['type'])
    self.assertEqual("Beagle Point", beagle['primaryStar']['name'])
    self.assertTrue(beagle['primaryStar']['isScoopable'])

  def test_getIds_search(self):
    json = Systems.getIds("Pho Aoscs AA-A h")

    self.assertEqual(3, len(json))

    system = json[0]
    self.assertEqual("Pho Aoscs AA-A h0", system['name'])
    self.assertEqual(47400376, system['id'])
    self.assertEqual(2394415, system['id64'])

    system = json[1]
    self.assertEqual("Pho Aoscs AA-A h1", system['name'])
    self.assertEqual(34320464, system['id'])
    self.assertEqual(10783023, system['id64'])

    system = json[2]
    self.assertEqual("Pho Aoscs AA-A h3", system['name'])
    self.assertEqual(29715014, system['id'])
    self.assertEqual(27560239, system['id64'])

  def test_getIds_list(self):
    json = Systems.getIds("Sol", "Beagle Point")

    sol = json[1]
    self.assertEqual("Sol", sol['name'])

    # ids
    self.assertEqual(27, sol['id'])
    self.assertEqual(10477373803, sol['id64'])

    beagle = json[0]
    self.assertEqual("Beagle Point", beagle['name'])

    # ids
    self.assertEqual(124406, beagle['id'])
    self.assertEqual(81973396946, beagle['id64'])

  def test_getCoordinates_search(self):
    json = Systems.getCoordinates("Pho Aoscs AA-A h")

    self.assertEqual(3, len(json))

    system = json[0]
    self.assertEqual("Pho Aoscs AA-A h0", system['name'])

    self.assertEqual(-3270.65625, system['coords']['x'])
    self.assertEqual(3135.5625, system['coords']['y'])
    self.assertEqual(24347.125, system['coords']['z'])

    system = json[1]
    self.assertEqual("Pho Aoscs AA-A h1", system['name'])

    self.assertEqual(-3201.15625, system['coords']['x'])
    self.assertEqual(3247.8125, system['coords']['y'])
    self.assertEqual(24244.46875, system['coords']['z'])

    system = json[2]
    self.assertEqual("Pho Aoscs AA-A h3", system['name'])

    self.assertEqual(-3213.9375, system['coords']['x'])
    self.assertEqual(3225.90625, system['coords']['y'])
    self.assertEqual(24485.21875, system['coords']['z'])

  def test_getCoordinates_list(self):
    json = Systems.getCoordinates("Sol", "Beagle Point")

    sol = json[1]
    self.assertEqual("Sol", sol['name'])

    # coordinates
    self.assertTrue(sol['coords'])
    self.assertEqual(sol['coords']['x'], 0)
    self.assertEqual(sol['coords']['y'], 0)
    self.assertEqual(sol['coords']['z'], 0)

    beagle = json[0]
    self.assertEqual("Beagle Point", beagle['name'])

    # coordinates
    self.assertTrue(beagle['coords'])
    self.assertEqual(beagle['coords']['x'], -1111.5625)
    self.assertEqual(beagle['coords']['y'], -134.21875)
    self.assertEqual(beagle['coords']['z'], 65269.75)

  def test_getPermit_search(self):
    json = Systems.getSystems("Pho Aoscs AA-A h")

    self.assertEqual(3, len(json))

    system = json[0]

    self.assertFalse(system['requirePermit'])

    system = json[1]

    self.assertFalse(system['requirePermit'])

    system = json[2]

    self.assertFalse(system['requirePermit'])

  def test_getPermit_list(self):
    json = Systems.getPermit("Sol", "Beagle Point")

    sol = json[1]
    self.assertEqual("Sol", sol['name'])

    # permit
    self.assertTrue(sol['requirePermit'])

    beagle = json[0]
    self.assertEqual("Beagle Point", beagle['name'])

    # permit
    self.assertFalse(beagle['requirePermit'])

  def test_getInformation_search(self):
    json = Systems.getInformation("Pho Aoscs AA-A h")

    self.assertEqual(3, len(json))

    system = json[0]

    self.assertFalse(system['information'])

    system = json[1]
    self.assertEqual("Pho Aoscs AA-A h1", system['name'])

    self.assertFalse(system['information'])

    system = json[2]

    self.assertFalse(system['information'])

  def test_getInformation_list(self):
    json = Systems.getInformation("Sol", "Beagle Point")

    sol = json[1]
    self.assertEqual("Sol", sol['name'])

    # information
    self.assertTrue(sol['information'])
    self.assertEqual("Federation", sol['information']['allegiance'])
    self.assertTrue('government' in sol['information'])
    self.assertTrue('faction' in sol['information'])
    self.assertTrue('factionState' in sol['information'])
    self.assertTrue('population' in sol['information'])
    self.assertTrue('security' in sol['information'])
    self.assertTrue('economy' in sol['information'])
    self.assertTrue('secondEconomy' in sol['information'])
    self.assertTrue('reserve' in sol['information'])

    beagle = json[0]
    self.assertEqual("Beagle Point", beagle['name'])

    # information
    self.assertFalse(beagle['information'])

  def test_getPrimaryStar_search(self):
    json = Systems.getPrimaryStar("Pho Aoscs AA-A h")

    self.assertEqual(3, len(json))

    system = json[0]

    self.assertEqual("Wolf-Rayet N Star", system['primaryStar']['type'])
    self.assertEqual("Pho Aoscs AA-A h0 A", system['primaryStar']['name'])
    self.assertFalse(system['primaryStar']['isScoopable'])

    system = json[1]
    self.assertEqual("Pho Aoscs AA-A h1", system['name'])

    self.assertEqual("O (Blue-White) Star", system['primaryStar']['type'])
    self.assertEqual("Pho Aoscs AA-A h1", system['primaryStar']['name'])
    self.assertTrue(system['primaryStar']['isScoopable'])

    system = json[2]
    self.assertEqual("Pho Aoscs AA-A h3", system['name'])

    self.assertEqual("Black Hole", system['primaryStar']['type'])
    self.assertEqual("Pho Aoscs AA-A h3 A", system['primaryStar']['name'])
    self.assertFalse(system['primaryStar']['isScoopable'])

  def test_getPrimaryStar_list(self):
    json = Systems.getPrimaryStar("Sol", "Beagle Point")

    sol = json[1]
    self.assertEqual("Sol", sol['name'])

    # primaryStar
    self.assertTrue(sol['primaryStar'])
    self.assertEqual("G (White-Yellow) Star", sol['primaryStar']['type'])
    self.assertEqual("Sol", sol['primaryStar']['name'])
    self.assertTrue(sol['primaryStar']['isScoopable'])

    beagle = json[0]
    self.assertEqual("Beagle Point", beagle['name'])

    # primaryStar
    self.assertTrue(beagle['primaryStar'])
    self.assertEqual("K (Yellow-Orange) Star", beagle['primaryStar']['type'])
    self.assertEqual("Beagle Point", beagle['primaryStar']['name'])
    self.assertTrue(beagle['primaryStar']['isScoopable'])

  def test_getSystems_nonexistant(self):
    with self.assertRaises(exception.SystemNotFoundError):
      Systems.getSystems("LOL")
    with self.assertRaises(exception.SystemNotFoundError):
      Systems.getSystems("LOL", "WUT")

    json = Systems.getSystems("LOL", "Sol")
    self.assertEqual(1, len(json))
