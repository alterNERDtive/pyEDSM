import datetime
from . import systemsApi, statusApi

class Commander:
  """
  FIXXME
  """
  pass

class Status:
  """
  FIXXME
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
  FIXXME
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
