import unittest
from . import exception
from .systemsApi import System

class SystemTest(unittest.TestCase):

  def test_getSystem_sol(self):
    system = System().getSystem("Sol")

    # ids
    self.assertEqual(27, system.id)
    self.assertEqual(10477373803, system.id64)

    # coordinates
    self.assertTrue(system.coords)
    self.assertEqual(system.coords['x'], 0)
    self.assertEqual(system.coords['y'], 0)
    self.assertEqual(system.coords['z'], 0)

    # permit
    self.assertTrue(system.requirePermit)
    self.assertEqual("Sol", system.permitName)

    # information
    self.assertTrue(system.information)
    self.assertEqual("Federation", system.information['allegiance'])
    self.assertTrue('government' in system.information)
    self.assertTrue('faction' in system.information)
    self.assertTrue('factionState' in system.information)
    self.assertTrue('population' in system.information)
    self.assertTrue('security' in system.information)
    self.assertTrue('economy' in system.information)
    self.assertTrue('secondEconomy' in system.information)
    self.assertTrue('reserve' in system.information)

    # primaryStar
    self.assertTrue(system.primaryStar)
    self.assertEqual("G (White-Yellow) Star", system.primaryStar['type'])
    self.assertEqual("Sol", system.primaryStar['name'])
    self.assertTrue(system.primaryStar['isScoopable'])

  def test_getSystem_Beagle(self):
    system = System().getSystem("Beagle Point")

    # ids
    self.assertEqual(124406, system.id)
    self.assertEqual(81973396946, system.id64)

    # coordinates
    self.assertTrue(system.coords)
    self.assertEqual(system.coords['x'], -1111.5625)
    self.assertEqual(system.coords['y'], -134.21875)
    self.assertEqual(system.coords['z'], 65269.75)

    # permit
    self.assertFalse(system.requirePermit)

    # information
    self.assertFalse(system.information)

    # primaryStar
    self.assertTrue(system.primaryStar)
    self.assertEqual("K (Yellow-Orange) Star", system.primaryStar['type'])
    self.assertEqual("Beagle Point", system.primaryStar['name'])
    self.assertTrue(system.primaryStar['isScoopable'])

  def test_getSystem_invalidName(self):
    with self.assertRaises(exception.systemNotFoundError):
      System().getSystem("Lol")
