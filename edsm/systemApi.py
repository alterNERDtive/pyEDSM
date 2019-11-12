import requests
import urllib.parse
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

    json = cls.query("systemName=" + urllib.parse.quote(systemName, safe=''))
    return json

  @classmethod
  def getBodiesById(cls, systemId):
    """
    Requests information about the bodies in a system.

    :param systemId: ID of the system in question
    """

    json = cls.query("systemId=" + str(systemId))
    return json
