import time
import sys

heart = [
"  ***     ***  ",
" *****   ***** ",
"******* *******",
" ************* ",
"  ***********  ",
"   *********   ",
"    *******    ",
"     *****     ",
"      ***      ",
"       *       "
]

def print_heart():
    for line in heart:
        print(line)
    print()

def type_out(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_heart()
    name = input("Untuk siapa (nama): ")
    msg = f"Aku sayang kamu, {name} ❤️"
    type_out(msg)
    # animasi kecil
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\nSelesai!")