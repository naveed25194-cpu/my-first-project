import random

def draw_winner(participants):
	"""Return one random winner from the participant list."""
	if not participants:
		raise ValueError("Participant list is empty.")
	return random.choice(participants)

def main():
	participants = ["Walid","Tariq","Farooq","Hameed","Izhan","Hira", "Anis", "Naveed", "Mustafa", "Zainab", "Haleema"]

	winner = draw_winner(participants)
	print("Lucky Draw Participants:", ", ".join(participants))
	print("Winner:", winner)

if __name__ == "__main__":
	main()