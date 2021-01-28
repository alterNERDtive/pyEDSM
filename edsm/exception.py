class ServerError(Exception):
  """
  Exception used for everything server-related; basically every time the API
  doesn’t reply with a `200 OK`, this is what’s going to be raised.
  """
  def __str__(self):
    return "Server Error fetching {}, params: {}.".format(self.args[0],
        self.args[1])
  pass

class NotFoundError(Exception):
  """
  Base class for all exceptions related to not finding an item in EDSM’s
  database. All specific exceptions handling misses should be derived from this.

  Note: this is raised by the base class for all API endpoints. Implementations
  derived from it should catch it and raise a more specific one.
  """

class SystemNotFoundError(NotFoundError):
  """
  Raised when a system could not be found in the database. Used by the
  `systemApi` and `systemsApi` modules.
  """

  def __str__(self):
    params = self.args[0]
    if 'systemName' in params:
      return "System {} not found.".format(params['systemName'])
    else:
      return "Systems {} not found.".format(params['systemName[]'])

class CommanderNotFoundError(NotFoundError):
  """
  Raised when a commander could not be found in the database (or has their
  profile/logs hidden). Used by the `commanderApi` and `logsApi` modules.
  """

  def __str__(self):
    params = self.args[0]
    return "Commander {} not found or has not made his flight logs public.".format(params['commanderName'])
