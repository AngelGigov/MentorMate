num = int(input("Please Enter Odd Number in diapasone of 1 to 10000: "))
if (num % 2) == 0:
    print("{0} is Even number". format(num))
    breakpoint()
elif (num <= 1 or num >= 10000):
    print("Entered number is out of range, please enter number in diapasone 1 to 10000")
    breakpoint()
else:
    pass
for row in range(num + 1):
    for col in range(num*10):
        if (row+col == num) or (row+col == num*3) or (row-col== -num) or (row -col == -num*3):
            print("*", end="")
        elif (row+col == 2*num-1) or (row+col == 4*num-1) or (col-row == num*2-1) or (col-row == num*4-1):
            print("*", end="")
        elif (row+col == 6*num) or (col-row==6*num) or (row+col==8*num) or (col-row==8*num):
            print("*", end="")
        elif (row+col == 7*num-1) or (col-row==7*num-1) or (row+col==9*num-1) or (col-row==9*num-1):
            print("*", end="")
        elif (row+col > 6*num and row+col < 7*num-1) or (col-row>6*num and col-row<7*num-1) or (row+col>8*num and row+col<9*num-1) or (col-row>8*num and col-row<9*num-1):
            print("*", end="")
        elif (row+col > num and row+col < 2*num-1) or (row+col > 3*num and row+col < 4*num-1) or (col-row >
         num and col - row < 2*num-1) or (col-row > num*3 and col-row < 4*num-1):
            print("*", end="")
        else:
            print("-", end="")
    print()
