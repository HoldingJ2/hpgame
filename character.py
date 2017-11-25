class Character():

    def __init__(self, char_name, char_description):
        """initialises a character with name and description"""
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.item = None
        self.completed_text = None
        self.conversation2 = None

    def describe(self):
        """Describes the character"""
        print( self.name + " is here!" )
        print( self.description )

    def set_conversation(self, conversation):
        """sets the conversation for the character"""
        self.conversation = conversation
    
    def set_possession(self, item):
        """sets the item the character possesses"""
        self.item = item

    def talk(self):
        """prints the characters conversation"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    
    def get_completed_text(self):
        """returns their text that appears after completion of their request"""
        return self.completed_text
  
    def set_completed_text(self, text):
        """sets the text that will appear after completion of their request"""
        self.completed_text = text
    
    def get_conversation2(self):
        """returns their alternative conversation"""
        return self.conversation2
    
    def set_conversation2(self,text):
        """sets their alternative conversation"""
        self.conversation2 = text

    def fight(self, combat_item, current_room):
        """starts fight sequence"""
        print(self.name + " doesn't want to fight with you")
        return True
        
    def steal(self):
        """starts steal sequence"""
        print( self.name + " is friendly, you cannot steal from friends")        
      
class Enemy(Character):
  
  def __init__(self, char_name, char_description):
      """initialises enemy with name and description"""
      super().__init__(char_name, char_description)
      self.weakness = None
      enemies_defeated = 0
  
  
  def set_weakness(self, weakness):
      """sets the enemy's weakness"""
      self.weakness = weakness
  
  def fight(self, combat_item, current_room):
      """starts fight sequence for enemy"""
      if combat_item == self.weakness:
          print( "You scared off " + self.name + " with the " + combat_item)
          current_room.set_character(None)
          Enemy.enemies_defeated += 1
          return True
      else:
          print( "Oh no! That didn't work, " + self.name + " defeated you!")
          return False
  
  def steal(self):
      """starts steal sequence for enemy"""
      if self.item is not None:
          print("You stole a " + self.item )
      else:
          print(self.name + " had nothing on them")
  
  
class Friend(Character):
  
  def __init__(self, char_name, char_description):
      """initialises friend character with name and description"""
      super().__init__(char_name, char_description)
      self.request = None
    
  
  def set_request(self,item):
      """sets character request item"""
      self.item = item
  
  def get_request(self):
      """returns character request item"""
      return self.request
  
  def give(self, item):
      """give a character an item"""
      if item == self.item.name:
          print(self.completed_text)
          self.conversation = self.conversation2
      else:
          print(self.name + " doesn't want that")
      

