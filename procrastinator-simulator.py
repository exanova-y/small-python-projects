from random import *
from time import sleep

#a function to choose random event and update the task time quickly
def decision(d, minutes, bonus):
  item = choice(list(d))
  print(item)
  minutes += d[item][0]+bonus
  bonus +=d[item][1]
  return minutes, bonus

#introduce the program
print("Ever wondered how long it takes for a procrastinator to finish a task? Welcome to the Simulator!")
print("(｡･∀･)ﾉﾞ\n")
sleep(2)
print("(Challenge: Can you complete the task faster than the original time?)")
sleep(1)

#user inputs
minutes = int(input("Pick a task. Enter how long it takes in minutes. (All calculations will be in minutes) "))
originalTime = minutes
bonus = 0
website = input("What is a website you like? ")
p = ["yes", "y", "Yes", "Y"]

print("\nYou are at home. Added 10 minutes.\n")
minutes += 10
sleep(1)

#mental state
minutes, bonus = decision({"You dreamed of civilization collapse. You can't stop thinking about it.":[0, 5], "You slept for too long and you're exhausted today.":[0, 20], "You had a good sleep, thus you'll be able to complete steps quicker":[0, -10], "Someone blasted loud music and you can't sleep. You become irritable. ": [0, 10]}, minutes, bonus)
print()
sleep(1)

#print a random outdoor distraction with the decision function. The same for distractions below.
input("You hear a weird noise outside. It's a sound you've never heard before.\n(enter to continue)")
minutes, bonus = decision({"You jump out of the window to see what's going on. You return. ":[5, 0], "You plug your ears and try to ignore it.":[0, 1], "Your brain goes into a million directions thinking about the noise.":[5, 0]}, minutes, bonus)
sleep(1)

#indoor distraction 
input("\nNow is a perfect time to get work done, you think.(enter to continue)")
minutes, bonus = decision({"Instructions were unclear. You email the teacher. Teacher disappeared.":[240, 0], "You get a call from a scammer in Burkina Faso. ":[10, 0], "People are loudly running around in your house. You can't focus. Might as well join them.":[10, 0], "A family member marches into your room. They insist on debating you, right now.":[30, 0]}, minutes, bonus)
sleep(2)

#device distraction
input("\nYou decide to take a break.(enter to continue)")
minutes, bonus = decision({"You find an article about octopus.":[20, 0], "You decide now is a great time for video editing!":[60, 0], "You make a comprehensive to do list and throw it away.":[120, 0], "You find a photo from your childhood and decide to do the same thing again.":[60, 0]}, minutes, bonus)
sleep(1)

print("\nYou work on task for 10 minutes.")
minutes += 10+bonus
sleep(1)

#check if user likes task
fun  = input("Do you like the task? (yes/no) ")
likeTask = (fun in p)
if likeTask:
  bonus -=10
  print("You get an energy boost.")
else:
  session = randint(10, 120)
  minutes += session+bonus
  print("You go off to", website, "for", session,"minutes")
sleep(1)

#personal distraction
input("\nYou sit down again.(enter to continue)")
minutes, bonus = decision({"You wash your hands.":[0, 1], "You think about death, life and stealing books":[0, 2], "You decide to check "+website+". A picture disturbs you.":[0, 2], "You just remembered, you missed a meeting 2 hours ago.":[0, 0], "You spot a pencil out of place, and go on an organization spree.":[30, 0], "A mosquito buzzes around your head. You scratch your ears and wonder if there are bugs.":[5, 0], "You can't stop thinking about food.":[0, 2]}, minutes, bonus)
sleep(1)

#time distraction
input("\nYou wonder what time it is.(enter to continue)")
minutes, bonus = decision({"You open your phone and scroll through emails for no reason. Wait, what are we doing again?":[5, 0], "It is 11pm.":[1, 0]}, minutes, bonus)
sleep(1)

#check time limit of task
limit = input("\nIs there a time limit for the task? Choose number:\n1. Due next week. 2. Due tomorrow. 3. Self-imposed deadline 4. No limits: ")

if likeTask:
  flowTime = originalTime/4
  print("You enter flow state. Everything else turns into blurs. Task is completed in", flowTime, "minutes.")
else:
  if "1" in limit:
    minutes +=8640
    print("You decide to finish the remaining bits over 6 days.")
  elif "2" in limit:
    minutes -=20
    print("You start sweating.")
  elif "3" in limit:
    minutes -=5
    print("You shake your head.")
  else: 
    minutes +=40320
    print("You decide to come back 4 weeks later.")
  minutes +=bonus
sleep(1)

#convert time into understandable units
print("\n(∪.∪ )...zzz\n")
if minutes >= 1440:
  finishTime = round(minutes/60/24, 1)
  state = "days"
elif minutes >= 60:
  finishTime = round(minutes/60 ,1)
  state = "hours"
else:
  finishTime = minutes
  state = "minutes"

print("After", finishTime, state, ", you successfully completed the task that you thought to be", originalTime, "minutes long.")
sleep(2)
print("Thank you for using the Procrastinator Simulator.")