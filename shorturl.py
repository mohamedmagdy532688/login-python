from pystyle import *
import pyshorteners as short
print(Box.Lines("[+] development by: Mohamed Magdy [+]"))
Write.Print("[+] this program for short url \n", Colors.purple_to_red, interval= 0.1)
print(Box.DoubleCube("Example [4]"))

url = Write.Input("write url:", Colors.blue_to_green, interval= 0.1)
sh = short.Shortener()
Write.Print(sh.tinyurl.short(url), Colors.green, interval= 0.3)
input('\n press any kay to exit ...')