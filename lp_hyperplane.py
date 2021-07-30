import string

#not lineare separable? => delta = False
#lineare separable? => delta = True

def create_lp_hyper(function: [str], bounds: [str], x1: [float], y1: [float], x2: [float], y2: [float], delta=True) -> str:
    
    #constant initialisation
    function[0] = ""

    #generate function to maximize
    z = "maximize\n\tdelta"
    s = ""
    #generate constraints based on x and y values for class 1
    s += "\n\nsubject to\n"
    for i in range(len(x1)):
        copy_function = list(function)
        above = "\t"
        for j in range(len(copy_function)):
            value = ""
            if (copy_function[j] != ""):
                value = str(eval(copy_function[j].replace("x", str(x1[i]))))
            above += value + " " + string.ascii_lowercase[j].replace("e", "") + " + "
        above += "delta <= " + str(y1[i]) + "\n"
        s+=above
    s+= "\n"
    
    #generate constraints based on x and y values for class 2
    for i in range(len(x2)):
        copy_function = list(function)
        below = "\t"
        for j in range(len(copy_function)):
            value2 = ""
            if (copy_function[j] != ""):
                value2 = str(eval(copy_function[j].replace("x", str(x2[i]))))
            below += value2 + " " + string.ascii_lowercase[j].replace("e", "") + " + "
        below += "- delta >= " + str(y2[i]) + "\n"
        s+=below.replace(" + - ", " - ")
    
    #generate constraints for variables
    s += "\nbounds\n\t"
    for i in range(len(bounds)):
        s += string.ascii_lowercase[i] +" " + bounds[i] + "\n\t"
    s+= "delta >= 0"
    
    #not lineare separable
    if not delta: 
        z = "minimize\n\t"
        s = s.replace("<=", "=").replace(">=", "=")
        for i in range(len(x1)):
            s = s.replace("delta", "u" + str(i) + " - v" + str(i), 1)
            z += "v" + str(i) + " + "
        for i in range(len(x2)):
            s = s.replace("- delta", "+ x" + str(i) + " - y" + str(i), 1)
            z += "x" + str(i) + " + "
        s = s.replace("delta = 0", "")
    s = z+s
    
    return s + "\nend"