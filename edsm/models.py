import datetime
from natsort import natsorted
from operator import attrgetter

from . import logsApi, systemApi, systemsApi, statusApi
from .base import Positionable

class Commander(Positionable):
  """
  Model for a CMDR. Uses both the “commander” and “logs” endpoints for different
  things.

  :attribute name: the commander’s name (string)
  :attribute apiKey: the commander’s EDSM API key (string)
  :attribute currentPosition: x, y and z coordinates fo the commander’s current
  position (dict)
  :attribute currentSystem: the system the commander is currently in (string)
  :attribute lastActivity: date and time of the commander’s last uploaded
  activity (string, format: YYYY-MM-DD HH-MM-SS)
  :attribute profileUrl: the commander’s profile on EDSM (string)
  """

  def __init__(self, name, apiKey=""):
    self.name = name
    self.apiKey = apiKey
    self.__profileUrl__ = None

  @property
  def currentPosition(self):
    json = logsApi.Position.getPosition(self.name, self.apiKey)
    self.__profileUrl__ = json['url']
    return json['coordinates']
  @property
  def coords(self):
    return self.currentPosition

  @property
  def currentSystem(self):
    json = logsApi.Position.getSystem(self.name, self.apiKey)
    self.__profileUrl__ = json['url']
    return json['system']

  @property
  def lastActivity(self):
    json = logsApi.Position.getSystem(self.name, self.apiKey)
    self.__profileUrl__ = json['url']
    return json['dateLastActivity']

  @property
  def profileUrl(self):
    if self.__profileUrl__ == None:
      json = logsApi.Position.getSystem(self.name, self.apiKey)
      self.__profileUrl__ = json['url']
    return self.__profileUrl__

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

class System(Positionable):
  """
  Model for a star system. Uses both the “system” and “systems” API endpoints.

  :attribute name: the system’s name (string)
  :attribute id: the system’s id (int)
  :attribute id64: the system’s id64 (int, may be None)
  :attribute coords: the systems x, y and z coordinates (dict)
  :attribute requirePermit: system requires a permit to access (bool)
  :attribute permitName: the name of the required permit (string, may be None)
  :attribute information: (faction) information (dict, may be empty, cached for
  2h)
  :attribute primaryStar: information about the primary star (dict)
  :attribute bodyCount: amount of bodies in the system (int)

  :method fetch: updates all attributes in one go
  """
  def __init__(self, name, coords=None, id=None, id64=None):
    # FIXXME: this probably needs some way to make sure the system exists. Or
    # not. Not sure yet how I want to handle wrong system names.
    self.name = name
    self.__coords = coords
    self.__id = id
    self.__id64 = id64
    self.__requirePermit = None
    self.__permitName = None
    self.__information = {'cachedAt': None}
    self.__primaryStar = None

  @property
  def name(self):
    return self.__systemName
  @name.setter
  def name(self, name):
    self.__systemName = name

  @property
  def coords(self):
    if self.__coords == None:
      self.__coords = systemsApi.System.getCoordinates(self.name)['coords']
    return self.__coords

  @property
  def requirePermit(self):
    if self.__requirePermit == None:
      self.__updatePermit()
    return self.__requirePermit
  @property
  def permitName(self):
    if self.__requirePermit == None:
      self.__updatePermit()
    return self.__permitName
  def __updatePermit(self):
    permitInfo = systemsApi.System.getPermit(self.name)
    self.__requirePermit = permitInfo['requirePermit']
    if self.__requirePermit:
      self.__permitName = permitInfo['permitName']

  @property
  def id(self):
    if self.__id == None:
      self.__updateIDs()
    return self.__id
  @property
  def id64(self):
    if self.__id64 == None:
      self.__updateIDs()
    return self.__id64
  @property
  def ids(self):
    return {id:self.id, id64:self.id64}
  def __updateIDs(self):
    ids = systemsApi.System.getIds(self.name)
    self.__id = ids['id']
    if ids['id64']:
      self.__id64 = ids['id64']

  @property
  def information(self):
    if self.__information['cachedAt'] == None or (datetime.datetime.now()
    - self.__information['cachedAt'] > datetime.timedelta(hours=2)):
      self.__information = systemsApi.System.getInformation(self.name)['information']
      self.__information['cachedAt'] = datetime.datetime.now()
    return self.__information

  @property
  def primaryStar(self):
    if self.__primaryStar == None:
      self.__primaryStar = systemsApi.System.getPrimaryStar(self.name)['primaryStar']
    return self.__primaryStar

  @property
  def bodyCount(self):
    """
    This is not going to be cached, since the primary use will probably be in
    exploring; hence the amount of bodies EDSM knows about might change on the
    spot.
    """
    return len(systemApi.Bodies.getBodies(self.name)['bodies'])

  def fetch(self):
    """
    Fetches all information about the system from the API (again). Useful if you
    need everything anyway, it’s faster to fetch it in one single call.
    """
    json = systemsApi.System.getSystem(self.name)
    self.name = json['name']
    self.__id = json['id']
    self.__id64 = None
    if json['id64']:
      self.__id64 = json['id64']
    self.__coords = json['coords']
    self.__requirePermit = json['requirePermit']
    self.__permitName = None
    if self.requirePermit:
      self.__permitName = json['permitName']
    self.__information = json['information']
    self.__information['cachedAt'] = datetime.datetime.now()
    self.__primaryStar = json['primaryStar']

    return self

  @classmethod
  def getSystems(self, *systemName):
    """
    Searches EDSM for a range of systems. Unknown systems will be silently
    ignored (unless none can be found at all).

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    json = systemsApi.Systems.getSystems(*systemName)

    systems = []
    for system in json:
      systems.append(System(system['name'], system['coords'], system['id'],
        system['id64']))

    return natsorted(systems, key=attrgetter("name"))

  # comparison operators!

  def __eq__(self, other):
    if (self.id == other.id and self.id64 == other.id64):
      return True
    else:
      return False

  def __lt__(self, other):
    return natsorted([self.name, other.name])[0] == self.name

  def __gt__(self, other):
    return natsorted([self.name, other.name])[1] == self.name
