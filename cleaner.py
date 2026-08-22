import subprocess
import ctypes
import os
import time
import shutil

print("--- Hello, im a cleaner! ---\n")

def get_free_space():
    total, used, free = shutil.disk_usage("C:")
    return free

space_before = get_free_space()

user_profile = os.environ.get("USERPROFILE")
local_appdata = os.environ.get("LOCALAPPDATA")

paths = {
    "Download": f"{user_profile}/Downloads/*",
    "Temp": "C:/Temp/*",
    "Windows/Temp": "C:/Windows/Temp/*",
    "AppData/Temp": f"{local_appdata}/Temp/*",
}

sel = input("--- Clean Recycle Bin? (Y/N): ").strip().lower() == "y"

print("\n---> Start clean <---\n")

for name, folder_path in paths.items():
    print(f"---> Cleaning {name}")
    subprocess.run(["powershell", "-Command", f"Remove-Item -Path '{folder_path}' -Recurse -Force -ErrorAction SilentlyContinue"])

if sel:
    print("\nEmptying Recycle Bin...")
    ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 7)
    print("\n--- Clean finish! ---")
else:
    print("\n--- Clean finish! ---")

space_after = get_free_space()
bytes_cleaned = space_after - space_before

if bytes_cleaned > 0:
    mb_cleaned = bytes_cleaned / (1024*1024)
    if mb_cleaned >= 1024:
        gb_cleaned = mb_cleaned / 1024
        print(f"Освобождено {gb_cleaned} ГБ")
    else:
        print(f"Освобождено {mb_cleaned} МБ")

time.sleep(3)