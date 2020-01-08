import unittest
import datetime
from . import exception
from .models import Commander, System, Status

class CommanderTest(unittest.TestCase):

  def test_commander_public_IHFYD(self):
    cmdr = Commander("IHaveFuelYouDont")

    # position
    coords = cmdr.currentPosition
    self.assertEqual(25.40625, coords['x'])
    self.assertEqual(-31.0625, coords['y'])
    self.assertEqual(41.625, coords['z'])

    # system
    self.assertEqual("Dromi", cmdr.currentSystem)

    # last activity
    self.assertIsNotNone(cmdr.lastActivity)

    # profile
    self.assertEqual("https://www.edsm.net/en/user/profile/id/86423/cmdr/IHaveFuelYouDont", cmdr.profileUrl)

  def test_commander_profileUrl_cache(self):
    cmdr = Commander("shouldntMatter")
    cmdr.__profileUrl__ = "something_random"
    self.assertEqual("something_random", cmdr.profileUrl)

  def test_commander_notFound(self):
    cmdr = Commander("udofsiadefsudtirasedjutrsotusiae")
    with self.assertRaises(exception.CommanderNotFoundError):
      cmdr.currentPosition
    with self.assertRaises(exception.CommanderNotFoundError):
      cmdr.currentSystem
    with self.assertRaises(exception.CommanderNotFoundError):
      cmdr.lastActivity
    with self.assertRaises(exception.CommanderNotFoundError):
      cmdr.profileUrl

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
    self.assertRaises(exception.SystemNotFoundError, System("Lol").fetch)

  def test_getSystems_search(self):
    systems = System.getSystems("Pho Aoscs AA-A h")

    self.assertEqual(3, len(systems))

    system = systems[0]
    self.assertEqual("Pho Aoscs AA-A h0", system.name)
    self.assertEqual(47400376, system.id)
    self.assertEqual(2394415, system.id64)

    self.assertEqual(-3270.65625, system.coords['x'])
    self.assertEqual(3135.5625, system.coords['y'])
    self.assertEqual(24347.125, system.coords['z'])

    system = systems[1]
    self.assertEqual("Pho Aoscs AA-A h1", system.name)
    self.assertEqual(34320464, system.id)
    self.assertEqual(10783023, system.id64)

    self.assertEqual(-3201.15625, system.coords['x'])
    self.assertEqual(3247.8125, system.coords['y'])
    self.assertEqual(24244.46875, system.coords['z'])

    system = systems[2]
    self.assertEqual("Pho Aoscs AA-A h3", system.name)
    self.assertEqual(29715014, system.id)
    self.assertEqual(27560239, system.id64)

    self.assertEqual(-3213.9375, system.coords['x'])
    self.assertEqual(3225.90625, system.coords['y'])
    self.assertEqual(24485.21875, system.coords['z'])

  def test_getSystems_list(self):
    systems = System.getSystems("Sol", "Beagle Point")

    sol = systems[1]
    self.assertEqual("Sol", sol.name)

    # ids
    self.assertEqual(27, sol.id)
    self.assertEqual(10477373803, sol.id64)

    # coordinates
    self.assertTrue(sol.coords)
    self.assertEqual(sol.coords['x'], 0)
    self.assertEqual(sol.coords['y'], 0)
    self.assertEqual(sol.coords['z'], 0)

    beagle = systems[0]
    self.assertEqual("Beagle Point", beagle.name)

    # ids
    self.assertEqual(124406, beagle.id)
    self.assertEqual(81973396946, beagle.id64)

    # coordinates
    self.assertTrue(beagle.coords)
    self.assertEqual(beagle.coords['x'], -1111.5625)
    self.assertEqual(beagle.coords['y'], -134.21875)
    self.assertEqual(beagle.coords['z'], 65269.75)

  def test_eq(self):
    self.assertEqual(System("test", id=1, id64=64), System("other", id=1,
      id64=64))
    self.assertNotEqual(System("test", id=1, id64=64), System("test", id=1,
      id64=65))
    self.assertNotEqual(System("test", id=1, id64=64), System("test", id=2,
      id64=64))

  def test_lt(self):
    self.assertLess(System("test"), System("test2"))
    self.assertLess(System("test 2"), System("test 12"))
    self.assertLess(System("Col 50 Sector"), System("Col 285 Sector"))
    self.assertLess(System("Col 285 Sector"), System("Col 500 Sector"))
    self.assertLess(System("Pho Aoscs AA-A h0"), System("Pho Aoscs AA-A h1"))

  def test_gt(self):
    self.assertGreater(System("test2"), System("test"))
    self.assertGreater(System("test 12"), System("test 2"))
    self.assertGreater(System("Col 285 Sector"), System("Col 50 Sector"))
    self.assertGreater(System("Col 500 Sector"), System("Col 285 Sector"))
    self.assertGreater(System("Pho Aoscs AA-A h1"), System("Pho Aoscs AA-A h0"))
