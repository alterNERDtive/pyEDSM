import requests
from . import exception

class ApiEndpoint:
  """
  Parent class for all API endpoints.

  :param url: the endpoint’s URL
  """
  url = "https://www.edsm.net/api-"

  def query(self, params):
    """
    Queries the API endpoint with the given parameters.

    :param params: the parameters to append to the base URL
    """
    response = requests.get(self.url + "?" + params)
    if response.status_code != 200:
      raise exception.serverError()
    json = response.json()
    if not json:
      raise exception.notFoundError()
    return json

class System:
  """
  FIXXME
  """
  def __init__(self, name=""):
    systemName = name
    id = None
    id64 = None
    coords = None
    information = None
    primaryStar = None

  @property
  def name(self):
    return self.systemName

  @property
  def ids(self):
    return (self.id, self.id64)

class Commander:
  """
  FIXXME
  """
  pass
