firstnumber = int(input())
lastnumber = int(input())
result = firstnumber * lastnumber 
print(result)
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")