import math
import requests
from abc import ABC, abstractmethod

from . import exception

class ApiEndpoint:
  """
  Parent class for all API endpoints.

  :param url: the endpoint’s URL
  """

  url = "https://www.edsm.net/api-"

  @classmethod
  def query(cls, params={}):
    """
    Queries the API endpoint with the given parameters.

    :param params: the parameters to append to the base URL
    """

    response = requests.get(cls.url, params=params)
    if response.status_code != 200:
      raise exception.ServerError(cls.url, params)
    json = response.json()
    if not json:
      raise exception.NotFoundError()
    return json

class Positionable(ABC):
  """
  Abstract class for making sure that an object actually has a documented way to
  get coordinates for positioning.
  """

  @property
  @abstractmethod
  def coords(self):
    pass

  def distanceTo(self, coords, roundTo=2):
    """ Calculates  the distance to another Positionable, or a set of x,y,z
    coordinates.

    :param coords: either another Positionable, or a dict of x,y,z coordinates
    :param roundTo: digits to round the result to (default: 2)
    :raise ValueError: if argument cannot be resolved to a valid coordinates
      dict
    """

    if isinstance(coords, Positionable):
      coords = coords.coords
    for d in (self.coords, coords):
      if not isinstance(d, dict) or not all (k in d for k in ('x', 'y', 'z')):
        raise ValueError("\"{}\" is not a valid coordinates dictionary".format(d))

    return round(math.sqrt((coords['x'] - self.coords['x'])**2
      + (coords['y'] - self.coords['y'])**2
      + (coords['z'] - self.coords['z'])**2 ), roundTo)
