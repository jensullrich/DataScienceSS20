"""
Class Listkeeper strores named lists
"""
class ListKeeper:
  """
  Dictionary that stores the named lists
  """
  __named_lists_dict = dict()

  """
  Constructor, initializes with example list
  """
  def __init__(self):
    self.__named_lists_dict['example'] = [1,2,3,4,5]


  """
  returns all list names 
  """
  def show(self):
    return self.__named_lists_dict.keys()


  """
  adds a new list
  """
  def add(self, name, new_list):
    self.__named_lists_dict[name] = new_list


  """
  deletes given list
  """
  def delete(self, name):
    self.__named_lists_dict.pop(name)


  """
  sorts given list
  """
  def sort(self, name):
    self.__named_lists_dict[name].sort()


  """
  appends list to existing entry
  """
  def append(self, name, appList):
    self.__named_lists_dict[name].extend(appList)


  """
  overrides [] operator to get lists
  """
  def __getitem__(self, key):
    return self.__named_lists_dict[key]

