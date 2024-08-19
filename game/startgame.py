import time

print("You are praying to the holy rider, Wudanaz, as you run away from the Huns...")
time.sleep(1)
print("And then you ride your horse as whistling arrows follow you.")
time.sleep(1)
print("You arrive on a random grove in northern Italy and the warband seem to have lost the track of you... You sleep.")
time.sleep(1)
print("*crow sound*")
time.sleep(1)
print("You wake up next to a river, it seems like no one is around except for you and your horse.")
time.sleep(1)
print("a man approaches you, 'Who are you, what god do you beleive in?', he is a fat man with a bushy moustache. What will you respond?")
selection = input("A: 'I worship Wudanaz, my sir.' B: 'I am a Christian, worshipper of Jesus.' C: 'I am one with nature.' >> ")
if selection.lower() == "a":
    print("'I worship Wudanaz, my sir.'")
elif selection.lower() == "b":
    print("'I am a Christian, worshipper of Jesus.'")
elif selection.lower() == "c":
    print("'I am one with nature.'")
    from ...  Assets.Scripts.Characters.playergenderless import player_genderless_stats
    print(player_genderless_stats)
else:
    print("Invalid input. Game over.")
    exit()