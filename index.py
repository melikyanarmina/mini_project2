import random
dice_a= random.randint(1, 6)
dice_b= random.randint(1, 6)

first_roll=dice_a+dice_b
print(f"First roll: {first_roll}")

if first_roll == 7 or first_roll == 11:
   print("You win")
elif first_roll in (2,3,12):
   print("Casino wins")
goal_nums=4,5,6,8,9,10

print(f"Goal numbers are: {goal_nums}")
next_roll = dice_a + dice_b


if next_roll == 7:
            print("You lose")

elif next_roll in goal_nums:
            print("Player wins")

