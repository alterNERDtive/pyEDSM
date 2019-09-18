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
  def getCoordinates(cls, systemName):
    """
    Requests coordinates for a system.

    :param systemName: name of the system in question
    """

    try:
      json = cls.query("systemName=" + systemName
          + "&showCoordinates=1")
    except exception.notFoundError:
      raise exception.systemNotFoundError(systemName)
    return json

  @classmethod
  def getPermit(cls, systemName):
    """
    Requests permit information for a system.

    :param systemName: name of the system in question
    """

    try:
      json = cls.query("systemName=" + systemName
          + "&showPermit=1")
    except exception.notFoundError:
      raise exception.systemNotFoundError(systemName)
    return json

  @classmethod
  def getInformation(cls, systemName):
    """
    Requests faction information for a system.

    :param systemName: name of the system in question
    """

    try:
      json = cls.query("systemName=" + systemName
        + "&showInformation=1")
    except exception.notFoundError:
      raise exception.systemNotFoundError(systemName)
    return json

  @classmethod
  def getPrimaryStar(cls, systemName):
    """
    Requests primary star information for a system.

    :param systemName: name of the system in question
    """

    try:
      json = cls.query("systemName=" + systemName
          + "&showPrimaryStar=1")
    except exception.notFoundError:
      raise exception.systemNotFoundError(systemName)
    return json
