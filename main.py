from rpg import Room, Item, Friend, Enemy, Problem, Spell, Spellbook


#ROOMS

great_hall = Room("Great Hall")
entrance_hall = Room("Entrance Hall")
main_hallway = Room("Main Hallway")
library = Room("Library")
gryff_com = Room("Gryffindor Common Room")
stairs = Room("Main Staircase")
ff_corridor = Room("First Floor Corridor")
courtyard = Room("Courtyard")
bridge = Room("Bridge")
garden = Room("Garden")
greenhouse = Room("Greenhouse")
hagrid_hut = Room("Hagrid's Hut")

#ROOM LINKS

great_hall.link_room(entrance_hall, "south")

entrance_hall.link_room(great_hall, "north")
entrance_hall.link_room(main_hallway, "south")

main_hallway.link_room(entrance_hall, "north")
main_hallway.link_room(library, "west")
main_hallway.link_room(stairs, "east")
main_hallway.link_room(courtyard, "south")

library.link_room(main_hallway, "east")

stairs.link_room(main_hallway, "west")
stairs.link_room(gryff_com, "north")
stairs.link_room(ff_corridor, "south")

ff_corridor.link_room(stairs, "north")

gryff_com.link_room(stairs,"south")

courtyard.link_room(main_hallway, "north")
courtyard.link_room(bridge, "south")

bridge.link_room(courtyard, "north")
bridge.link_room(garden, "south")

garden.link_room(bridge, "north")
garden.link_room(greenhouse, "west")
garden.link_room(hagrid_hut, "east")

greenhouse.link_room(garden, "east")

hagrid_hut.link_room(garden, "west")

#CHARACTERS

dumble = Friend("Dumbledore", "A grand wizard")
herm = Friend("Hermione", "A gryffindor girl with big bushy hair")
neville = Friend("Neville", "A gryffindor boy with big ears")

#ITEMS

sherbet_lemon = Item("Sherbet Lemon")
rune_book = Item("rune book")
rememberall = Item("Rememberall")


dumble.set_request(sherbet_lemon)
dumble.set_conversation("I'd really like a sherbet lemon")

herm.set_request(rune_book)
herm.set_conversation("Have you seen my rune book anywhere?")
herm.set_completed_text("Thank you so much! Now I can finally finish my homework")
herm.set_conversation2("Can't talk sorry, this work's due in next week!")

bookcase = Problem("There's a fallen bookcase which looks too heavy to lift")

great_hall.set_character(dumble)
gryff_com.set_character(herm)
library.set_problem(bookcase)

leviosa = Spell("wl")
leviosa_book = Spellbook("Charms: First Year")
leviosa_book.set_spell(leviosa)
great_hall.set_spellbook(leviosa_book)

bookcase.set_solution(leviosa.name)
bookcase.set_resolution("You used your spell to lift up the bookcase")
bookcase.set_item(rune_book)
bookcase.set_end_desc("There's a pile of books on the floor where the bookcase was.")

backpack = []

my_spells = []

current_room = great_hall      
current_item = None

run = True

while run == True:		
    print("\n")         
    current_room.get_details()
    print("")
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    problem = current_room.get_problem()
    book = current_room.get_spellbook()
    
    
    if inhabitant is not None:
      inhabitant.describe()
    
    if problem is not None:
      problem.describe()
      
    
   
    
    command = input("> ")    
    
    
    if command in ["north", "south", "east", "west"]:
      current_room = current_room.move(command)
      
    elif command == "talk":
      if inhabitant is not None:
        inhabitant.talk()
      else:
        print("There is nobody to talk to")
        
    elif command == "fight":
      if inhabitant is not None:
        print("What will you fight with?")
        fight_with = input()
        if fight_with in backpack:
          run = inhabitant.fight(fight_with, current_room)
        else:
          print("You don't have that")
      else:
        print("There is nobody to fight")
        
    elif command == "steal":
      if inhabitant is not None:
        inhabitant.steal()
      else:
        print("There is nobody to steal from")
        
    elif command == "search":
      if item is not None:
        item.take(current_room)
        backpack.append(item.name)
      elif book is not None:
        book.take(current_room)
        my_spells.append(book.spell.name)
      else:
        print("You didn't find anything")
    
    elif command == "spell":
      if not my_spells:
        print("You don't know any spells")
      else:
        if problem is not None:
          print("Which spell will you use?")
          spell = input()
          if spell in my_spells:
            problem.cast_spell(spell, current_room)
          else:
            print("You don't know that spell")
        else:
          print("There is nothing to cast a spell on")
    
    elif command == "give":
      if inhabitant is not None:
        if not backpack:
          print("You have nothing to give them")
        else:
          print("What would you like to give them?")
          item = input()
          if item in backpack:
            inhabitant.give(item)
          else:
            print("You don't have that")
      else:
        print("There is nobody to give anything to")
    
    elif command == "i":
      print("backpack:")
      print( backpack)
    
    elif command == "s":
      print( "My spells:")
      print( my_spells)
    
    else:
      print("That is not an option")
    
    if Enemy.enemies_defeated == 2:
      print("You defeated all of the enemies!")
      run = False
      

print("The End")
