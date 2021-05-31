def fizzbuzz():
    output = []
    for i in range(1,101):
        if(i%3 == 0):
            output.append("Fizz")
        elif(i%5 == 0):
            output.append("Buzz")
        else:
            output.append(i)
    return output

