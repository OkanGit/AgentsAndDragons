import random
import pandas as pd
import Monster

class Player:
    def __init__(self, name, hp, mp, attack, abilities : pd.DataFrame):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack = attack
        self.is_defending = False
        self.abilities = abilities

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5)
        enemy.take_damage(damage)
        #print(f"{self.name} attacks! {self.name} deals {damage} damage to {enemy.name}!")
        return f"{self.name} attacks! {self.name} deals {damage} damage to {enemy.name}!"

    def useAttackAbility(self, enemy, abilityName):
        ability = self.abilities[self.abilities["Name"] == abilityName]
        #print(ability)

        if any(weakness in ability["Attributes"] for weakness in enemy.weaknesses):
            damage = random.randint(self.attack - 5, self.attack + 5) * float(ability["Damage Multiplier"].iloc[0]) * 1.5
        else:
            damage = random.randint(self.attack - 5, self.attack + 5) * float(ability["Damage Multiplier"].iloc[0])

        enemy.take_damage(damage)
        print(f"{self.name} uses {abilityName}! {self.name} deals {damage} damage to {enemy.name}!")
        return f"{self.name} uses {abilityName}! {self.name} deals {damage} damage to {enemy.name}!"
        
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