import unittest
from . import exception
from .logsApi import Position

class PositionTest(unittest.TestCase):

  def test_getPosition_public_IHFYD(self):
    json = Position.getPosition("IHaveFuelYouDont")
    self.assertEqual(100, json['msgnum'])
    self.assertEqual("OK", json['msg'])

    # position
    coords = json['coordinates']
    self.assertEqual(25.40625, coords['x'])
    self.assertEqual(-31.0625, coords['y'])
    self.assertEqual(41.625, coords['z'])

    # profile url
    self.assertEqual("https://www.edsm.net/en/user/profile/id/86423/cmdr/IHaveFuelYouDont", json['url'])

    #last activity
    self.assertIsNotNone(json['dateLastActivity'])

  def test_getPosition_notFound(self):
    self.assertRaises(exception.CommanderNotFoundError,
      Position.getPosition, "efgsias.oshsudifaesuitrna")

  def test_getSystem_public_IHFYD(self):
    json = Position.getSystem("IHaveFuelYouDont")
    self.assertEqual(100, json['msgnum'])
    self.assertEqual("OK", json['msg'])

    # system
    self.assertEqual("Dromi", json['system'])
    self.assertEqual(38324688, json['systemId'])
    self.assertEqual(1213084977515, json['systemId64'])

    # profile url
    self.assertEqual("https://www.edsm.net/en/user/profile/id/86423/cmdr/IHaveFuelYouDont", json['url'])

    #last activity
    self.assertIsNotNone(json['dateLastActivity'])

  def test_getSystem_notFound(self):
    self.assertRaises(exception.CommanderNotFoundError,
        Position.getSystem, "efgsias.oshsudifaesuitrna")
