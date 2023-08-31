class Pet:
  def __init__(self, name, health, attack, type):
    self.name = name
    self.health = health
    self.attack = attack 
    self.type = type
    self.knocked_out = False

  def __repr__(self):
    return '{name} is a {type} type, with {attack} attack and {health} health.'.format(name = self.name, type = self.type, attack = self.attack, health = self.health)

  def set_knocked_out(self):
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
       self.set_knocked_out()
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