import unittest
from datetime import datetime

from . import statusApi

class StatusTest(unittest.TestCase):

  def test_Status(self):
    json = statusApi.Status.getServerStatus()

    # lastUpdate should be a time string
    fmt = '%Y-%m-%d %H:%M:%S'
    try:
      datetime.strptime(json['lastUpdate'], fmt)
    except ValueError:
      self.fail("`lastUpdate` is not a time string in the expected format of"
          + "`{}`. value: `{}`", fmt , json['lastUpdate'])

    self.assertIn(json['type'], ("success", "warning", "danger"))

    # this needs to be updated when I know more status messages / codes; right
    # now I only know of “Upgrading”/1 and “OK”/2
    self.assertIn(json['message'], ("OK", "Upgrading"))
    self.assertIn(json['status'], (1, 2))
