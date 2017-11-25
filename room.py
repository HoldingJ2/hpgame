class Room():

  def __init__(self, room_name):
    """initialises room with name"""
    self.name = room_name
    self.description = "*room desc*"
    self.linked_rooms = {}
    self.item = None
    self.character = None
    self.problem = None
    self.spellbook = None
    
  def set_description(self, room_description):
    """sets room description"""
    self.description = room_description
    
  def get_description(self):
    """returns room description"""
    return self.description
    
  def set_name(self, room_name):
    """sets the room name"""
    self.name = room_name
    
  def get_name(self):
    """returns room name"""
    return self.name
  
  def set_character(self, character):
    """sets character to be in the room"""
    self.character = character
  
  def get_character(self):
    """returns character in the room"""
    return self.character
  
  def set_item(self, item_name):
    """sets item to be in the room"""
    self.item = item_name
  
  def get_item(self):
    """returns item in the room"""
    return self.item
  
  def get_problem(self):
    """returns problem in the room"""
    return self.problem
  
  def set_problem(self, problem):
    """sets problem for the room"""
    self.problem = problem
  
  def set_spellbook(self, spellbook):
    """sets spellbook to be in the room"""
    self.spellbook = spellbook
  
  def get_spellbook(self):
    """returns spellbook in the room"""
    return self.spellbook
  
  def describe(self):
    """describes room"""
    print( self.description)
    
  def link_room(self, room_to_link, direction):
    """links room to other rooms by direction"""
    self.linked_rooms[direction] = room_to_link
    
  def get_details(self):
    """get details of the room: name, description and linked rooms"""
    print(self.name)
    print( "---------")
    print(self.description)
    for direction in self.linked_rooms:
        room = self.linked_rooms[direction]
        print( "The " + room.get_name() + " is " + direction)
        
  
  def move(self, direction):
    """move player to room in stated direction"""
    if direction in self.linked_rooms:
        return self.linked_rooms[direction]
    else:
        print("You can't go that way, idiot...")
        return self
  
  
