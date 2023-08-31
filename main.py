from pet import Pet
from player import Player

def battle(player_one, player_two):
    while True:
        # Player 1's turn
        print(f"\n{player_one.name}'s Turn:")
        action = input("Choose your action ('attack', 'swap', 'potion'): ").strip().lower()

        if action == 'attack':
            player_one.attacking_other_player(player_two)
        elif action == 'swap':
            new_active = int(input('Which pet would you like to swap to? (Enter 0, 1, or 2): '))
            player_one.switch_active_pet(new_active)
        elif action == 'potion':
            player_one.use_potion()
        else:
            print("Invalid action, please try again.")
            continue

        if all(pet.knocked_out for pet in player_two.pets):
            print(f"{player_one.name} wins!")
            break

        # Player 2's turn
        print(f"\n{player_two.name}'s Turn:")
        action = input("Choose your action ('attack', 'swap', 'potion'): ").strip().lower()

        if action == 'attack':
            player_two.attacking_other_player(player_one)
        elif action == 'swap':
            new_active = int(input('Which pet would you like to swap to? (Enter 0, 1, or 2): '))
            player_two.switch_active_pet(new_active)
        elif action == 'potion':
            player_two.use_potion()
        else:
            print("Invalid action, please try again.")
            continue

        if all(pet.knocked_out for pet in player_one.pets):
            print(f"{player_two.name} wins!")
            break

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

print('Let the fate of Azeroth lay in this battle! Here are our champions!')
print(player_one)
print(player_two)

# Start the battle
battle(player_one, player_two)
