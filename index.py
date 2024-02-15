def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


dice_a = random.randint(1, 6)
dice_b = random.randint(1, 6)
first_roll = dice_a + dice_b
print(f"First roll: {first_roll}")

if first_roll == 7 or first_roll == 11:
    print("You win")
elif first_roll in (2, 3, 12):
    print("Casino wins")
else:
    print(f"Goal number is: {first_roll}")

    goal_number = first_roll

    while True:
        next_roll = roll_dice()
        print(f"Next roll: {next_roll}")
        if next_roll == 7:
            print("You lose")
            break
        elif next_roll == goal_number:
            print("Player wins")
            break
        else:
            print("Roll again")
