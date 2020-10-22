import pyautogui
import math
# Quadratic Formula = ( -b +/- sqrt(b^2 - 4 * a * c) )/(2*a)

pyautogui.alert('This program will take a quadratic in the form of [ax^2 + bx + c] and give you the values of x.')
# Get inputs for each variable from user, as well as store as strings for later use
var_a = pyautogui.prompt('[ax^2 + bx + c] Please give a value for "a"')
var_b = pyautogui.prompt('[ax^2 + bx + c] Please give a value for "b"')
var_c = pyautogui.prompt('[ax^2 + bx + c] Please give a value for "c"')
print('var info:')
print("a b c= " + var_a + " " + var_b + " " + var_c)

# Convert answers into integers for calculation
int_a = int(var_a)
int_b = int(var_b)
int_c = int(var_c)
print("int test: a+b+c= " + str(int_a + int_b + int_c))

# --Calculation for x1

bneg = int_b - int_b - int_b
bsqr = int_b * int_b
print("bneg= " + str(bneg))
print("bsqr= " + str(bsqr))

sqrtcalc = math.sqrt(bsqr - 4 * int_a * int_c)
print("sqrtcalc= " + str(sqrtcalc))

fractop1 = bneg + sqrtcalc
fractop2 = bneg - sqrtcalc
fracbot = 2 * int_a

x1 = fractop1 / fracbot
x2 = fractop2 / fracbot
print("x= " + str(x1) + ' ' + str(x2))

pyautogui.alert('x is equal to: ' + str(x1) + ' & ' + str(x2))
