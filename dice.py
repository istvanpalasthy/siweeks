import random

num1 = (random.randint(1,6))
num2 = (random.randint(1,6))
num3 = (random.randint(1,6))
num4 = (random.randint(1,6))
num5 = (random.randint(1,6))

print("Dice for the attacker:", num1,"-",num2,"-",num3)
print("Dice for the defender:", num4,"-",num5)

if num1 > num4 or num1 == num4 and num2 < num4:
    print("Outcome: Defender lost 1 unit and Attacker lost 1 unit")
elif num1 > num4 and num2 > num5:
    print("Outcome: Defender lost 2 unit")
elif num1 < num4 and num2 > num4:
    print("Attacker lost 1 unit and Defender lost 1 unit")
elif num1 < num4 and num2 < num5:
    print("Attacker lost 2 unit")
elif num2 > num5 and num4 > num2:
    print("Attacker lost 1 unit and Defender lost 1 unit")
elif num1 == num4 and num2 > num5:
    print("Attacker lost 1 unit and Defender lost 1 unit")
elif num1 < num3 and num2 == num5:
    print("Attacker lost 2 unit")
elif num1 > num3 and num2 == num5:
    print("Attacker lost 1 unit and Defender lost 1 unit")
elif num1 == num3 and num2 == num5:
    print("The attacker lost 2 unit")
elif num4 > num1 and num2 > num5:
    print("Attacker lost 1 unit and Defender lost 1 unit")