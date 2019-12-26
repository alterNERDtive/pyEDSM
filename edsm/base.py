import requests
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
