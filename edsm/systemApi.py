import requests
from . import base
from . import exception
from . import models

class Bodies(base.ApiEndpoint):
  """
  The “bodies” endpoint of the “system” API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "system-v1/bodies"

  @classmethod
  def query(cls, params):
    try:
      json = super().query(params)
    except exception.NotFoundError:
      raise exception.SystemNotFoundError(params)
    return json

  @classmethod
  def getBodies(cls, systemName):
    """
    Requests information about the bodies in a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName})
    return json

  @classmethod
  def getBodiesById(cls, systemId):
    """
    Requests information about the bodies in a system.

    :param systemId: ID of the system in question
    """

    json = cls.query({'systemId': str(systemId)})
    return json

class Traffic(base.ApiEndpoint):
  """
  The "traffic" endpoint of the "system" API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "system-v1/traffic"

  @classmethod
  def query(cls, params):
    try:
      json = super().query(params)
    except exception.NotFoundError:
      raise exception.SystemNotFoundError(params)
    return json

  @classmethod
  def getTraffic(cls, systemName):
    """
    Requests information about traffic in a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName})
    return json

  @classmethod
  def getTrafficById(cls, systemId):
    """
    Requests information about traffic in a system.

    :param systemName: ID of the system in question
    """

    json = cls.query({'systemId' : str(systemId)})
    return json