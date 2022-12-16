import os
from subprocess import call

def cls():
    _ = call('clear' if os.name == 'posix' else 'cls')

def quit():
	cls()
	print('You are weak.')
	running = False
	return running

def game_over():
	print("\n***Game Over***")
	print("\ncontinue or quit?")
	user_input = input(':')
	if user_input == ('quit'):
		running = quit()
	elif user_input == ('continue'):
		running = True
	return running

running = True
while running==True:
	if running == False:
		break
	cls()

	#Initial Menu
	print('***Welcome to the Circus!***\n\nPlease enter a keyword to perform an action:')
	print('To tame the lions, lion')
	print('To ride an elephant, elephant')
	print('To use the flying trapeze, trap')
	print('To worship the devil, 666')
	print('\nEnter quit at anytime to exit.')
	user_input = input(':')

	if user_input == ('quit'):
		running = quit()

	#lion
	elif user_input == ('lion'):
		cls()
		print("Before you are two lions. They don't seem very happy...")
		print("What will you do?\n")
		print("feed")
		print("whip")
		user_input = input(':')

		if user_input == ('feed'):
			cls()
			print('You offer a piece of steak. The lions rush over and rip the meat from your hand and devour it.')
			print("Unfortunately, they don't stop there. They tear you apart... limb from limb.")
			running = game_over()


		elif user_input == ('whip'):
			cls()
			print('\nWow... that was a bad choice. Whipping a lion? What kind of moron are you?')
			print('The lions leap upon you and feast, starting with your legs.')
			running = game_over()

		elif user_input == quit:
			running = quit()

	#elephant
	elif user_input == ('elephant'):
		cls()
		print('The large gray creature directs its attention toward you. It seems docile enough...')
		print('Nearby you see a large bag of peanuts to feed the elephant and a step-ladder to ride, do you\n')
		print('feed')
		print('ride')
		user_input = input(':')

		if user_input == ('feed'):
			cls()
			print('\nThe elephant seems to really enjoy the peanuts as it gently eats them from your palm. "It tickles" you exclaim.')
			print("Suddenly... a mouse emerges from the bag of peanuts. The elephant reacts in terror leaping on to it's hind legs.")
			print("It lands with all of its force, crushing you.")
			running = game_over()

		elif user_input == ('ride'):
			cls()
			print("\nUsing a ladder, you climb upon the already saddled beast.")
			print("The truely gentle animal responds to your every command. What fun indeed...")
			print("In the midst of turning around, a mouse runs directly infront of the elephant.")
			print("Terrified, it bucks you off, rendering you paralyzed.")
			print("Rats begin to swarm and devour you.")
			running = game_over()

		elif user_input == ('quit'):
			running = quit()

	#trap
	elif user_input == ('trap'):
		cls()
		print("It should be a breeze the ride the trapeze, but alas, I shake at the knees.")
		print("What will you do?")
		print("ride")
		print("descend")
		user_input = input(':')

		if user_input == ('ride'):
			cls()
			print("Shakily, you wrap your hands around the bar and set off.")
			print("It is actually much easier than you expected. Weeeee.")
			print("Suddenly, one of the cables snap. You fall into the lion pit.")
			print("Paralyzed, you call for help, but it is too late.")
			print("Lions and rats devour you.")
			running = game_over()

		elif user_input == ('descend'):
			cls()
			print("The coward you are, you begin to climb back down the ladder.")
			print("Your sweaty coward hands slip and you fall, hitting every bar on the way down.")
			print("You are paralyzed. The elephants devour you.")
			running = game_over()

		elif user_input == ('quit'):
			running = quit()

	#666
	elif user_input == ('666'):
		cls()
		print("Praise to you, Satan! in the heights you lit")
		print("And also in the deeps where now you sit,")
		print("Vanquished, in Hell, and dream in hushed defiance")
		print("O that my soul, beneath the Tree of Science")
		print("Might rest near you, while shadowing your brows,")
		print("It spreads a second Temple with its boughs.")
		print("\nYou are consumed by rats.")
		running = game_over()