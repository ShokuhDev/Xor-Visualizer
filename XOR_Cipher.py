import os
import time

# ================= COLORS =================

class Colors:
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# ================= CLEAR =================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================= BANNER =================

def banner():
    print(f"""{Colors.CYAN}{Colors.BOLD}

╔══════════════════════════════════════════════╗
║                                              ║
║                 XOR TOOL                     ║
║                                              ║
╚══════════════════════════════════════════════╝

{Colors.RESET}""")

# ================= VISUALIZER =================

def visualize(byte_value, key, mode):

    xor_value = byte_value ^ key

    ascii_bin = bin(byte_value)[2:].zfill(8)
    key_bin = bin(key)[2:].zfill(8)
    xor_bin = bin(xor_value)[2:].zfill(8)

    if mode == "encrypt":
        title = "🔒 ENCRYPTION PROCESS"
    else:
        title = "🔓 DECRYPTION PROCESS"

    print(f"\n{Colors.YELLOW}{'='*55}{Colors.RESET}")
    print(f"{Colors.BOLD}{title}{Colors.RESET}")
    print(f"{Colors.YELLOW}{'='*55}{Colors.RESET}")

    print(f"\n{Colors.CYAN}Byte:{Colors.RESET} {byte_value}")

    print(f"\n{Colors.BLUE}Binary Operation:{Colors.RESET}")

    print(f"  {ascii_bin}")
    print(f"⊕ {key_bin}")
    print(f"  {'─'*8}")
    print(f"  {Colors.GREEN}{xor_bin}{Colors.RESET}")

    print(f"\n{Colors.MAGENTA}Result Byte:{Colors.RESET} {xor_value}")

    time.sleep(0.2)

    return xor_value

# ================= ENCRYPT =================

def encrypt():

    clear()
    banner()

    text = input(f"{Colors.CYAN}Enter text to encrypt:{Colors.RESET} ")

    while True:

        try:
            key = int(input(f"{Colors.CYAN}Enter key (0-255):{Colors.RESET} "))

            if 0 <= key <= 255:
                break
            else:
                print(f"{Colors.RED}Key must be between 0 and 255{Colors.RESET}")

        except:
            print(f"{Colors.RED}Invalid key{Colors.RESET}")

    encrypted = bytearray()

    print(f"\n{Colors.GREEN}{Colors.BOLD}STARTING ENCRYPTION...{Colors.RESET}")

    for byte in text.encode("utf-8"):
        encrypted.append(visualize(byte, key, "encrypt"))

    print(f"\n{Colors.YELLOW}{Colors.BOLD}ENCRYPTED TEXT (HEX):{Colors.RESET}")
    print(encrypted.hex())

    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

# ================= DECRYPT =================

def decrypt():

    clear()
    banner()

    text = input(f"{Colors.CYAN}Enter encrypted text (HEX):{Colors.RESET} ")

    while True:

        try:
            key = int(input(f"{Colors.CYAN}Enter key (0-255):{Colors.RESET} "))

            if 0 <= key <= 255:
                break
            else:
                print(f"{Colors.RED}Key must be between 0 and 255{Colors.RESET}")

        except:
            print(f"{Colors.RED}Invalid key{Colors.RESET}")

    decrypted = bytearray()

    try:
        encrypted_bytes = bytes.fromhex(text)
    except ValueError:
        print(f"\n{Colors.RED}Invalid HEX input{Colors.RESET}")
        input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")
        return

    print(f"\n{Colors.GREEN}{Colors.BOLD}STARTING DECRYPTION...{Colors.RESET}")

    for byte in encrypted_bytes:
        decrypted.append(visualize(byte, key, "decrypt"))

    try:
        result = decrypted.decode("utf-8")
    except UnicodeDecodeError:
        result = decrypted.decode("utf-8", errors="replace")

    print(f"\n{Colors.YELLOW}{Colors.BOLD}DECRYPTED TEXT:{Colors.RESET}")
    print(result)

    input(f"\n{Colors.CYAN}Press Enter to continue...{Colors.RESET}")

# ================= MENU =================

def menu():

    while True:

        clear()
        banner()

        print(f"{Colors.YELLOW}1.{Colors.RESET} Encrypt")
        print(f"{Colors.YELLOW}2.{Colors.RESET} Decrypt")
        print(f"{Colors.YELLOW}3.{Colors.RESET} Exit")

        choice = input(f"\n{Colors.CYAN}Select option:{Colors.RESET} ")

        if choice == "1":
            encrypt()

        elif choice == "2":
            decrypt()

        elif choice == "3":

            print(f"\n{Colors.GREEN}Goodbye ✅{Colors.RESET}")
            break

        else:
            print(f"\n{Colors.RED}Invalid option{Colors.RESET}")
            time.sleep(1)
 #================= START =================

if __name__ == "__main__":
    menu()
