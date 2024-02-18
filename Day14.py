# EXERCISE : GOOD MORNING SIR!
# USING TIME MODULE

import time

print("Welcome!!")
print("\nCURRENT TIME :")

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestampH = int(time.strftime('%H'))
# print(timestampH)

# timestampM = int(time.strftime('%M'))
# print(timestampM)

# timestampS = int(time.strftime('%S'))
# print(timestampS)

if timestampH < 12:
    print("\nGood Morning sir!")

elif timestampH > 12 & timestampH <= 16:
    print("\nGood Afternoon Sir!")

elif timestampH > 16 & timestampH <= 21:
    print("\nGood Evening Sir!")

else:
    print("\nGood Night Sir!")
