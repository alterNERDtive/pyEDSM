import unittest
import datetime
from . import exception
from .models import System, Status

class StatusTest(unittest.TestCase):

  def test_Status_initial(self):
    status = Status()
    self.assertIsNotNone(status.lastUpdate)
    self.assertIsNotNone(status.type)
    self.assertIsNotNone(status.message)
    self.assertIsNotNone(status.status)

  def test_Status_cacheUpdate(self):
    status = Status()
    # populate initially
    status.forceUpdate()
    lastCacheTime = status.cachedAt
    status.cachedAt = datetime.datetime.now() - datetime.timedelta(minutes=2, seconds=30)
    status.status
    # should have updated now
    self.assertNotEqual(lastCacheTime, status.cachedAt)
    lastCacheTime = status.cachedAt
    # force update
    status.forceUpdate()
    self.assertNotEqual(lastCacheTime, status.cachedAt)

class SystemTest(unittest.TestCase):

  def test_System_Sol(self):
    system = System("Sol").fetch()

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

  def test_BodyCount_Sol(self):
    self.assertEqual(40, System("Sol").bodyCount)

  def test_System_Beagle(self):
    system = System("Beagle Point").fetch()

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
    self.assertEqual(1, len(system.information))
    self.assertTrue(system.information['cachedAt'])

    # primaryStar
    self.assertTrue(system.primaryStar)
    self.assertEqual("K (Yellow-Orange) Star", system.primaryStar['type'])
    self.assertEqual("Beagle Point", system.primaryStar['name'])
    self.assertTrue(system.primaryStar['isScoopable'])

  def test_BodyCount_Beagle(self):
    self.assertEqual(10, System("Beagle Point").bodyCount)

  # FIXXME: I need some tests for the individual getters.

  def test_System_invalidName(self):
    with self.assertRaises(exception.SystemNotFoundError):
      # FIXXME: I should probably look for the system at instance time …
      system = System("Lol").fetch()
