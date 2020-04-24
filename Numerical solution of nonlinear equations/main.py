import newton_method as nm
import chord_method as cm
import dichotomy_method as dm

# You can change function in modules

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False   

while True:
    print("1 -> Input or change borders, 2 -> Output result 0 -> Exit")
    choose = input()
    if(choose == "1"):
        print("Input the borders of section")
        a = input(); b = input()
        print("Input accuracy")
        e = input()
        if (is_digit(a) and is_digit(b) and is_digit(e)):
            a = float(a); b = float(b); e = float(e)
        else:
            print("Wrong input. Try again..")
            raise SystemExit('ValueError')
    elif(choose == "2" and 'a' in locals()):
        NM = nm.NewtonMethod(); CM = cm.ChordMethod(); DM = dm.DichotonomyMethod()
        print(F"NewtonMethod = {NM.get_result(a,e)} | DichotonomyMethod = {DM.get_result(a,b,e)} | ChordMethod = {CM.get_result(a,b,e)}")
    elif(choose == "0"):
        break
    else:
        if('a' not in locals()):
            print("Use 1 to input borders before output results")
        else:
            print("Wrong number")