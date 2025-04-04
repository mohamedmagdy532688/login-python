from pystyle import *

print(Box.Lines("[+] development by: Mohamed Magdy [+]"))
Write.Print("[+] this program for login page \n", Colors.purple_to_red, interval= 0.1)
Write.Print("[+] write username and password \n\n", Colors.purple_to_red, interval= 0.1)
print(Box.DoubleCube("Example [1]"))

while True: 
    username = Write.Input("write username:",Colors.blue_to_green, interval= 0.1) 
    password = Write.Input("Write password:",Colors.blue_to_green, interval= 0.1)

    if username == "magdy" and password == "123456":
        Write.Print("[+] welocme admin \n", Colors.green, interval= 0.1)
        input('\n press any kay to exit ...')
    else:
        Write.Print("[-] Error try again \n\n", Colors.red, interval= 0.1)

