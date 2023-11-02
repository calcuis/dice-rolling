import random

dice_code = {
    1: ("⚀"),
    2: ("⚁"),
    3: ("⚂"),
    4: ("⚃"),
    5: ("⚄"),
    6: ("⚅")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in dice:
    print(dice_code.get(die), end="")
print()

for die in dice:
    total += die
print(f"total: {total}")
