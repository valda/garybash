import os, string, win32api, win32con
path = None
blenderpath = None
stext = "blenderpathold"

try:
    keyHandle = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, "SOFTWARE\\Bethesda Softworks\\Fallout3", 0, win32con.KEY_ALL_ACCESS)
    path, typeId = win32api.RegQueryValueEx(keyHandle, "Installed Path")
    win32api.RegCloseKey(keyHandle)
except Exception, e:
    try:
       keyHandle = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Bethesda Softworks\\Fallout3", 0, win32con.KEY_ALL_ACCESS)
       path, typeId = win32api.RegQueryValueEx(keyHandle, "Installed Path")
       win32api.RegCloseKey(keyHandle)
    except Exception, e:
        print "ReadRegistryValue failed:", e

try:
    keyHandle = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, "SOFTWARE\\BlenderFoundation", 1, win32con.KEY_ALL_ACCESS)
    blenderpath, typeId = win32api.RegQueryValueEx(keyHandle, "Install_Dir")
    win32api.RegCloseKey(keyHandle)
    print blenderpath
    blenderpath.join('blender.exe')
    blenderpath = blenderpath + '\\Blender.exe'
    print blenderpath
except Exception, e:
    print "ReadRegistryValue failed:", e

rtext = blenderpath
print rtext
filename = path + "\\Mopy\\bosh.py"
inputFile = file(filename, 'r')
data = inputFile.read()
inputFile.close()
data = data.replace(stext, rtext)
outputFile = file(filename, 'w')
outputFile.write(data)
outputFile.close()
