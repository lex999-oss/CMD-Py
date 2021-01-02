import os
import sys
import winreg

if sys.argv[1] == "list_dir":
    if len(sys.argv) < 3:
        print("Not enough parameters to execute command")
        print("Usage: list_dir <dir>")
    elif len(sys.argv) > 3:
        print("Too many parameters to execute command")
        print("Usage: list_dir <dir>")
    elif sys.argv[2] == "help":
        print("List the contents if <dir> folder\n"
              "Usage: list_dir <dir>")
    else:
        os.system("dir {}".format(sys.argv[2]))
if sys.argv[1] == "move_dir":
    if len(sys.argv) < 3:
        print("Not enough parameters to execute command")
        print("Usage: move_dir <dir1> <dir2>")
    elif len(sys.argv) > 4:
        print("Too many parameters to execute command")
        print("Usage: move_dir <dir1> <dir2>")
    elif sys.argv[2] == "help":
        print("Move <dir1> to <dir2>\n"
              "Usage: move_dir <dir1> <dir2>")
    else:
        os.system("move {} {}".format(sys.argv[2], sys.argv[3]))

if sys.argv[1] == "create_key":
    if len(sys.argv) < 3:
        print("Not enough parameters to execute command")
        print("Usage: create_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")
    elif len(sys.argv) > 4:
        print("Too many parameters to execute command")
        print("Usage: create_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")
    elif sys.argv[2] == "help":
        print("Create a new registry key in <HKEY_* CONSTANT>\n"
              "Elevated administrator shell required!\n"
              "Usage: create_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")
    else:
        if sys.argv[2] == "HKEY_CLASSES_ROOT":
            try:
                winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_CLASSES_ROOT\\{} created successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_CURRENT_USER":
            try:
                winreg.CreateKey(winreg.HKEY_CURRENT_USER, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_CURRENT_USER\\{} created successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_LOCAL_MACHINE":
            try:
                winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_LOCAL_MACHINE\\{} created successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_USERS":
            try:
                winreg.CreateKey(winreg.HKEY_USERS, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_USERS\\{} created successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_PERFORMANCE_DATA":
            try:
                winreg.CreateKey(winreg.HKEY_PERFORMANCE_DATA, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_PERFORMANCE_DATA\\{} created successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_CURRENT_CONFIG":
            try:
                winreg.CreateKey(winreg.HKEY_CURRENT_CONFIG, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_CURRENT_CONFIG\\{} created successfully!\n".format(sys.argv[3]))
        else:
            print("Unsupported HKEY_* Constant!")
            print("Usage: create_key <HKEY_* CONSTANT>["
                  "HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS "
                  "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")

if sys.argv[1] == "delete_key":
    if len(sys.argv) < 3:
        print("Not enough parameters to execute command")
        print("Usage: delete_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <KEY_NAME>")
    elif len(sys.argv) > 4:
        print("Too many parameters to execute command")
        print("Usage: delete_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <KEY_NAME>")
    elif sys.argv[2] == "help":
        print("Remove registry key in <HKEY_* CONSTANT>\n"
              "Elevated administrator shell required!\n"
              "Usage: delete_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <KEY_NAME>")
    else:
        if sys.argv[2] == "HKEY_CLASSES_ROOT":
            try:
                winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_CLASSES_ROOT\\{} deleted successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_CURRENT_USER":
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_CURRENT_USER\\{} deleted successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_LOCAL_MACHINE":
            try:
                winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_LOCAL_MACHINE\\{} deleted successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_USERS":
            try:
                winreg.DeleteKey(winreg.HKEY_USERS, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_USERS\\{} deleted successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_PERFORMANCE_DATA":
            try:
                winreg.DeleteKey(winreg.HKEY_PERFORMANCE_DATA, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_PERFORMANCE_DATA\\{} deleted successfully!\n".format(sys.argv[3]))
        elif sys.argv[2] == "HKEY_CURRENT_CONFIG":
            try:
                winreg.DeleteKey(winreg.HKEY_CURRENT_CONFIG, sys.argv[3])
            except OSError as err:
                print(err)
                exit(0)
            print("Registry key HKEY_CURRENT_CONFIG\\{} deleted successfully!\n".format(sys.argv[3]))
        else:
            print("Unsupported HKEY_* Constant!")
            print("Usage: delete_key <HKEY_* CONSTANT>["
                  "HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS "
                  "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")

if sys.argv[1] == "modify_key":
    if len(sys.argv) < 3:
        print("Not enough parameters to execute command")
        print("Usage: modify_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")
    elif len(sys.argv) > 4:
        print("Too many parameters to execute command")
        print("Usage: modify_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <NEW_KEY_NAME>")
    elif sys.argv[2] == "help":
        print("Modify key in <HKEY_* CONSTANT>\n"
              "Elevated administrator shell required!\n"
              "Usage: delete_key <HKEY_* CONSTANT>[HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS"
              "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <KEY_NAME>")
    else:
        if sys.argv[2] == "HKEY_CLASSES_ROOT":
            try:
                key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, sys.argv[3], 0, winreg.KEY_ALL_ACCESS)
            except OSError as err:
                print(err)
                exit(0)
            print("Values of HKEY_CLASSES_ROOT\\{} key:\n".format(sys.argv[3]))
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                print (winreg.EnumValue(key, i))
            value_name = input("Insert the name of the value you want to modify/create: ")
            print("Value types: [STRING|INTEGER]\n")
            value_type = input("Insert the type of the value you want to modify/create: ")
            value_data = 0
            if value_type == "STRING":
                value_type = winreg.REG_SZ
                value_data = input("Insert the string data of the value you want to modify/create: ")
            elif value_type == "INTEGER":
                value_type = winreg.REG_DWORD
                value_data = int(input("Insert the string data of the value you want to modify/create: "))
            else:
                print("Invalid data type!\n")
            try:
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            except OSError as err:
                print(err)
                exit(0)
            winreg.CloseKey(key)
        elif sys.argv[2] == "HKEY_CURRENT_USER":
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, sys.argv[3], 0, winreg.KEY_ALL_ACCESS)
            except OSError as err:
                print(err)
                exit(0)
            print("Values of HKEY_CURRENT_USER\\{} key:\n".format(sys.argv[3]))
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                print(winreg.EnumValue(key, i))
            value_name = input("Insert the name of the value you want to modify/create: ")
            print("Value types: [STRING|INTEGER]\n")
            value_type = input("Insert the type of the value you want to modify/create: ")
            value_data = 0
            if value_type == "STRING":
                value_type = winreg.REG_SZ
                value_data = input("Insert the string data of the value you want to modify/create: ")
            elif value_type == "INTEGER":
                value_type = winreg.REG_DWORD
                value_data = int(input("Insert the string data of the value you want to modify/create: "))
            else:
                print("Invalid data type!\n")
            try:
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            except OSError as err:
                print(err)
                exit(0)
            winreg.CloseKey(key)
        elif sys.argv[2] == "HKEY_LOCAL_MACHINE":
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sys.argv[3], 0, winreg.KEY_ALL_ACCESS)
            except OSError as err:
                print(err)
                exit(0)
            print("Values of HKEY_LOCAL_MACHINE\\{} key:\n".format(sys.argv[3]))
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                print(winreg.EnumValue(key, i))
            value_name = input("Insert the name of the value you want to modify/create: ")
            print("Value types: [STRING|INTEGER]\n")
            value_type = input("Insert the type of the value you want to modify/create: ")
            value_data = 0
            if value_type == "STRING":
                value_type = winreg.REG_SZ
                value_data = input("Insert the string data of the value you want to modify/create: ")
            elif value_type == "INTEGER":
                value_type = winreg.REG_DWORD
                value_data = int(input("Insert the string data of the value you want to modify/create: "))
            else:
                print("Invalid data type!\n")
            try:
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            except OSError as err:
                print(err)
                exit(0)
            winreg.CloseKey(key)
        elif sys.argv[2] == "HKEY_USERS":
            try:
                key = winreg.OpenKey(winreg.HKEY_USERS, sys.argv[3], 0, winreg.KEY_ALL_ACCESS)
            except OSError as err:
                print(err)
                exit(0)
            print("Values of HKEY_USERS\\{} key:\n".format(sys.argv[3]))
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                print(winreg.EnumValue(key, i))
            value_name = input("Insert the name of the value you want to modify/create: ")
            print("Value types: [STRING|INTEGER]\n")
            value_type = input("Insert the type of the value you want to modify/create: ")
            value_data = 0
            if value_type == "STRING":
                value_type = winreg.REG_SZ
                value_data = input("Insert the string data of the value you want to modify/create: ")
            elif value_type == "INTEGER":
                value_type = winreg.REG_DWORD
                value_data = int(input("Insert the string data of the value you want to modify/create: "))
            else:
                print("Invalid data type!\n")
            try:
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            except OSError as err:
                print(err)
                exit(0)
            winreg.CloseKey(key)
        elif sys.argv[2] == "HKEY_PERFORMANCE_DATA":
            try:
                key = winreg.OpenKey(winreg.HKEY_PERFORMANCE_DATA, sys.argv[3], 0, winreg.KEY_ALL_ACCESS)
            except OSError as err:
                print(err)
                exit(0)
            print("Values of HKEY_PERFORMANCE_DATA\\{} key:\n".format(sys.argv[3]))
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                print(winreg.EnumValue(key, i))
            value_name = input("Insert the name of the value you want to modify/create: ")
            print("Value types: [STRING|INTEGER]\n")
            value_type = input("Insert the type of the value you want to modify/create: ")
            value_data = 0
            if value_type == "STRING":
                value_type = winreg.REG_SZ
                value_data = input("Insert the string data of the value you want to modify/create: ")
            elif value_type == "INTEGER":
                value_type = winreg.REG_DWORD
                value_data = int(input("Insert the string data of the value you want to modify/create: "))
            else:
                print("Invalid data type!\n")
            try:
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            except OSError as err:
                print(err)
                exit(0)
            winreg.CloseKey(key)
        elif sys.argv[2] == "HKEY_CURRENT_CONFIG":
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, sys.argv[3], 0, winreg.KEY_ALL_ACCESS)
            except OSError as err:
                print(err)
                exit(0)
            print("Values of HKEY_CURRENT_CONFIG\\{} key:\n".format(sys.argv[3]))
            for i in range(0, winreg.QueryInfoKey(key)[1]):
                print(winreg.EnumValue(key, i))
            value_name = input("Insert the name of the value you want to modify/create: ")
            print("Value types: [STRING|INTEGER]\n")
            value_type = input("Insert the type of the value you want to modify/create: ")
            value_data = 0
            if value_type == "STRING":
                value_type = winreg.REG_SZ
                value_data = input("Insert the string data of the value you want to modify/create: ")
            elif value_type == "INTEGER":
                value_type = winreg.REG_DWORD
                value_data = int(input("Insert the string data of the value you want to modify/create: "))
            else:
                print("Invalid data type!\n")
            try:
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
            except OSError as err:
                print(err)
                exit(0)
            winreg.CloseKey(key)

        else:
            print("Unsupported HKEY_* Constant!")
            print("Usage: modify_key <HKEY_* CONSTANT>["
                  "HKEY_CLASSES_ROOT|HKEY_CURRENT_USER|HKEY_LOCAL_MACHINE|HKEY_USERS "
                  "|HKEY_PERFORMANCE_DATA|HKEY_CURRENT_CONFIG] <KEY_NAME>")
