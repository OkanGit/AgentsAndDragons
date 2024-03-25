import random

class Player:
    def __init__(self, name, hp, mp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        enemy.take_damage(damage)
        print(f"{self.name} deals {damage} damage to {enemy.name}!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

class Monster:
    def __init__(self, name, hp, max_hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack

    def attack_player(self, player):
        damage = random.randint(self.attack - 3, self.attack + 3)
        player.take_damage(damage)
        print(f"{self.name} attacks! {self.name} deals {damage} damage to {player.name}!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

def battle(players, monster):
    print(f"A {monster.name} draws near!")
    while all(player.is_alive() for player in players) and monster.is_alive():
        for player in players:
            if not player.is_alive():
                continue
            print(f"\n{player.name}'s HP: {player.hp}/{player.max_hp} | MP: {player.mp}/{player.max_mp}")
        print(f"\n{monster.name}'s HP: {monster.hp}/{monster.max_hp}\n")

        # Players' turn
        for player in players:
            if not player.is_alive():
                continue
            print(f"\n{player.name}'s turn:")
            player_choice = input("What will you do? (attack/defend/item): ").lower()
            if player_choice == "attack":
                player.attack_enemy(monster)
            elif player_choice == "defend":
                print(f"{player.name} defends!")
            elif player_choice == "item":
                print(f"{player.name} uses an item!")
                # Implement item usage logic here
            else:
                print("Invalid choice! You lose your turn.")
            if not monster.is_alive():
                break

        # Monster's turn
        if monster.is_alive():
            print("\nMonster's turn:")
            monster.attack_player(random.choice(players))

    if all(player.is_alive() for player in players):
        print(f"\nVictory! {', '.join(player.name for player in players)} defeated {monster.name}!")
    else:
        print("\nDefeat... Game Over...")

# Example Usage
# players = [Player("Hero", 100, 50, 20), Player("Warrior", 120, 30, 25)]
# monster = Monster("Slime", 100, 100, 10)
# battle(players, monster)
