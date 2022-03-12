import unittest
from . import exception
from .systemApi import Bodies
from .systemApi import Traffic

class BodiesTest(unittest.TestCase):

  def test_getBodies_HD43193(self):
    json = Bodies.getBodies("HD 43193")

    # system data
    self.assertEqual(85920, json['id'])
    self.assertEqual("HD 43193", json['name'])

    # body count
    self.assertEqual(17, len(json['bodies']))

    # star
    star = json['bodies'][0]
    self.assertEqual(219074, star['id'])
    self.assertEqual("HD 43193 A", star['name'])
    self.assertEqual("Star", star['type'])
    self.assertEqual("B (Blue-White) Star", star['subType'])
    self.assertEqual(0, star['distanceToArrival'])
    self.assertTrue(star['isMainStar'])
    self.assertTrue(star['isScoopable'])
    self.assertEqual(760, star['age'])
    self.assertEqual("V", star['luminosity'])
    self.assertEqual(0.443283, star['absoluteMagnitude'])
    self.assertEqual(14.5625, star['solarMasses'])
    self.assertEqual(5.3612057397555715, star['solarRadius'])
    self.assertEqual(30995, star['surfaceTemperature'])
    self.assertEqual(277.5355324074074, star['orbitalPeriod'])
    self.assertEqual(0.4615586345240675, star['semiMajorAxis'])
    self.assertEqual(0.275417, star['orbitalEccentricity'])
    self.assertEqual(73.390816, star['orbitalInclination'])
    self.assertEqual(23.460678, star['argOfPeriapsis'])
    self.assertEqual(2.2797341579861112, star['rotationalPeriod'])
    self.assertFalse(star['rotationalPeriodTidallyLocked'])
    self.assertEqual(None, star['axialTilt'])

    # planet
    planet = json['bodies'][15]
    self.assertEqual(311417, planet['id'])
    self.assertEqual("HD 43193 CD 7 a", planet['name'])
    self.assertEqual("Planet", planet['type'])
    self.assertEqual("Class IV gas giant", planet['subType'])
    # self.assertEqual(17963, planet['distanceToArrival']) # this sadly varies due to orbiting …
    self.assertFalse(planet['isLandable'])
    self.assertEqual(11.175634423255477, planet['gravity'])
    self.assertEqual(1574.405762, planet['earthMasses'])
    self.assertEqual(75701.896, planet['radius'])
    self.assertEqual(1021, planet['surfaceTemperature'])
    self.assertEqual("No volcanism", planet['volcanismType'])
    self.assertEqual("No atmosphere", planet['atmosphereType'])
    self.assertEqual("Not terraformable", planet['terraformingState'])
    self.assertEqual(55.31602430555556, planet['orbitalPeriod'])
    self.assertEqual(0.11103302421536405, planet['semiMajorAxis'])
    self.assertEqual(None, planet['orbitalEccentricity'])
    self.assertEqual(28.739708, planet['orbitalInclination'])
    self.assertEqual(248.851364, planet['argOfPeriapsis'])
    self.assertEqual(57.64743634259259, planet['rotationalPeriod'])
    self.assertFalse(planet['rotationalPeriodTidallyLocked'])
    self.assertEqual(0.198277, planet['axialTilt'])

  def test_getBodiesById_HD43193(self):
    json = Bodies.getBodiesById(85920)

    # system data
    self.assertEqual(85920, json['id'])
    self.assertEqual("HD 43193", json['name'])

    # body count
    self.assertEqual(17, len(json['bodies']))

    # star
    star = json['bodies'][0]
    self.assertEqual(219074, star['id'])
    self.assertEqual("HD 43193 A", star['name'])
    self.assertEqual("Star", star['type'])
    self.assertEqual("B (Blue-White) Star", star['subType'])
    self.assertEqual(0, star['distanceToArrival'])
    self.assertTrue(star['isMainStar'])
    self.assertTrue(star['isScoopable'])
    self.assertEqual(760, star['age'])
    self.assertEqual("V", star['luminosity'])
    self.assertEqual(0.443283, star['absoluteMagnitude'])
    self.assertEqual(14.5625, star['solarMasses'])
    self.assertEqual(5.3612057397555715, star['solarRadius'])
    self.assertEqual(30995, star['surfaceTemperature'])
    self.assertEqual(277.5355324074074, star['orbitalPeriod'])
    self.assertEqual(0.4615586345240675, star['semiMajorAxis'])
    self.assertEqual(0.275417, star['orbitalEccentricity'])
    self.assertEqual(73.390816, star['orbitalInclination'])
    self.assertEqual(23.460678, star['argOfPeriapsis'])
    self.assertEqual(2.2797341579861112, star['rotationalPeriod'])
    self.assertFalse(star['rotationalPeriodTidallyLocked'])
    self.assertEqual(None, star['axialTilt'])

    # planet
    planet = json['bodies'][15]
    self.assertEqual(311417, planet['id'])
    self.assertEqual("HD 43193 CD 7 a", planet['name'])
    self.assertEqual("Planet", planet['type'])
    self.assertEqual("Class IV gas giant", planet['subType'])
    # self.assertEqual(17963, planet['distanceToArrival']) # this sadly varies due to orbiting …
    self.assertFalse(planet['isLandable'])
    self.assertEqual(11.175634423255477, planet['gravity'])
    self.assertEqual(1574.405762, planet['earthMasses'])
    self.assertEqual(75701.896, planet['radius'])
    self.assertEqual(1021, planet['surfaceTemperature'])
    self.assertEqual("No volcanism", planet['volcanismType'])
    self.assertEqual("No atmosphere", planet['atmosphereType'])
    self.assertEqual("Not terraformable", planet['terraformingState'])
    self.assertEqual(55.31602430555556, planet['orbitalPeriod'])
    self.assertEqual(0.11103302421536405, planet['semiMajorAxis'])
    self.assertEqual(None, planet['orbitalEccentricity'])
    self.assertEqual(28.739708, planet['orbitalInclination'])
    self.assertEqual(248.851364, planet['argOfPeriapsis'])
    self.assertEqual(57.64743634259259, planet['rotationalPeriod'])
    self.assertFalse(planet['rotationalPeriodTidallyLocked'])
    self.assertEqual(0.198277, planet['axialTilt'])

  def test_wonkySystemNames(self):
    Bodies.getBodies("BD+49 1280")
    # FIXXME: I remember finding a system with “[]” in the name, but can’t
    # remember … and the search function in the usual tools aren’t very helpful
    # :)
  
