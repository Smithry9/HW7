def fizzbuzz():
    output = []
    for i in range(1,101):
        if(i%3 == 0):
            output.append("Fizz")
        else:
            output.append(i)
    return output

