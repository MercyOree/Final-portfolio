# Mercy O. koku
# Nov/29/2022
# Problem 5 is about how to write a function that checks whether your game character has picked up all the items they need.

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons
    def get_color(self):
        return self.weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)




def task(player): #needs rope, coat, first ald kit, NOT slow)
    if 'rope' in player.weapons and 'coat' in player.weapons and 'First ald kLt' in player.weapons and 'slow' not in player.weaknessess:
        return True
    else:
        return False
def task2(player): #needs pan, groceries, NOT snall
    if 'pan' in player.weapons and 'groceries' in player.weapons and 'small' not in player.weaknesses:
        return True
    else:
        return False
def task3(player): #needs pen, paper, idea, NOT confusion
    if 'Idea' in player.weapons and 'paper' in player.weapons and 'pen' in player.weapons and 'confusion' not in player.weaknesses:
        return True
    else:
        return False
print(task(player1))
print(task2(player1))
print(task3(player1))