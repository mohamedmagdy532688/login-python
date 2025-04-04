from pystyle import *

print(Box.Lines("[+] development by: Mohamed Magdy [+]"))
Write.Print("[+] this program for calculator \n", Colors.purple_to_red, interval= 0.1)
print(Box.DoubleCube("Example [2]"))

while True:
    number1 = int(Write.Input("write first number:", Colors.blue_to_green, interval= 0.1))
    operator = Write.Input("write operator:", Colors.blue_to_green, interval= 0.1)
    number2 = int(Write.Input("write second number:", Colors.blue_to_green, interval= 0.1))

    if operator == "+":
        Write.Print("[+] the result is : ", Colors.green, interval = 0.1)
        print(number1 + number2)
        input('\n press any kay to exit ...')
        break
    elif operator == "-":
        Write.Print("[+] the result is : ", Colors.green, interval = 0.1)
        print(number1 - number2)
        input('\n press any kay to exit ...')
        break
    elif operator == "*":
        Write.Print("[+] the result is : ", Colors.green, interval = 0.1)
        print (number1 * number2)
        input('\n press any kay to exit ...')
        break
    elif operator == "/":
        Write.Print("[+] the result is : ", Colors.green, interval = 0.1)
        print (number1 / number2)
        input('\n press any kay to exit ...')
        break
    else:
        Write.Print("\n [-] please write just : + - * / \n", Colors.red, interval = 0.1)
        input('\n press any kay to exit ...')