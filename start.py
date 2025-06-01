import os
import sys
import subprocess
import importlib
import time

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    
    @staticmethod
    def print_colored(message, color_type, delay=0.5):
        if color_type == "error":
            print(f"{Colors.RED}{message}{Colors.RESET}")
        elif color_type == "success":
            print(f"{Colors.GREEN}{message}{Colors.RESET}")
        elif color_type == "info":
            print(f"{Colors.YELLOW}{message}{Colors.RESET}")
        else:
            print(message)
        time.sleep(delay)

def check_python():
    try:
        python_version = sys.version
        Colors.print_colored(f"[INFO] Python found: {python_version.split()[0]}", "info", 0.8)
        return True
    except Exception:
        Colors.print_colored("[ERROR] Python not found in the system!", "error", 1.0)
        print("Install Python from https://python.org")
        time.sleep(1.0)
        return False

def check_library(library_name):
    Colors.print_colored(f"[CHECK] Check. {library_name}...", "info", 0.6)
    try:
        importlib.import_module(library_name)
        Colors.print_colored(f"[OK] {library_name} already installed", "success", 0.5)
        return True
    except ImportError:
        Colors.print_colored(f"[MISSING] {library_name} not installed", "error", 0.5)
        return False

def install_library(library_name):
    print(f"[INSTALL] Installation {library_name}...")
    time.sleep(0.3)
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "install", library_name], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            Colors.print_colored(f"[SUCCESS] {library_name} successfully installed", "success", 0.8)
            return True
        else:
            Colors.print_colored(f"[ERROR] Unable to install {library_name}", "error", 1.0)
            print("Check internet connection or permissions")
            time.sleep(1.0)
            return False
    except subprocess.TimeoutExpired:
        Colors.print_colored(f"[ERROR] Timeout during installation of {library_name}", "error", 1.0)
        return False
    except Exception as e:
        Colors.print_colored(f"[ERROR] Error in installation: {str(e)}", "error", 1.0)
        return False

def check_main_file():
    if os.path.exists("main.py"):
        Colors.print_colored("[INFO] File main.py found", "info", 0.5)
        return True
    else:
        Colors.print_colored("[ERROR] File main.py not found in current directory!", "error", 1.0)
        print("Make sure main.py is in the same folder as this script")
        time.sleep(1.0)
        return False

def launch_main():
    Colors.print_colored("[INFO] Starting IP Address Finder...", "info", 1.0)
    
    try:
        result = subprocess.run([sys.executable, "main.py"], check=False)
        if result.returncode != 0:
            print()
            Colors.print_colored("[ERROR] The application closed with an error.", "error", 1.0)
            return False
        return True
    except Exception as e:
        print()
        Colors.print_colored(f"[ERROR] Unable to start the application: {str(e)}", "error", 1.0)
        return False

def main():
    os.system("title IP Address Finder - Startup")
    
    print()
    print("================================")
    print("   IP Address Finder")
    print("   Automatic startup...")
    print("================================")
    print()
    time.sleep(1.0)
    
    if not check_python():
        input("\nPress ENTER to exit...")
        sys.exit(1)
    
    print()
    Colors.print_colored("[INFO] Dependencies control...", "info", 0.8)
    print()

    required_libraries = ["requests", "pyperclip"]
    missing_libraries = []

    for library in required_libraries:
        if not check_library(library):
            missing_libraries.append(library)
    
    print()
    
    if missing_libraries:
        Colors.print_colored("[INFO] Installing missing dependencies...", "info", 1.0)
        print()
        
        for library in missing_libraries:
            if not install_library(library):
                input("\nPress ENTER to exit...")
                sys.exit(1)
            print()
        
        Colors.print_colored("[SUCCESS] All dependencies have been installed!", "success", 1.0)
        print()
    else:
        Colors.print_colored("[INFO] All dependencies are already installed", "info", 1.0)
        print()
    
    if not check_main_file():
        input("\nPress ENTER to exit...")
        sys.exit(1)
    
    print()
    
    success = launch_main()
    
    print()
    if success:
        Colors.print_colored("[INFO] Application closed normally", "info", 0.5)
    
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        Colors.print_colored("[INFO] Startup interrupted by user", "info", 0.5)
        sys.exit(0)
    except Exception as e:
        print()
        Colors.print_colored(f"[ERROR] Unexpected error: {str(e)}", "error", 1.0)
        input("\nPress ENTER to exit...")
        sys.exit(1)