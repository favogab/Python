# Coke Machine
# This program simulates a coke machine that accepts coins and calculates change.
amount_due = 50   # BEFORE loop

# check if amount_due is greater than 0
while amount_due > 0: # LOOP
    coin = int(input("Insert Coin: "))  

     # check if coin is valid (25, 10, or 5)
    if coin == 25 or coin == 10 or coin == 5:   # VALIDATE coin
        amount_due -= coin

      # check if amount_due is still greater than 0
    if amount_due > 0:    # STILL owe money?
        print("Amount Due:", amount_due)

print("Change Owed:", -amount_due)   # AFTER loop