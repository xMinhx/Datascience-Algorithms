import string
#Beispiel für function Parameter: x^2 + x + c -> ["c", "x", x**2]
#Beispiel für bounds Parameter: a >= 0, b <= 0, c ist Frei -> ["a >= 0", "b <= 0", "free"]
def create_lp_ausgleich(function: [str], bounds: [str], x: [float], y: [float], typ="minimize") -> str:
 #Konstanten Initialisierung
 function[0] = ""
 
 #Prüft ob minimize oder maximize gewählt wurde
 if typ not in ["minimize","maximize"]:
 return "Ungültiger Typ"
 s = typ + "\n\t"
 
 #Generiert die zu minimierende Funktion
 for i in range(0, len(x)):
 s += "u" + str(i) + " + " + "v" + str(i) + " + " 
 s = s[:-2]
 
 #Generiert die Nebenbedingungen anhand der X und Y Werte
 s += "\n\nsubject to\n"
 for i in range(len(x)):
 copy_function = list(function)
 tmp = "\t"
 for j in range(len(copy_function)):
 value = ""
 if (copy_function[j] != ""):
 value = str(eval(copy_function[j].replace("x", str(x[i]))))
 tmp += value + " " + string.ascii_lowercase[j].replace("e", "") + " + "
 tmp += "u" + str(i) + " - " + "v" +str(i) +" = " + str(y[i]) +"\n"
 s+=tmp
 
 #Generiert die Rahmenbedingungen der Variablen
 s += "\nbounds\n\t"
 for i in range(len(bounds)):
 s += string.ascii_lowercase[i] +" " + bounds[i] + "\n\t"
 return s + "\nend"