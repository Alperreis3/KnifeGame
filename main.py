import random

def play_knife_game():
    # Initialize the game
    fingers = ["index", "middle", "ring", "pinky"]
    lives = 3

    while lives > 0:
        # Choose a random finger to "stab"
        finger = random.choice(fingers)
        print(f"The knife is pointed at your {finger} finger!")

        # Prompt the player to choose a finger to "block" with
        choice = input("Choose a finger to block with (index, middle, ring, pinky): ")
        
        # Check if the player was "stabbed"
        if choice == finger:
            print("You were stabbed!")
            lives -= 1
        else:
            print("You blocked the knife!")
    
    print("Game over!")

# Start the game
play_knife_game()
