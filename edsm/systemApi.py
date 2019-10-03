import requests
from . import base
from . import exception
from . import models

class Bodies(base.ApiEndpoint):
  """
  The “system” endpoint of the “systems” API

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

    json = cls.query("systemName=" + systemName)
    return json

  @classmethod
  def getBodiesById(cls, systemId):
    """
    Requests information about the bodies in a system.

    :param systemId: ID of the system in question
    """

    json = cls.query("systemId=" + str(systemId))
    return json
