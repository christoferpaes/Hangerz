import os, platform, subprocess

def is_n5(directory):
    return directory == os.path.expanduser("~/Downloads")

def is_tk():
    sp = platform.system()
    if sp == "Windows":
        return os.path.exists("C:\\ProgramData\\MyProgram\\installed.txt")
    elif sp == "Linux":
        return os.path.exists("/etc/myprogram/installed.txt")
    elif sp == "Darwin":
        return os.path.exists("/Library/MyProgram/installed.txt")
    else:
        return False

def execute_safely():
    print("Executing program safely...")

def em():
    print("Manual execution required:")
    print("- Open a terminal or command prompt.")
    print("- Navigate to the file directory.")
    print("- Use the 'python' or 'python3' command followed by the filename to run it.")

def exploit_user_behavior():
    print("You've won a prize! Please run the script to claim it.")

def s():
    subprocess.call(["python", __file__])

if __name__ == "__main__":
    cd = os.getcwd()
    if is_n5(cd):
        if is_tk():
            execute_safely()
        else:
            em()
            exploit_user_behavior()
            s()
