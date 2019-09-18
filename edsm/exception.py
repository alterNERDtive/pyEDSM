class ServerError(Exception):
  pass

class NotFoundError(Exception):
  def __self__(self, name):
    self.name = name

class SystemNotFoundError(NotFoundError):
  def __str__(self):
    return "System not found. Params: {}".format(self.args)

class CommanderNotFoundError(NotFoundError):
  def __str__(self):
    return "Commander not found or has not made his flight logs public. Params: {}".format(self.args)
