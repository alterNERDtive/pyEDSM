import requests
from . import base
from . import exception
from . import models

class System(base.ApiEndpoint):
  """
  The “system” endpoint of the “systems” API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "v1/system"

  @classmethod
  def query(cls, params):
    try:
      json = super().query(params)
    except exception.NotFoundError:
      raise exception.SystemNotFoundError(params)
    return json

  @classmethod
  def getSystem(cls, systemName):
    """
    Requests the entire range of information for a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName,
          'showId': 1,
          'showCoordinates': 1,
          'showPermit': 1,
          'showInformation': 1,
          'showPrimaryStar': 1})
    return json

  @classmethod
  def getIds(cls, systemName):
    """
    Requests the id and id64 for a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName,
          'showId': 1})
    return json

  @classmethod
  def getCoordinates(cls, systemName):
    """
    Requests coordinates for a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName,
          'showCoordinates': 1})
    return json

  @classmethod
  def getPermit(cls, systemName):
    """
    Requests permit information for a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName,
          'showPermit': 1})
    return json

  @classmethod
  def getInformation(cls, systemName):
    """
    Requests faction information for a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName,
          'showInformation': 1})
    return json

  @classmethod
  def getPrimaryStar(cls, systemName):
    """
    Requests primary star information for a system.

    :param systemName: name of the system in question
    """

    json = cls.query({'systemName': systemName,
          'showPrimaryStar': 1})
    return json

class Systems(base.ApiEndpoint):
  """
  The “systems” endpoint of the “systems” API

  :attribute url: the API endpoint URL
  """

  url = base.ApiEndpoint.url + "v1/systems"

  @classmethod
  def query(cls, params):
    try:
      json = super().query(params)
    except exception.NotFoundError:
      raise exception.SystemNotFoundError(params)
    return json

  @classmethod
  def getSystems(cls, *systemName):
    """
    Requests the entire range of information for a range of systems. Will
    silently ignore systems that cannot be found in the database.

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    parameters = {'showId': 1,
        'showCoordinates': 1,
        'showPermit': 1,
        'showInformation': 1,
        'showPrimaryStar': 1}

    if len(systemName) == 1:
      parameters['systemName'] = systemName[0]
    else:
      parameters['systemName[]'] = list(systemName)

    return cls.query(parameters)

  @classmethod
  def getIds(cls, *systemName):
    """
    Requests the id and id64 for a range of systems. Will silently ignore
    systems that cannot be found in the database.

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    parameters = {'showId': 1}

    if len(systemName) == 1:
      parameters['systemName'] = systemName[0]
    else:
      parameters['systemName[]'] = list(systemName)

    return cls.query(parameters)

  @classmethod
  def getCoordinates(cls, *systemName):
    """
    Requests the coordinates for a range of systems. Will silently ignore
    systems that cannot be found in the database.

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    parameters = {'showCoordinates': 1}

    if len(systemName) == 1:
      parameters['systemName'] = systemName[0]
    else:
      parameters['systemName[]'] = list(systemName)

    return cls.query(parameters)

  @classmethod
  def getPermit(cls, *systemName):
    """
    Requests permit information for a range of systems. Will silently ignore
    systems that cannot be found in the database.

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    parameters = {'showPermit': 1}

    if len(systemName) == 1:
      parameters['systemName'] = systemName[0]
    else:
      parameters['systemName[]'] = list(systemName)

    return cls.query(parameters)

  @classmethod
  def getInformation(cls, *systemName):
    """
    Requests faction information for a range of systems. Will silently ignore
    systems that cannot be found in the database.

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    parameters = {'showInformation': 1}

    if len(systemName) == 1:
      parameters['systemName'] = systemName[0]
    else:
      parameters['systemName[]'] = list(systemName)

    return cls.query(parameters)

  @classmethod
  def getPrimaryStar(cls, *systemName):
    """
    Requests primary star information for a range of systems. Will silently
    ignore systems that cannot be found in the database.

    :param *systemName: either a single string to find systems names beginning
      with it, or multiple full system names to query simultaneously
    """

    parameters = {'showPrimaryStar': 1}

    if len(systemName) == 1:
      parameters['systemName'] = systemName[0]
    else:
      parameters['systemName[]'] = list(systemName)

    return cls.query(parameters)
