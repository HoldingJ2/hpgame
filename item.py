class Item():
  
  def __init__(self, item_name):
    """initialises item with name"""
    
    self.name = item_name
    self.description = ""
    
  def set_name(self, item_name):
    """sets the name of an item"""
    self.name = item_name
  
  def set_desc(self, item_desc):
    """sets the description of an item"""
    self.description = item_desc
  
  def take(self, current_room):
    """take an item"""
    self.get_details()
    current_room.item = None
      
  def describe(self):
    """describes the item"""
    print( "There is a " + self.name + " in here")
    print( self.description)
    
  def get_details(self):
    print("You found a " + self.name)
    print("Description: " + self.description)
    


  