class TrafficTest(unittest.TestCase):
  def test_getTraffic_Sol(self):
    json = Traffic.getTraffic('Sol')

    self.assertIs(type(json), dict)

    # system data
    self.assertEqual(27, json['id'])
    self.assertEqual(10477373803, json['id64'])
    self.assertEqual('Sol', json['name'])
    self.assertEqual('https://www.edsm.net/en/system/id/27/name/Sol', json['url'])
    self.assertEqual('J. Calvert (Joshua)', json['discovery']['commander'])
    self.assertEqual('2014-11-18 18:21:43', json['discovery']['date'])

    # format
    self.assertIn('breakdown', json)
    self.assertIs(type(json['breakdown']), dict)

    self.assertIn('traffic', json)
    self.assertIn('total', json['traffic'])
    self.assertIn('week', json['traffic'])
    self.assertIn('day', json['traffic'])
    self.assertIs(type(json['traffic']), dict)
    self.assertIs(type(json['traffic']['total']), int)
    self.assertIs(type(json['traffic']['week']), int)
    self.assertIs(type(json['traffic']['day']), int)

  def test_getTrafficById_Sol(self):
    json = Traffic.getTrafficById(27)

    self.assertIs(type(json), dict)

    # system data
    self.assertEqual(27, json['id'])
    self.assertEqual(10477373803, json['id64'])
    self.assertEqual('Sol', json['name'])
    self.assertEqual('https://www.edsm.net/en/system/id/27/name/Sol', json['url'])
    self.assertEqual('J. Calvert (Joshua)', json['discovery']['commander'])
    self.assertEqual('2014-11-18 18:21:43', json['discovery']['date'])

    # format
    self.assertIn('breakdown', json)
    self.assertIs(type(json['breakdown']), dict)

    self.assertIn('traffic', json)
    self.assertIn('total', json['traffic'])
    self.assertIn('week', json['traffic'])
    self.assertIn('day', json['traffic'])
    self.assertIs(type(json['traffic']), dict)
    self.assertIs(type(json['traffic']['total']), int)
    self.assertIs(type(json['traffic']['week']), int)
    self.assertIs(type(json['traffic']['day']), int)

  def test_getTraffic_HD43193(self):
    json = Traffic.getTraffic('HD 43193')
    
    self.assertIs(type(json), dict)
    
    # system data
    self.assertEqual(85920, json['id'])
    self.assertEqual(167244341, json['id64'])
    self.assertEqual('HD 43193', json['name'])
    self.assertEqual('https://www.edsm.net/en/system/id/85920/name/HD+43193', json['url'])
    self.assertEqual('Virosh Lich', json['discovery']['commander'])
    self.assertEqual('2015-02-11 19:20:59', json['discovery']['date'])

    # format
    self.assertIn('breakdown', json)
    self.assertIs(type(json['breakdown']), dict)

    self.assertIn('traffic', json)
    self.assertIn('total', json['traffic'])
    self.assertIn('week', json['traffic'])
    self.assertIn('day', json['traffic'])
    self.assertIs(type(json['traffic']), dict)
    self.assertIs(type(json['traffic']['total']), int)
    self.assertIs(type(json['traffic']['week']), int)
    self.assertIs(type(json['traffic']['day']), int)

  def test_getTrafficById_HD43193(self):
    json = Traffic.getTrafficById(85920)

    self.assertIs(type(json), dict)
    
    # system data
    self.assertEqual(85920, json['id'])
    self.assertEqual(167244341, json['id64'])
    self.assertEqual('HD 43193', json['name'])
    self.assertEqual('https://www.edsm.net/en/system/id/85920/name/HD+43193', json['url'])
    self.assertEqual('Virosh Lich', json['discovery']['commander'])
    self.assertEqual('2015-02-11 19:20:59', json['discovery']['date'])

    # format
    self.assertIn('breakdown', json)
    self.assertIs(type(json['breakdown']), dict)

    self.assertIn('traffic', json)
    self.assertIn('total', json['traffic'])
    self.assertIn('week', json['traffic'])
    self.assertIn('day', json['traffic'])
    self.assertIs(type(json['traffic']), dict)
    self.assertIs(type(json['traffic']['total']), int)
    self.assertIs(type(json['traffic']['week']), int)
    self.assertIs(type(json['traffic']['day']), int)


