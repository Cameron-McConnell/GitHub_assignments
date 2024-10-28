import random
import tbc

# Define the Character class
class Character:
    def __init__(self, name, hit_points, hit_chance, max_damage, armor):
        self.name = name
        self.hitPoints = hit_points
        self.hitChance = hit_chance
        self.maxDamage = max_damage
        self.armor = armor

    def printStats(self):
        """Print the stats of the character."""
        print(f"{self.name} - HP: {self.hitPoints}, Hit Chance: {self.hitChance}%, Max Damage: {self.maxDamage}, Armor: {self.armor}")

    def attack(self, target):
        """Simulate an attack on another character."""
        if random.randint(1, 100) <= self.hitChance:
            damage = random.randint(1, self.maxDamage)
            damage_after_armor = max(damage - target.armor, 0)  # Ensure that damage is not negative
            print(f"{self.name} attacks {target.name} and deals {damage_after_armor} damage!")
            target.hitPoints -= damage_after_armor
        else:
            print(f"{self.name} missed the attack!")

    def is_alive(self):
        """Check if the character is still alive."""
        return self.hitPoints > 0

# Function to simulate the fight between Hero and Monster
def fight(hero, monster):
    """Simulate a combat between two characters."""
    while hero.is_alive() and monster.is_alive():
        print("\nHero's turn:")
        hero.attack(monster)
        monster.printStats()

        if not monster.is_alive():
            print(f"{monster.name} has been defeated!")
            break

        print("\nMonster's turn:")
        monster.attack(hero)
        hero.printStats()

        if not hero.is_alive():
            print(f"{hero.name} has been defeated!")
            break

# Function to handle input validation
def testInt(self, value, min = 0, max = 100, default = 0):
    """ takes in value
        checks to see if it is an int between
        min and max. if it is not a legal value
        set it to default """
    
    out = default
    
    if type(value) == int:
        if value >= min:
            out = value
        else:
            print("Too small")
    else:
        print("Must be an int")
        
    return out

# Main function to initialize the game
def main():
    def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    
    monster = tbc.Character("Monster", 20, 30, 5, 0)
    
    hero.printStats()
    monster.printStats()
    
    tbc.fight(hero,monster)

if __name__ == "__main__":
    main()
    
