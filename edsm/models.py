from . import systemsApi

class System:
  """
  FIXXME
  """
  def __init__(self, name=""):
    json = systemsApi.System.getSystem(name)
    self.systemName = json['name']
    self.id = json['id']
    if json['id64']:
      self.id64 = json['id64']
    self.coords = json['coords']
    self.requirePermit = json['requirePermit']
    if self.requirePermit:
      self.permitName = json['permitName']
    self.information = json['information']
    self.primaryStar = json['primaryStar']

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
