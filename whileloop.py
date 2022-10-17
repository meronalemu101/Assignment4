response = False
iteration = 0

failsafe = 1

while not response:
    failsafe = failsafe + 1
    if failsafe == 10:
        break
    iteration = iteration + 1
    print("image1.png")
    if (10, 20) == 20:
        response = True
    print("image2.png")
# was able to get 20 responses but listing them one after another, not in sets of 10 each
2) import random

response = False
iteration = 0

while not response:
    iteration = iteration + 1
    print("Showing image for %i iterations until response given" % iteration)

    if random.randint(0, 10) == 1 or random.randint(0, 10) == 2:
        response = True

3) import random

response = False
iteration = 0

failsafe = -1

while not response:

    failsafe = failsafe + 1
    if failsafe == 20:
        break

    iteration = iteration + 1
    print("Showing image for %i iterations until response given" % iteration)

    if random.randint(0, 10) == 1 or random.randint(0, 10) == 2:
        response = True
