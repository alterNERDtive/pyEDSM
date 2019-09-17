import requests
from . import base
from . import exception

class System(base.ApiEndpoint):
  """
  The “system” endpoint of the “systems” API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "v1/system"

  def getSystem(self, systemName):
    """
    Requests the entire range of information for a system

    :param systemName: name of the system in question
    """

    try:
      json = self.query("systemName=" + systemName
        + "&showId=1"
        + "&showCoordinates=1"
        + "&showPermit=1"
        + "&showInformation=1"
        + "&showPrimaryStar=1")
    except exception.notFoundError:
      raise exception.systemNotFoundError(systemName)

    system = base.System()
    system.systemName = json['name']
    system.id = json['id']
    system.id64 = json['id64']
    system.coords = json['coords']
    system.requirePermit = json['requirePermit']
    if system.requirePermit:
      system.permitName = json['permitName']
    system.information = json['information']
    system.primaryStar = json['primaryStar']
    return system

  def getIds(self, systemName):
    return None

  def getCoordinates(self, systemName):
    return None

  def getInformation(self, systemName):
    return None

  def getPrimaryStar(self, systemName):
    return None
