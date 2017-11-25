class Problem():
  
  def __init__(self, desc):
    """initialises problem with description"""
    self.description = desc
    self.resolution = None
    self.solution = None
    self.item = None
    self.end_description = None
  
  def set_description(self, desc):
    """sets the description of the problem"""
    self.description = desc
  
  def get_description(self):
    """returns the description"""
    return self.description
  
  def set_resolution(self, text):
    """sets the text which appears when the problem is resolved"""
    self.resolution = text
  
  def get_resolution(self):
    """returns the text to appear when the problem is resolved"""
    return self.resolution
  
  def get_solution(self):
    """returns the solution to the problem"""
    return self.solution

  def set_solution(self, sol):
    """sets the solution to the problem"""
    self.solution = sol
  
  def set_item(self, item):
    """sets the item available after resolution of the problem"""
    self.item = item
  
  def get_item(self):
    """returns the item available after the resolution of the problem"""
    return self.item
  
  def get_end_desc(self):
    """returns the description after it has been resolved"""
    return self.end_description
  
  def set_end_desc(self, desc):
    """sets the description of the problem for after it has been solved"""
    self.end_description = desc
  
  def describe(self):
    """describes problem"""
    print(self.description)
  
  def cast_spell(self, spell, current_room):
    """asks player to choose a spell to combat the problem"""
    if spell == self.solution:
      print( self.resolution)
      current_room.set_problem(None)
      current_room.item = self.item
      current_room.set_description(self.end_description)
    else:
      print("That didn't work")
      
    
