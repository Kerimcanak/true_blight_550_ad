import time

print("You are praying to the ancestral spirit, Wudanaz, as you run away from the Huns...")
time.sleep(1)
print("And then you ride your horse as whistling arrows follow you.")
time.sleep(1)
print("You arrive on a random grove in northern Italy and the warband seem to have lost the track of you... You sleep.")
time.sleep(1)
print("*crow sound*")
time.sleep(1)
print("You wake up next to a river, it seems like no one is around except for you and your horse.")
time.sleep(1)
name = input("Name: ")
player_stats["name"] = name
print(f"{name}! You are still alive! Thank Wudanaz! Now I know I am safe, let’s go buddy, c’mon.")
time.sleep(1)
print("A figure appears on your back, a man in red Roman robes holding a sword, slightly fat with a mustache:")
time.sleep(1)
print("'Who are you, stranger? Why are you in our village?'")
time.sleep(1)
print(f"{name}! I am {name}! I am of Heruli tribe.")
time.sleep(1)
religion_selection = input("A: 'I am a man.' B: 'I am a woman.' C: 'I am one with nature.' >> ")
if religion_selection.lower() == "a":
    time.sleep(1)
    print("'A warrior? Then, your fate is determined.'")
    time.sleep(1)
    player_stats["weapon"] = "Sword"
    player_stats["profession"] = "Warrior"
elif religion_selection.lower() == "b":
    time.sleep(1)
    print("'A shield-bearer? May love protect you.'")
    time.sleep(1)
    player_stats["weapon"] = "Shield"
    player_stats["profession"] = "Shield-bearer"
elif religion_selection.lower() == "c":
    time.sleep(1)
    print("'A shaman? Then, you already know it.'")
    time.sleep(1)
    player_stats["weapon"] = "Feathered Spear"
    player_stats["profession"] = "Shaman"
else:
    print("Invalid input. Game over.")
    exit()
time.sleep(1)
print(player_stats)
