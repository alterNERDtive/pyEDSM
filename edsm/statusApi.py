import requests
from . import base, exception

class Status(base.ApiEndpoint):
  """
  The only endpoint of the “status” API. It is used to check the game server
  status.

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "status-v1/elite-server"

  @classmethod
  def getServerStatus(cls):
    return cls.query()
