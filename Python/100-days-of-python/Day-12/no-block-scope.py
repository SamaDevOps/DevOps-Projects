# There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

boss_level = 10

def boss_fight():
    global boss_level
    boss_level += 1
    if boss_level > 10:
        print(f"you will be fighting {enemies[1]}")

boss_fight()