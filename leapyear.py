def leapyear(inputYear):
    if(inputYear % 4 == 0):
        if(inputYear % 100 == 0):
            return False
        else:
            return True
    return False
