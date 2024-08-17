# #python 101
# class user_info:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def info(self):
#         return f'Name: {self.name}, Age: {self.age}'

# test = user_info('Beer', 21)

# info_string = test.info()
# print(info_string)

################################


class game_mmo_rpg:
    def __init__(self, character_name, character_class, character_level):
        self.character_name = character_name
        self.character_class = character_class
        self.character_level = character_level
        
    def info(self):
        return f'Character Name: {self.character_name}, Character Class: {self.character_class}, Character Level: {self.character_level}'
    
    def level_up(self):
        self.character_level += 1
        return f'Character {self.character_name} has leveled up to level {self.character_level}'
    
    def get_health(self):
        return f'Character {self.character_name} has {self.character_level * 10} health points'
    
    def get_experience(self):
        return f'Character {self.character_name} has {self.character_level * 100} experience points'
    
    def get_inventory(self):
        return f'Character {self.character_name} has {self.character_level} items in their inventory'
    
    def get_skills(self):
        return f'Character {self.character_name} has {self.character_level} skills'
    
    def get_spells(self):
        return f'Character {self.character_name} has {self.character_level} spells'
    
    def get_status(self):
        return f'Character {self.character_name} has {self.character_level} health points, {self.character_level * 100} experience points, {self.character_level} items in their inventory, {self.character_level} skills, and {self.character_level} spells'


test_game = game_mmo_rpg('Beer', 'Warrior', 1)

info_string = test_game.info()
print(info_string)    
    