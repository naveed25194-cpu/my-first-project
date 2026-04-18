import random


def ask_choice(question, choices):
	"""Ask the user to choose from a list of options."""
	print("\n" + question)
	for i, choice in enumerate(choices, start=1):
		print(f"  {i}. {choice}")

	while True:
		answer = input("Choose a number: ").strip()
		if answer.isdigit():
			index = int(answer) - 1
			if 0 <= index < len(choices):
				return index
		print("That is not a valid choice. Try again.")


def lucky_event(score):
	"""Random event that changes score for extra fun."""
	events = [
		("You found a rocket-powered sandwich. +3 points", 3),
		("A sleepy dragon stole your socks. -2 points", -2),
		("You did an epic backflip. +2 points", 2),
		("You stepped on a banana peel dramatically. -1 point", -1),
		("A wizard gave you glitter armor. +4 points", 4),
	]
	text, delta = random.choice(events)
	print("\nLucky event:", text)
	return score + delta


def run_game():
	print("=" * 45)
	print("   WELCOME TO THE SILLY ADVENTURE GAME")
	print("=" * 45)
	name = input("What is your hero name? ").strip() or "Captain Mystery"
	print(f"\nHello, {name}! Your quest is to collect fun points.")

	score = 0

	# Round 1
	c1 = ask_choice(
		"You enter a neon forest. What do you do?",
		["Dance with robots", "Sneak past glowing mushrooms", "Ride a giant snail"],
	)
	if c1 == 0:
		print("The robots love your moves. +2 points")
		score += 2
	elif c1 == 1:
		print("You stay stealthy but miss the party. +1 point")
		score += 1
	else:
		print("The snail is slow but legendary. +3 points")
		score += 3

	score = lucky_event(score)

	# Round 2
	c2 = ask_choice(
		"A troll asks for the secret password:",
		["Please", "Banana Thunder", "1234"],
	)
	if c2 == 1:
		print("Correct! The troll gives you a high five. +3 points")
		score += 3
	else:
		print("Not quite. The troll gives you a sticker anyway. +1 point")
		score += 1

	score = lucky_event(score)

	# Final challenge
	c3 = ask_choice(
		"Final challenge: pick your finishing move!",
		["Thunder Joke", "Mega Yawn", "Confetti Cannon"],
	)
	if c3 == 2:
		print("Confetti everywhere! Crowd goes wild. +4 points")
		score += 4
	elif c3 == 0:
		print("The villain laughs so hard they surrender. +3 points")
		score += 3
	else:
		print("Everyone gets sleepy... but peaceful. +2 points")
		score += 2

	print("\n" + "-" * 45)
	print(f"Adventure complete, {name}!")
	print(f"Final score: {score}")

	if score >= 12:
		print("Rank: LEGEND OF CHAOS")
	elif score >= 8:
		print("Rank: HERO OF GIGGLES")
	else:
		print("Rank: APPRENTICE OF FUN")
	print("-" * 45)


def main():
	while True:
		run_game()
		again = input("\nPlay again? (y/n): ").strip().lower()
		if again not in {"y", "yes"}:
			print("Thanks for playing. Stay awesome!")
			break


if __name__ == "__main__":
	main()
