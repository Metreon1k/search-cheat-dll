import os
import sys
import time

# Конфигурация
TARGET = b"net/minecraft/util/math/AxisAlignedBB"
EXTS = (".dll", ".exe", ".jar")
EXCLUDE = "C:\\Windows"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\033[94m" + "="*60)
    print("      SCANN-CHEAT SYSTEM v1.0 | Powered by Metreon1k")
    print("="*60 + "\033[0m")
    print(f"[*] Target Signature: \033[93m{TARGET.decode()}\033[0m")
    print(f"[*] Search Path:      \033[93mC:\\\033[0m")
    print(f"[*] Status:           \033[92mScanning files...\033[0m\n")

    found_list = []
    start_time = time.time()
    files_scanned = 0

    try:
        for root, dirs, files in os.walk("C:\\"):
            if root.startswith(EXCLUDE):
                continue
            
            for file in files:
                if file.lower().endswith(EXTS):
                    path = os.path.join(root, file)
                    files_scanned += 1
                    
                    if files_scanned % 100 == 0:
                        print(f"\r[>] Scanned: {files_scanned} files...", end="", flush=True)

                    try:
                        with open(path, 'rb') as f:
                            if TARGET in f.read():
                                print(f"\r\033[92m[FOUND]\033[0m {path}")
                                found_list.append(path)
                    except:
                        continue
    except KeyboardInterrupt:
        print("\n\033[91m[!] Scanning aborted by user\033[0m")

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    print("\n\n" + "\033[94m" + "="*60)
    print(f"SCAN COMPLETED in {duration}s")
    if found_list:
        print(f"TOTAL MATCHES: \033[91m{len(found_list)}\033[0m")
    else:
        print(f"TOTAL MATCHES: \033[92m0\033[0m")
    print("="*60 + "\033[0m")

if __name__ == "__main__":
    main()
