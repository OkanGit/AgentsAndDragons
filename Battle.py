import random
import pandas as pd
        
class Battle:

    def __init__(self, players, monster) -> None:
        self.players = players
        self.monster = monster
        self.is_over = False

        self.moveList = {}

        #print(f"A {self.monster.name} draws near!")
        self.battlePrint = ""
        self.battlePrint = self.battlePrint + f"A {self.monster.name} draws near!"
        self.battleState()
        
        pass

    def battleState(self):
        
        print(self.battlePrint)
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
            print("What will you do?")
            self.battlePrint = self.battlePrint + "What will you do?"
        
        return self.battlePrint

    def nextTurn(self, playerTurns):
        
        self.battlePrint = ""
        if not self.is_over:
            i=0
            for player in self.players:
                if not player.is_alive():
                    continue

                print(f"\n{player.name}'s turn:")
                self.battlePrint = self.battlePrint + f"\n{player.name}'s turn:"
                player_choice = playerTurns[i]

                if player_choice.lower() == "attack":
                    attackPrint = player.attack_enemy(self.monster, [])
                    self.battlePrint = self.battlePrint + attackPrint

                elif player_choice.lower() == "defend":
                    print(f"{player.name} defends!")
                    self.battlePrint = self.battlePrint + f"{player.name} defends!"
                    player.defend()

                elif player_choice.lower() == "item":
                    print(f"{player.name} uses an item!")
                    self.battlePrint = self.battlePrint + f"{player.name} uses an item!"
                    # Implement item usage logic here

                else:
                    
                    for ability in player.abilities["Name"]:
                        if player_choice == ability:
                            print(f"\n{player.name} uses {ability}! ")
                            self.battlePrint = self.battlePrint + f"\n{player.name} uses {ability}! "
                            attackPrint = player.attack_enemy(self.monster, player.abilities[player.abilities["Name"] == ability]["Attributes"])
                            self.battlePrint = self.battlePrint + attackPrint
                            break

                    # print("Invalid choice! You lose your turn.")
                    # self.battlePrint = self.battlePrint + "Invalid choice! You lose your turn."

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

            self.battleState()
            current = self.battlePrint
            
        else:
            print("The battle is already over!")
            current = "The battle is already over!"
        
        return current

    def enterAttack(self, player):

        self.moveList[player.name] = "attack"

        print(f"{player.name} has selected attack")

        if all(player.name in self.moveList.keys() for player in self.players):
            self.executeTurn()
    

    def enterDefend(self, player):

        self.moveList[player.name] = "defend"

        print(f"{player.name} has selected defend")

        if all(player.name in self.moveList.keys() for player in self.players):
            self.executeTurn()

    def enterAbility(self, player, ability):

        self.moveList[player.name] = ["ability", ability]

        print(f"{player.name} has selected ability")

        if all(player.name in self.moveList.keys() for player in self.players):
            self.executeTurn()

    def executeTurn(self):

        self.battlePrint = ""
        if not self.is_over:
            for player in self.players:
                
                move = self.moveList[player.name]

                if not player.is_alive():
                    continue
                
                if not self.monster.is_alive():
                    break
                #print(f"\n{player.name}'s turn:")
                self.battlePrint = self.battlePrint + f"\n{player.name}'s turn:"

                if type(move) == str:
                    if move == "attack":
                        attackPrint = player.attack_enemy(self.monster)
                        self.battlePrint = self.battlePrint + attackPrint

                    elif move == "defend":
                        #print(f"{player.name} defends!")
                        self.battlePrint = self.battlePrint + f"{player.name} defends!"
                        player.defend()

                else:
                    if move[0] == "ability":
                        
                        #print(f"\n{player.name} uses {move[1]}!")
                        attackPrint = player.useAttackAbility(self.monster, move[1])
                        self.battlePrint = self.battlePrint + attackPrint
                        break

            
            # Monster's turn
            if self.monster.is_alive():
                #print("\nMonster's turn:")
                self.battlePrint = self.battlePrint + "\nMonster's turn:"
                monsterAttackPrint = self.monster.attack_player(random.choice(self.players))
                self.battlePrint = self.battlePrint + monsterAttackPrint

            for player in self.players:
                player.removeDefense()

            self.battleState()
            current = self.battlePrint
            
        else:
            print("The battle is already over!")
            current = "The battle is already over!"
       
        self.moveList = {}
        print("Turn executed")


# Example Usage
# players = [Player("Hero", 100, 50, 20), Player("Warrior", 120, 30, 25)]
# monster = Monster("Slime", 100, 100, 10)
# battle(players, monster)