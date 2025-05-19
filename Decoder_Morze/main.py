from colorama import init, Fore
from colorama import Back
from colorama import Style
import sys

init(autoreset=True)

print(Fore.MAGENTA + """
    __  ___                      ____                      __         
   /  |/  /___  _________  ___  / __ \___  _________  ____/ /__  _____
  / /|_/ / __ \/ ___/_  / / _ \/ / / / _ \/ ___/ __ \/ __  / _ \/ ___/
 / /  / / /_/ / /    / /_/  __/ /_/ /  __/ /__/ /_/ / /_/ /  __/ /    
/_/  /_/\____/_/    /___/\___/_____/\___/\___/\____/\__,_/\___/_/    

""")

MORSE_CODE_TABLE = {
 '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
 '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
 '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
 '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
 '--..': 'Z', '.-.-.-': '.', '--..--': ',', '..--..': '?',
 '.----': '1', '..---': '2', '...--': '3', '....-': '4',
 '.....': '5', '-....': '6', '--...': '7', '---..': '8',
 '----.': '9', '-----': '0', '...---...': 'SOS'
}

def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    decoded_message = ''

    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in MORSE_CODE_TABLE:
                decoded_message += MORSE_CODE_TABLE[letter]
        decoded_message += ' '
    return decoded_message.strip()

def flag_void():
    if '-h' in sys.argv:
        print("Алфавит Морзе")
        print(Fore.CYAN + """ 
A .-          S ...
B -...        T -
C -.-.        U ..-
D -..         V ...-
E .           W .--
F ..-.        X -..-
G --.         Y -.--
H ....        Z --..
I ..          1 .----
J .---        2 ..---
K -.-         3 ...--
L .-..        4 ....-
M --          5 .....
N -.          6 -....
O ---         7 --...
P .--.        8 ---..
Q --.-        9 ----.
R .-.         0 -----
""")

def cipher_input():
    print("Вывод алфавита: -h\n")

    user_input = input("Введите зашифрованное сообщение: ")
    decoded_text = decode_morse(user_input)

    print(f"\nРасшифровка: {decoded_text}")

if __name__ == "__main__":
    flag_void()
    cipher_input()