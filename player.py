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
        else: 
            self.current_pet = new_active  # Fixed this line
        print('Your turn {pet}, go get em\'!'.format(pet=self.pets[self.current_pet].name))

  
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
    
    if my_pet.knocked_out:
        print("{name} is knocked out and can't attack!".format(name=my_pet.name))
    else:
        my_pet.attacking(other_player_pet)