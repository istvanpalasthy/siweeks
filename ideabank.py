import sys

file=open("otlettakarek.txt","a")
idea=input("What is your new idea? ")
file.write(idea+"\n")
print("Your idea bank:",idea)
file.close()

with open("otlettakarek.txt", 'r') as f:
    for i, line in enumerate(f, start=1):
        print('{}. {}'.format(i, line.strip()))