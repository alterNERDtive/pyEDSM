import datetime
from . import systemsApi, statusApi

class Commander:
  """
  Model for a CMDR. Uses both the “commander” and “logs” endpoints for different
  things.

  FIXXME
  """
  pass

class Status:
  """
  Model for the “status” API endpoint. Tells you the game servers’ current
  status. it will automatically cache values for 2 minutes; given EDSM only
  updates their status endpoint from Frontier’s servers roughly every
  30 minutes, that should be more than frequent enough.

  :attribute lastUpdate: the time EDSM last updated their status at (datetime)
  :attribute type: status type (string); should be “success”, “warning” or
  “danger”
  :attribute message: status message (string)
  :attribute status: status code (int)
  """
  def __init__(self):
    self.__lastUpdate = None
    self.__type = None
    self.__message = None
    self.__status = None
    self.cachedAt = None

  @property
  def lastUpdate(self):
    self.__update()
    return self.__lastUpdate

  @property
  def type(self):
    self.__update()
    return self.__type

  @property
  def message(self):
    self.__update()
    return self.__message

  @property
  def status(self):
    self.__update()
    return self.__status

  def forceUpdate(self):
    """
    Forces an update from the EDSM Api.
    """
    json = statusApi.Status.getServerStatus()
    self.__lastUpdate = datetime.datetime.strptime(json['lastUpdate'], '%Y-%m-%d %H:%M:%S')
    self.__type = json['type']
    self.__message = json['message']
    self.__status = json['status']
    self.cachedAt = datetime.datetime.now()

  def __update(self):
    if self.cachedAt == None or (datetime.datetime.now() - self.cachedAt > datetime.timedelta(minutes=2)):
      self.forceUpdate()

class System:
  """
  Model for a star system. Uses both the “system” and “systems” API endpoints.

  :attribute name: the system’s name (string)
  :attribute id: the system’s id (int)
  :attribute id64: the system’s id64 (int, may be None)
  :attribute coords: the systems x, y and z coordinates (dict)
  :attribute requirePermit: system requires a permit to access (bool)
  :attribute permitName: the name of the required permit (string, may be None)
  :attribute information: (faction) information (dict, may be empty)
  :attribute primaryStar: information about the primary star (dict)
  """
  def __init__(self, name):
    json = systemsApi.System.getSystem(name)
    self.systemName = json['name']
    self.id = json['id']
    self.id64 = None
    if json['id64']:
      self.id64 = json['id64']
    self.coords = json['coords']
    self.requirePermit = json['requirePermit']
    self.permitName = None
    if self.requirePermit:
      self.permitName = json['permitName']
    self.information = json['information']
    self.primaryStar = json['primaryStar']

  @property
  def name(self):
    return self.systemName

  @property
  def ids(self):
    return {id:self.id, id64:self.id64}
