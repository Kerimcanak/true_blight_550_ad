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
print("a man approaches you, 'Who are you, what god do you beleive in?', he is a fat man with a bushy moustache. What will you respond?")
religion_selection = input("A: 'I worship Wudanaz, my sir.' B: 'I am a Christian, worshipper of Jesus.' C: 'I am one with nature.' >> ")
if religion_selection.lower() == "a":
    print("'I worship Wudanaz, my sir.'")
elif religion_selection.lower() == "b":
    print("'I am a Christian, worshipper of Jesus.'")
elif religion_selection.lower() == "c":
    print("'I am one with nature.'")
    from Characters.genderlessplayer.player import player_stats
    print(player_stats)
    time.sleep(1)
    print("The mman asks 'Hmm, so you are one of those pagans, poor you. What is your name then?")
else:
    print("Invalid input. Game over.")
    exit()
name = input("Name: ")
player_stats["name"] = name
print(player_stats)
if player_stats["religion"] == "pagan":
    print("Man says: 'Interesting one! Perhaps we can work it out, one day you can get baptised and saved. Good luck, my boy. Now I know you, you can go but follow me if you wanna survive.'")
elif player_stats["religion"] == "christian":
    print("Man says: 'Interesting one! Perhaps we can work it out my brother in Christ, you are saved in eyes of God. Good luck, my boy. I almost thought you were hostile. Follow me if you wanna survive.'")
tutorial_selection = input("Would you like to play the tutorial? (y/n) >> ")
if tutorial_selection.lower() == "y":
    print("Tutorial")
elif tutorial_selection.lower() == "n":
    print("No tutorial")
else:
    print("Invalid input. Game over.")
    exit()
