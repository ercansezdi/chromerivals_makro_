import win32api # if active state python is installed or install pywin32 package seperately

try: win32api.WinExec('C:\\Users\\ercan\\Desktop\\test_\\update\\dist\\update_func\\updater.exe') # Works seamlessly
except: pass