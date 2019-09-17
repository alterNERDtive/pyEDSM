class serverError(Exception):
  pass

class notFoundError(Exception):
  def __self__(self, name):
    self.name = name

class systemNotFoundError(notFoundError):
  def str(self):
    return "System \"{}\" not found.".format(self.name)

class commanderNotFoundError(notFoundError):
  def str(self):
    return "Commander \"{}\" not found or has not made his flight logs public.".format(self.name)
