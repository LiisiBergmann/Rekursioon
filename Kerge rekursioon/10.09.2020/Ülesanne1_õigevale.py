
def esineb(väärtus, järjend):

    if len(järjend) == 0:
        return False
    elif järjend[0] == väärtus:
        return True
    else:
        return esineb(väärtus, järjend[1:])




print(esineb("a",["c", "e","u","a"])) # see asi peab just siin kandiliste sulgude vahel olema, kui seda pole on tulemuseks False