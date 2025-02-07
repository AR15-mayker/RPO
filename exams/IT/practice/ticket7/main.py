MORSE_CODE = {
    'А': '.-',     'Б': '-...',   'В': '.--',    'Г': '--.',   'Д': '-..',
    'Е': '.',      'Ё': '.',      'Ж': '...-',   'З': '--..',  'И': '..',
    'Й': '.---',   'К': '-.-',    'Л': '.-..',   'М': '--',    'Н': '-.',
    'О': '---',    'П': '.--.',   'Р': '.-.',    'С': '...',    'Т': '-',
    'У': '..-',    'Ф': '..-.',   'Х': '....',   'Ц': '-.-.',  'Ч': '--..-',
    'Ш': '--..',   'Щ': '--.-.',  'Ъ': '.--.-.',  'Ы': '-.--',  'Ь': '-..-',
    'Э': '..-..',  'Ю': '..--',   'Я': '.-.-',

    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-',  '(': '-.--.',
    ')': '-.--.-'
}

def encode_morse(message):
    encoded_message = []
    
    for char in message.upper():
        if char in MORSE_CODE:
            encoded_message.append(MORSE_CODE[char])
        elif char == " ":
            encoded_message.append("")
        else:
            print(f"Предупреждение: символ '{char}' не поддерживается и будет пропущен.")
    
    return " ".join(encoded_message).strip()

def main():
    user_input = input("Введите сообщение для кодирования: ")
    
    if not user_input.strip():
        print("Ошибка: сообщение не должно быть пустым.")
        return

    morse_coded = encode_morse(user_input)
    
    if morse_coded:
        print(f"Азбука Морзе: {morse_coded}")
    else:
        print("Ошибка: не удалось закодировать сообщение.")


if __name__ == "__main__":
    main()
