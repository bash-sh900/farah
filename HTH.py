import sys
import os
import time
import random
##########################################################################################################
co=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[35m','\033[1;36m','\033[1;37m','\033[1;38m']
#########################################################################################################
def jalan(z):
    for e in z+'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.01)
######################################################
time.sleep(0.7)
os.system('clear')
jalan("\033[1;36m_____________")
jalan("\033[1;32m┈┈┈╲┈┈┈┈╱   \033[1;36m |")
jalan("\033[1;32m┈┈┈╱▔▔▔▔╲   \033[1;36m |")
jalan("\033[1;32m┈┈┃┈▇┈┈▇┈┃  \033[1;36m |")
jalan("\033[1;32m╭╮┣━━━━━━┫╭╮\033[1;36m |")
jalan("\033[1;32m┃┃┃┈┈┈┈┈┈┃┃┃\033[1;36m |")
jalan("\033[1;32m╰╯┃┈┈┈┈┈┈┃╰╯\033[1;36m |")
jalan("\033[1;32m┈┈╰┓┏━━┓┏╯  \033[1;36m |")
jalan("\033[1;32m┈┈┈╰╯┈┈╰╯   \033[1;36m |")
jalan("\033[1;36m_____________")
jalan("\033[1;32m______________________________")
####################################################################
def list():
    print(" \033[1;36m[1] \033[1;34mInstall all pkg termux | ")
    time.sleep(0.3)
    print(" \033[1;36m[2] \033[1;34mHack camira            | ")
    time.sleep(0.3)
    print(" \033[1;36m[3] \033[1;34mVirus 4                | ")
    time.sleep(0.3)
    print(" \033[1;36m[4] \033[1;34mInstall hammer         | ")
    time.sleep(0.3)
    print(" \033[1;36m[5] \033[1;34mHack android           | ")
    time.sleep(0.3)
    print(" \033[1;36m[6] \033[1;34minstall voice          | ")
    time.sleep(0.3)
    print(" \033[1;36m[0] \033[1;34mExit                   | ")
    jalan("\033[1;32m______________________________")

list()
print(random.choice(co))
i=input("︻╦̴╦═─ : ")
if i=='1':
    os.system('cd ~ ; pkg upgate -y ; pkg upgrade -y ; pkg install python -y ; pkg install git -y ; pkg install figlet ; git clone https://github.com/khalid-bx/pkg-termux ; cd pkg-termux ; bash pkg.sh')
elif i=='2':
    os.system('cd ~ ; pkg update ; pkg upgrade ; pkg install python -y ; pkg install git -y ; git clone https://github.com/AngelSecurityTeam/Cam-Hackers ; pip install requests ; pip install colorama ; cd Cam-Hackers ; python3 cam-hackers.py')
elif i=='3':
    os.system('cd ~ ; pkg update ; pkg upgrade ; pkg install python2 -y ; pkg install git -y ; git clone https://github.com/ERROR4317/viruscreater ; cd viruscreater ; python2 virus.py')
elif i=='3':
    os.system('cd ~ ; pkg update ; pkg upgrade ; pkg install python2 -y ; pkg install git -y ; git clone https://github.com/ERROR4317/viruscreater ; cd viruscreater ; python2 virus.py')
elif i=='4':
    os.system('cd ~ ; apt update ; apt upgrade ; pkg install python2 ; pkg install git ; git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING ; cd LEDEAR_HACKING ; chmod 777 * ; python2 ledearhacking.py')
elif i=='5':
    os.system('cd ~ ;  pkg update ; pkg upgrade -y ; pkg install git -y ; pkg install python -y ; termux-setup-storage -y ; pip install gTTS ; git clone https://github.com/khalid-bx/voice ; cd voice ; python voice.py')
elif i=='0':
    os.system('exit')
else:
    os.system('python farah.py')
