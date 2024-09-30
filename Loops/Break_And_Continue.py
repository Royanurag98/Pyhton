# Break : It is used to terminate the loop when encountered.

i=0
while i<=5:
    print("Our loop is Executing.......")
    if i==3:
        print("Now our loop is terminate......")
        break
    i+=1
#Continue : it use to terminates execution in the current iteration and continues execution of the loop with the next iteration.
i=0
while i<=5:
    
    if i==3:
        i+=1
        print("Now our skeep the execution from current line......")
        continue
    print("Our loop is Executing.......")
    i+=1
