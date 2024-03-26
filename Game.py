import random

class Player:
    def __init__(self, name, hp, mp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.is_defending = False

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        enemy.take_damage(damage)
        print(f"{self.name} deals {damage} damage to {enemy.name}!")
        return f"{self.name} deals {damage} damage to {enemy.name}!"

    def take_damage(self, damage):
        if self.is_defending:
            self.hp -= (damage * 0.5)
        else:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0
    
    def defend(self):
        self.is_defending = True
    
    def removeDefense(self):
        self.is_defending = False


class Monster:
    def __init__(self, name, hp, max_hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack

    def attack_player(self, player):
        damage = random.randint(self.attack - 3, self.attack + 3)
        player.take_damage(damage)
        if player.is_defending:
            print(f"{self.name} attacks! {self.name} deals {damage/2} damage to {player.name}!")
            return f"{self.name} attacks! {self.name} deals {damage/2} damage to {player.name}!"
        else:
            print(f"{self.name} attacks! {self.name} deals {damage} damage to {player.name}!")
            return f"{self.name} attacks! {self.name} deals {damage} damage to {player.name}!"

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0
    
        
class Battle:

    def __init__(self, players, monster) -> None:
        self.players = players
        self.monster = monster
        print(f"A {self.monster.name} draws near!")
        self.battlePrint = ""
        self.battlePrint = self.battlePrint + f"A {self.monster.name} draws near!"
        self.battleState()
        self.is_over = False
        pass

    def battleState(self):
                
        for player in self.players:
            if not player.is_alive():
                continue
            print(f"\n{player.name}'s HP: {player.hp}/{player.max_hp} | MP: {player.mp}/{player.max_mp}")
            self.battlePrint = self.battlePrint + f"\n{player.name}'s HP: {player.hp}/{player.max_hp} | MP: {player.mp}/{player.max_mp}"
        print(f"\n{self.monster.name}'s HP: {self.monster.hp}/{self.monster.max_hp}\n")
        self.battlePrint = self.battlePrint + f"\n{self.monster.name}'s HP: {self.monster.hp}/{self.monster.max_hp}\n"

        if not self.monster.is_alive():
            print(f"\nVictory! {', '.join(player.name for player in self.players)} defeated {self.monster.name}!")
            self.battlePrint = self.battlePrint + f"\nVictory! {', '.join(player.name for player in self.players)} defeated {self.monster.name}!"
            self.is_over = True
        elif all(not player.is_alive for player in self.players):
            print("Defeat! Every party member has died!")
            self.battlePrint = self.battlePrint + "Defeat! Every party member has died!"
            self.is_over = True
        else:
            print("What will you do? (attack/defend/item): ")
            self.battlePrint = self.battlePrint + "What will you do? (attack/defend/item): "

    def nextTurn(self, playerTurns):
        if not self.is_over:
            i=0
            for player in self.players:
                if not player.is_alive():
                    continue

                print(f"\n{player.name}'s turn:")
                self.battlePrint = self.battlePrint + f"\n{player.name}'s turn:"
                player_choice = playerTurns[i]

                if player_choice == "attack":
                    attackPrint = player.attack_enemy(self.monster)
                    self.battlePrint = self.battlePrint + attackPrint

                elif player_choice == "defend":
                    print(f"{player.name} defends!")
                    self.battlePrint = self.battlePrint + f"{player.name} defends!"
                    player.defend()

                elif player_choice == "item":
                    print(f"{player.name} uses an item!")
                    self.battlePrint = self.battlePrint + f"{player.name} uses an item!"
                    # Implement item usage logic here

                else:
                    print("Invalid choice! You lose your turn.")
                    self.battlePrint = self.battlePrint + "Invalid choice! You lose your turn."

                if not self.monster.is_alive():
                    break

                i += 1
            
            # Monster's turn
            if self.monster.is_alive():
                print("\nMonster's turn:")
                self.battlePrint = self.battlePrint + "\nMonster's turn:"
                monsterAttackPrint = self.monster.attack_player(random.choice(self.players))
                self.battlePrint = self.battlePrint + monsterAttackPrint

            for player in self.players:
                player.removeDefense()

            current = self.battlePrint
            self.battlePrint = ""
            self.battleState()
        else:
            print("The battle is already over!")
            current = "The battle is already over!"
        
        return current

# def battle(players, monster):

#     print(f"A {monster.name} draws near!")
#     while all(player.is_alive() for player in players) and monster.is_alive():

#         for player in players:
#             if not player.is_alive():
#                 continue
#             player.defend()
#             print(f"\n{player.name}'s HP: {player.hp}/{player.max_hp} | MP: {player.mp}/{player.max_mp}")
#         print(f"\n{monster.name}'s HP: {monster.hp}/{monster.max_hp}\n")

#         # Players' turn
#         for player in players:
#             if not player.is_alive():
#                 continue
#             print(f"\n{player.name}'s turn:")
#             player_choice = input("What will you do? (attack/defend/item): ").lower()
#             if player_choice == "attack":
#                 player.attack_enemy(monster)
#             elif player_choice == "defend":
#                 print(f"{player.name} defends!")
#                 player.defend()
#             elif player_choice == "item":
#                 print(f"{player.name} uses an item!")
#                 # Implement item usage logic here
#             else:
#                 print("Invalid choice! You lose your turn.")
#             if not monster.is_alive():
#                 break

#         # Monster's turn
#         if monster.is_alive():
#             print("\nMonster's turn:")
#             monster.attack_player(random.choice(players))

#     if all(player.is_alive() for player in players):
#         print(f"\nVictory! {', '.join(player.name for player in players)} defeated {monster.name}!")
#     else:
#         print("\nDefeat... Game Over...")

# Example Usage
# players = [Player("Hero", 100, 50, 20), Player("Warrior", 120, 30, 25)]
# monster = Monster("Slime", 100, 100, 10)
# battle(players, monster)