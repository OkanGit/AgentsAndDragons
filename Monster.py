import random
import pandas as pd

class Monster:
    def __init__(self, name, hp, max_hp, attack, weaknesses):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.weaknesses = weaknesses

    def attack_player(self, player):
        damage = random.randint(self.attack - 3, self.attack + 3)
        player.take_damage(damage)
        if player.is_defending:
            #print(f"{self.name} attacks! {self.name} deals {damage/2} damage to {player.name}!")
            return f"{self.name} attacks! {self.name} deals {damage/2} damage to {player.name}!"
        else:
            #print(f"{self.name} attacks! {self.name} deals {damage} damage to {player.name}!")
            return f"{self.name} attacks! {self.name} deals {damage} damage to {player.name}!"

    def take_damage(self, damage):
        
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
        
    def is_alive(self):
        return self.hp > 0