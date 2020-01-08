import requests
from . import base
from . import exception
from . import models

class Position(base.ApiEndpoint):
  """
  The “get-position” endpoint of the “logs” API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "logs-v1/get-position"

  @classmethod
  def query(cls, params):
    try:
      json = super().query(params)
    except exception.NotFoundError:
      raise exception.CommanderNotFoundError(params)

    if json['msgnum'] == 203:
      raise exception.CommanderNotFoundError(params)
    return json

  @classmethod
  def getPosition(cls, commanderName, apiKey=""):
    """
    Requests the last known position of a given commander.

    This will only work if they have set their profile and logs or flight map to
    public or if you supply the commanders’s API key.

    :param commanderName: name of the commander in question
    :param apiKey: the commander’s EDSM API key
    """

    json = cls.query({'commanderName': commanderName,
          'apiKey': apiKey,
          'showId': 1,
          'showCoordinates': 1})
    return json

  @classmethod
  def getSystem(cls, commanderName, apiKey=""):
    """
    Requests the last known system of a given commander.

    This will only work if they have set their profile and logs or flight map to
    public or if you supply the commanders’s API key.

    :param commanderName: name of the commander in question
    :param apiKey: the commander’s EDSM API key
    """

    json = cls.query({'commanderName': commanderName,
            'showId': 1,
            'apiKey': apiKey})
    return json
