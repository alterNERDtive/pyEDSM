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
