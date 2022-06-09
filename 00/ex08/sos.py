import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

def main():
	if len(sys.argv) < 2:
		print("Please provide at least an argument")
		return
	s = sys.argv[1] if len(sys.argv) == 2 else ' '.join(sys.argv[1:])
	print(''.join([MORSE_CODE_DICT.get(l.capitalize(), "") + " " for l in s]).strip(' ') if all([c.isalnum() or c.isspace() for c in s]) else "ERROR")

if __name__ == "__main__":
	main()