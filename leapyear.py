def leapyear(inputYear):
    if(inputYear % 4 == 0):
        if(inputYear % 100 == 0):
            if(inputYear % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    return False
