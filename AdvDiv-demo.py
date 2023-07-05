import re
import AdvDiv

number1 = input("N1: ")
number2 = input("N2: ")
print(AdvDiv.div(float(re.sub("^\\.", "0.", number1.split("[")[0]).rstrip(".")), float(re.sub("^\\.", "0.", number2.split("[")[0]).rstrip(".")), int(number1.split("[")[1].rstrip("]")) if "[" in number1 else 0, int(number2.split("[")[1].rstrip("]")) if "[" in number2 else 0))
input()
