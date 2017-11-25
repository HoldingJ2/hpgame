class Spellbook():
  
  def __init__(self,book_name):
    """initialises spellbook with book name"""
    self.name = book_name
    self.spell = None
  
  def set_spell(self,spell):
    """sets spell to be learned from the spellbook"""
    self.spell = spell
  
  def get_spell(self):
    """returns the spell learned from the spellbook"""
    return self.spell
  
  def get_details(self):
    """gets the details of the book: name"""
    print("You found a spellbook entitled: " + self.name)
  
  def take(self, current_room):
    """take spellbook from the room"""
    self.get_details()
    current_room.spellbook = None
    print("You learned a new spell: " + self.spell.name)
  
