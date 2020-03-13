import newton_method as nm
import chord_method as cm
import dichotomy_method as dm

# You can change function in modules

def is_digit(str):
    if str.isdigit():
       return True
    else:
        try:
            float(str)
            return True
        except ValueError:
            return False   
            
print("Input the borders of section")
a = input(); b = input()
print("Input accuracy")
e = input()
if (is_digit(a) and is_digit(b) and is_digit(e)):
    a = float(a); b = float(b); e = float(e)
else:
    print("Wrong input. Try again..")
    raise SystemExit('ValueError')
NM = nm.NewtonMethod(); CM = cm.ChordMethod(); DM = dm.DichotonomyMethod()
print(F'NewtonMethod = {round(NM.get_result(a,b,e),10)} | DichotonomyMethod = {DM.get_result(a,b,e)} | ChordMethod = {round(CM.get_result(a,b,e),10)}')