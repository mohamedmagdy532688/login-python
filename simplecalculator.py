from pystyle import *

print(Box.Lines("[+] development by: Mohamed Magdy [+]"))
Write.Print("[+] this program for simple calculator \n", Colors.purple_to_red, interval= 0.1)
print(Box.DoubleCube("Example [3]"))

while True:
    number = int(Write.Input("write number:", Colors.purple_to_blue, interval= 0.1))
    for i in range(1, 11):
        print(number, "x" , i, "=", number * i)

    input('\n press any kay to exit ...')