myGlobal = [5,2]

def func1():
    global myGlobal
    myGlobal = [0,52]

def func2():
    print myGlobal[1]

func1()
func2()