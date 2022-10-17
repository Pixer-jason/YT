import os 
import pytube
#import tqdm
#from pathlib import Path
import time

os.system("clear")
def greetings():
    print("""\033[1;34;40m
██╗   ██╗████████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝    ██║       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
  ╚██╔╝     ██║       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
   ██║      ██║       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
   ╚═╝      ╚═╝       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """)
    print("\033[1;31;40m\t\t\tDeveloped By Pixer Jason\n")
    print("\033[1;33;40mInsipred By TripleHat\n")

greetings()

print("\033[1;37;40m1.Download 1080p Video\n")
print("2.Download 720p Video\n")
print("3.Change Dirrectory\n")
ingiza = input("Select Your Option: " + "\n")

for i in range (3):
    print("Please wait... ", i)
    time.sleep(1)
    os.system("clear")
    i=i+1

if ingiza == '1':
    lv = input("Enter YouTube URL For 1080p: ")
    time.sleep(3)
    dwn = pytube.YouTube(lv)
    print("Downloading..\../..\../\n")
    bangi = dwn.streams.get_highest_resolution().download(print("Finalizing..........\n"))
    print("Downloaded........... 100%", lv)
    print(bangi + "\n")


elif ingiza == '2':
    lv = input("Enter YouTube URL For 720pp: ")
    time.sleep(3)
    dwn = pytube.YouTube(lv)
    print("Downloading..\../..\../\n")
    bangi = dwn.streams.get_highest_resolution().download(print("Finalizing..........\n"))
    print("Downloaded........... 100%", lv)
    print(bangi + "\n")

elif ingiza == '3':
    print("\033[1;31;40mOops! There's Nothing Up Here!\n")
    exit
