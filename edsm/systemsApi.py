import requests
from . import base
from . import exception
from . import models

class System(base.ApiEndpoint):
  """
  The “system” endpoint of the “systems” API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "v1/system"

  @classmethod
  def getSystem(cls, systemName):
    """
    Requests the entire range of information for a system.

    :param systemName: name of the system in question
    """

    try:
      json = cls.query("systemName=" + systemName
        + "&showId=1"
        + "&showCoordinates=1"
        + "&showPermit=1"
        + "&showInformation=1"
        + "&showPrimaryStar=1")
    except exception.notFoundError:
      raise exception.systemNotFoundError(systemName)
    return json

  @classmethod
  def getIds(cls, systemName):
    return None

  @classmethod
  def getCoordinates(cls, systemName):
    return None

  @classmethod
  def getPermit(cls, systemName):
    return None

  @classmethod
  def getInformation(cls, systemName):
    return None

  @classmethod
  def getPrimaryStar(cls, systemName):
    return None
