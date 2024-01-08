# Add random number in the range of 1 to 100 and stop adding when the number to be addedis 50

import random
sum = 0
a = 0
while a != 50:
    a = random.randint(0,100)
    print (a)
    sum += a
    if a == 50:
        break
print(sum)