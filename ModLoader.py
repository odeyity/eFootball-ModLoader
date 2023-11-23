import shutil
import os
import sys

modPak = ['pc0101_console_win.pak', 'pc0101_console_win.ucas', 'pc0101_console_win.utoc',
          'pc7000_console_win.pak', 'pc7000_console_win.ucas', 'pc7000_console_win.utoc']
modCpk = ['dt200_console_all.cpk']
modExe = ['d3d10core.dll', 'd3d11.dll', 'd3d9.dll', 'dxgi.dll', 'dxgi.log', 'eFootball-FPS-Limit-Patcher.exe',
          'imgui.ini', 'UE4SS-settings.ini']

ef_dir = "D:\SteamLibrary\steamapps\common\eFootball"
pak_dir = ef_dir + "\pak"
cpk_dir = ef_dir + "\cpk"
exe_dir = ef_dir + "\eFootball\Binaries\Win64"

modded_fol = os.listdir("Modded")
modded_fol.remove("pak")
modded_fol.remove("cpk")
modded_fol.remove("exe")
print(modded_fol)

print("(1) Vanilla")
print("(2) Modded")
opt = input()

if  opt == "1":
    print("Switching to vanilla profile")
else:
    print("Switching to modded profile")

if opt == "1":
    print("------------------------")
    print("Status> Checking .pak files")
    print("------------------------")
    ef_list = os.listdir(pak_dir)
    for i in range(len(ef_list)):
        if ef_list[i] in modPak:
            mod = ef_list[i]
            modLoc = pak_dir + "\\" + mod
            print("Detected:", mod, "is a modded file")
            print("Moving:", mod)
            shutil.move(modLoc, "Modded\pak")
            modLoc = "Vanilla\pak\\" + mod
            shutil.move(modLoc, pak_dir)
    print("------------------------")
    print("Status> Checking .cpk files")
    print("------------------------")
    ef_list = os.listdir(cpk_dir)
    for i in range(len(ef_list)):
        if ef_list[i] in modCpk:
            mod = ef_list[i]
            modLoc = cpk_dir + "\\" + mod
            print("Detected:", mod, "is a modded file")
            print("Moving:", mod)
            shutil.move(modLoc, "Modded\cpk")
            modLoc = "Vanilla\cpk\\" + mod
            shutil.move(modLoc, cpk_dir)
    print("------------------------")
    print("Status> Checking .exe files")
    print("------------------------")
    ef_list = os.listdir(exe_dir)
    for i in range(len(ef_list)):
        if ef_list[i] in modExe:
            mod = ef_list[i]
            modLoc = exe_dir + "\\" + mod
            print("Detected:", mod, "is a modded file")
            print("Moving:", mod)
            shutil.move(modLoc, "Modded\exe")
else:
    print("------------------------")
    print("Status> Checking .pak files")
    print("------------------------")
    ef_list = os.listdir(pak_dir)
    for i in range(len(ef_list)):
        if ef_list[i] in modPak:
            mod = ef_list[i]
            modLoc = pak_dir + "\\" + mod
            print("Detected:", mod, "is a vanilla file")
            print("Moving:", mod)
            shutil.move(modLoc, "Vanilla\pak")
            modLoc = "Modded\pak\\" + mod
            shutil.move(modLoc, pak_dir)
    print("------------------------")
    print("Status> Checking .cpk files")
    print("------------------------")
    ef_list = os.listdir(cpk_dir)
    for i in range(len(ef_list)):
        if ef_list[i] in modCpk:
            mod = ef_list[i]
            modLoc = cpk_dir + "\\" + mod
            print("Detected:", mod, "is a modded file")
            print("Moving:", mod)
            shutil.move(modLoc, "Vanilla\cpk")
            modLoc = "Modded\cpk\\" + mod
            shutil.move(modLoc, cpk_dir)
    print("------------------------")
    print("Status> Checking .exe files")
    print("------------------------")
    ef_list = os.listdir("Modded\exe")
    for i in range(len(ef_list)):
        mod = ef_list[i]
        modLoc = "Modded\exe\\" + mod
        print("Detected:", mod, "is a modded file")
        print("Moving:", mod)
        shutil.move(modLoc, exe_dir)
            
