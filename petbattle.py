#WoW Pet Battle game!
#test change
class Pet:
  def __init__(self, name, health, attack, type):
    self.name = name
    self.health = health
    self.attack = attack 
    self.type = type
    self.knocked_out = False

  def __repr__(self):
    return '{name} is a {type} type, with {attack} attack and {health} health.'.format(name = self.name, type = self.type, attack = self.attack, health = self.health)

  def knocked_out(self):
    self.knocked_out = True
    if self.health != 0:
        self.health = 0
    print('{name} was knocked out!'.format(name = self.name))

  def revive(self):
    self.knocked_out = False
    if self.health == 0:
        self.health = 1
    print('{name} was revived!'.format(name = self.name))

  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
       self.health = 0
       self.knocked_out()
    else:
      print('{name} now has {health} health.'.format(name = self.name, health = self.health))

  def gain_health(self, amount):
    if self.health == 0:
        self.revive()
    self.health += amount
    print('{name} has been healed and now has {health} health.'.format(name = self.name, health = self.health))
  
  def attacking(self, other_pet):
    if self.knocked_out:
      print('{name} cannot attack, they are knocked out!'.format(name = self.name))
    

    if (self.type == 'Fire' and other_pet.type == 'Water') or (self.type == 'Nature' and other_pet.type == 'Fire') or (self.type == 'Water' and other_pet.type == 'Nature') or (self.type == 'Flying' and other_pet.type == 'Electric') or (self.type == 'Electric' and other_pet.type == 'Water'):
      print('{myname} attacked {otherpet} for {damage} damage'.format(myname = self.name, otherpet = other_pet.name, damage = self.attack / 2))
      print('It\'s not very effective.')
      other_pet.lose_health(self.attack / 2)

    if (self.type == other_pet.type):
      print('{myname} attacked {otherpet} for {damage} damage'.format(myname = self.name, otherpet = other_pet.name, damage = self.attack))
      other_pet.lose_health(self.attack)

    if (self.type == 'Fire' and other_pet.type == 'Nature') or (self.type == 'Nature' and other_pet.type == 'Water') or (self.type == 'Water' and other_pet.type == 'Fire') or (self.type == 'Flying' and other_pet.type == 'Nature') or (self.type == 'Electric' and other_pet.type == 'Flying'):
      print('{myname} attacked {otherpet} for {damage} damage.'.format(myname = self.name, otherpet = other_pet.name, damage = self.attack * 2))
      print('It was super effective!')
      other_pet.lose_health(self.attack * 2)

class Player:
  def __init__(self, pet_list, num_potions, name):
    self.pets = pet_list
    self.potions = num_potions
    self.name = name
    self.current_pet = 0

  def __repr__(self):
    'The player {name} has the following pets'.format(name = self.name)
    for pet in self.pets:
      print(pet)
    return 'The player\'s current pet is {name}'.format(name = self.pets[self.current_pet].name)
    

  def switch_active_pet(self, new_active):
    if new_active < len(self.pets) and new_active >= 0:
      if self.pets[new_active].knocked_out:
        print('You can\'t switch to that pet, they\'re knocked out!')
      elif new_active == self.current_pet:
        print('That pet is already active')
      else: self.current_pet == new_active
    print('Your turn {pet}, go get em\'!'.format(pet = self.pets[self.current_pet].name))
  
  def use_potion(self):
    if self.potions > 0:
      print('You used a potion on {pet}, they gained 60 health'.format(pet = self.pets[self.current_pet].name))
      self.pets[self.current_pet].gain_health(60)
      self.potions -= 1
    else:
      print('You are out of potions.')

  def attacking_other_player(self, other_player):
    my_pet = self.pets[self.current_pet]
    other_player_pet = other_player.pets[other_player.current_pet]
    my_pet.attacking(other_player_pet)

#Available pets

a = Pet('Lil Ragnaros', 200, 70, 'Fire')
b = Pet('Water Elemental', 140, 55, 'Water')
c = Pet('Dryad', 155, 50, 'Nature')
d = Pet('Gryphon Hatchling', 140, 60, 'Flying')
e = Pet('Lil Thrall', 180, 65, 'Electric')
f = Pet('Tonka Tank', 220, 35, 'Electric')

#Players input their names and the pets they want
  
player_1_name = input('Please enter a name for player one ')
player_2_name = input('Please enter a name for player two ')

choice = input('Alright ' + player_1_name + '! Please choose between "Lil Ragnaros" or "Water Elemental". ' + player_2_name + ' will get the one you do not choose.')

while choice != 'Lil Ragnaros' and choice != 'Water Elemental':
  choice = input('Oops, looks like your choice was invalid, please try again. ')

player_1_pets = []
player_2_pets = []

if choice == 'Lil Ragnaros':
  player_1_pets.append(a)
  player_2_pets.append(b)

else:
    player_1_pets.append(b)
    player_2_pets.append(a)

choice = input('Let\'s choose your second pet ' + player_2_name + ', pick between "Dryad" or "Grypon Hatchling. ' + player_1_name + ' will recieve the one you do not choose. ')

while choice != "Dryad" and choice != "Grypon Hatchling":
  choice = input('Oops, looks like your choice was invalid, please try again. ')

if choice == 'Dryad':
  player_2_pets.append(c)
  player_1_pets.append(d)
else:
  player_2_pets.append(d)
  player_1_pets.append(c)

choice = input(player_1_name + ' for you last pet, please choose between "Lil Thrall" or "Tonka Tank". ' + player_2_name + ' will recieve the one you do not choose. ')

while choice != 'Lil Thrall' and choice != 'Tonka Tank':
  choice = input('Oops, looks like your choice was invalid, please try again. ')

if choice == 'Lil Thrall':
  player_1_pets.append(e)
  player_2_pets.append(f)
else:
  player_1_pets.append(f)
  player_1_pets.append(e)

# Defining the players with their given inputs

player_one = Player(player_1_pets, 3, player_1_name)
player_two = Player(player_2_pets, 3, player_2_name)

# Game message for match startup
print('Let the fate of Azeroth lay in this battle! Here are our champions!')

print(player_one)
print(player_two)