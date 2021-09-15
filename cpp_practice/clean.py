#!/usr/bin/python
import os
import sys
import platform


current_OS = platform.system()

os.chdir("build")
os.system("rm -rf *")
print(str(sys.argv[-1]))


#if you wanna force it to run a certain way, here you go.
if sys.argv[-1] == "linux":
    os.system("cmake ..")
    os.system("make")
elif sys.argv[-1] == "mac":
    os.system("cmake .. -G Xcode")
    os.system("make")
elif sys.argv[-1] == "win":
    os.system('cmake .. -G"Visual Studio 16 2019"')

# else, just run what is native on the system.
else:
    if current_OS == "Darwin":
        os.system("cmake .. -G Xcode")
    elif current_OS == "Windows":
        os.system('cmake .. -G"Visual Studio 16 2019"')
    else:
        os.system("cmake ..")
        os.system("make")



os.chdir("..")
