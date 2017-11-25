class Spell():
  
  def __init__(self, spell_name):
    """initialises spell with name"""
    self.name = spell_name
    self.description = None
  
  def set_name(self,name):
    """sets name of spell"""
    self.name = name
  
  def get_name(self):
    """returns name of spell"""
    return self.name
  
  def set_description(self, desc):
    """sets description of spell"""
    self.description = desc
  
  def get_description(self):
    """returns description of spell"""
    return self.description
