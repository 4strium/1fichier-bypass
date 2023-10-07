import subprocess
import time

def disable_ethernet():
    try:
        subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "admin=disable"])
        print("Ethernet connection disabled.")
    except Exception as e:
        print(f"Error occurred: {e}")

def enable_ethernet():
    try:
        subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "admin=enable"])
        print("Ethernet connection enabled.")
    except Exception as e:
        print(f"Error occurred: {e}")

def close_app():
    try:
        subprocess.run(["taskkill", "/IM", "JDownloader2.exe", "/F"])
        print("App successfully closed.")
    except Exception as e:
        print(f"Error occurred: {e}")

def open_app():
    try:
        subprocess.run(["C:\Program Files\JDownloader\JDownloader2.exe"])
        print("App successfully opened.")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    time.sleep(2)
    disable_ethernet()
    time.sleep(4)
    enable_ethernet()
    time.sleep(2)
    close_app()
    time.sleep(5)
    open_app()

if __name__ == "__main__":
    main()