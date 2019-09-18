class ServerError(Exception):
  pass

class NotFoundError(Exception):
  def __self__(self, name):
    self.name = name

class SystemNotFoundError(NotFoundError):
  def str(self):
    return "System \"{}\" not found.".format(self.name)

class CommanderNotFoundError(NotFoundError):
  def str(self):
    return "Commander \"{}\" not found or has not made his flight logs public.".format(self.name)
