from time import sleep
import random
running = "y"

def wallet():
	print("\nWallet:")
	print("(₿)", btc, "Bitcoins\n")

def gameover():
	for x in range(3):
		print("~"*2)
		sleep(0.5)
	print("You died!")
	print("Somebody tried to swim in lava.")
	sleep(1)
	print("You started on floor",start, "and earned",btc, "bitcoins")
	running = input("Respawn?(y/n)") 
	return running

def robber(btc, floor):
	if btc >1:
		amount = random.randint(1, int(btc))
		btc = btc - amount
		print("The evil Mark Robber hacked your wallet.")
	else:
		amount = random.randint(1, 5)
		print("Mark Robber tried to rob you.")
		sleep(1)
		btc = btc+ amount
		print("but you robbed him", amount, "bitcoins instead")
	wallet()
	return btc, floor


def fall(btc, floor):
	print("You slipped and fell down the stairs")
	sleep(2)
	amount = random.randint(1, int(floor-1))
	floor = floor - amount
	print("You are now on floor", floor)
	if floor == 1:
		gameover()
	return btc, floor


def elevator(btc, floor):
	if floor%2 > 0:
		to = floor*3+1
	else:
		to = int(floor/2)
	print("An elevator is available. It goes to floor", to)
	enter = input("Enter? (y/n)")

	while enter not in ("y", "n"):
		enter = input("Enter? (y/n)") 
	if enter.lower() == "n":
		print("The elevator left")
		sec = random.randint(1, 3)
		for _ in range(sec):
			sleep(1)
			print("...")
		event = random.choice([fall, robber])
		btc, floor = event(btc, floor)

	else:
		print("You walk in")
		sleep(1)
		floor = to
		print("You are now on floor", floor)
		if floor == 1:
			running = gameover()
	return floor

#rules
while running.lower() == "y":
	btc = 0
	mine = "c"
	running = "y"

	print("(₿)\t", "Minin' Away\t", "(₿)\n" )
	note = input("Read the note? (y/n)")
	if note.lower() == "y":
		print("~"*5)
		input("The first floor of your hotel has turned into lava")
		input("The only way to survive is to go to higher floors.")
		input("Odd numbered floors have elevators that go up to even numbered floors.")
		input("Floor 3 ⬆⬆⬆  Floor 10 ")
		input("All even numbered floors have bitcoin miners")
		input("But elevators only go to lower odd floors")
		input("Floor 10 ⬇⬇⬇  Floor 5 ")
		input("You can't wait to mine Bitcoins")
		print("~"*5)
		
	start = int(input("Choose a floor to begin: "))
	floor = start
	while floor > 1:
		if floor%2 >0: #if odd
			print("▩ "*5)
			print("Doors are closed.")
			sleep(1)
			floor= elevator(btc,floor)


		if floor%2 == 0: #if even
			if mine in ("c", "C"):
				print("▢ "*5)
				print("Doors are open!")
				foundbtc = random.randint(1, 10)
				print("This door has", foundbtc, "bitcoins")
				mine = input("Mine bitcoins or check other doors? (m/c)")
				while mine.lower() not in ("m", "c"):
					mine = input("Mine bitcoins or check other doors? (m/c)")
			if mine.lower() == "m":
				print("Mining")
				for _ in range(3):
					print(".")
					sleep(0.5)
				mine = "c"
				result = random.choice(["Success!", "Failed"])
				print(result)
				if result == "Success!":
					btc = btc + foundbtc
				floor = elevator(btc, floor)
				wallet()
				sleep(2)

print("Share your high score on social media!")