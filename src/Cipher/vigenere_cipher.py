from typing import Optional

class vigenere_cipher:

    def __init__(self):
        self.capitalized = []

    # This function helps preserve capitalization
    def get_num(self, char, idx):
        num = ord(char)
        if (num > 64 and num < 91):
            num = num - 65
            self.capitalized.append(True)
        elif (num > 96 and num < 123):
            num = num - 97
            self.capitalized.append(False)
        else : raise Exception("Please only use alphabetical characters in the text!")
        return num

    def encipher(self, text: str, key: str, shift_left: Optional[bool] = True):
        if not key: raise Exception("Please enter a valid key!")
        key = ''.join(key.split()).lower()
        if (not key.isalpha()): raise Exception("Please only use alphabetical characters in the key!")
        key_len = len(key)
        text = ''.join(text.split())
        result = ''
        self.capitalized = []
        if (shift_left):
            for i, char in enumerate(text):
                key_val = ord(key[(i%key_len)])-97
                num = self.get_num(char, i)
                num = ((num+key_val)%26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)
        else:
            for i, char in enumerate(text):
                key_val = ord(key[(i % key_len)]) - 65
                num = self.get_num(char, i)
                num = ((num - key_val) % 26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)

        return result

    def decipher(self, text: str, key: str, shift_left: Optional[bool] = True):
        if not key: raise Exception("Please enter a valid key!")
        key = ''.join(key.split()).lower()
        if (not key.isalpha()): raise Exception("Please only use alphabetical characters in the key!")
        key_len = len(key)
        text = ''.join(text.split())
        result = ''
        self.capitalized = []
        if (shift_left):
            for i, char in enumerate(text):
                key_val = ord(key[(i%key_len)])-97
                num = self.get_num(char, i)
                num = ((num-key_val)%26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)
        else:
            for i, char in enumerate(text):
                key_val = ord(key[(i % key_len)]) - 65
                num = self.get_num(char, i)
                num = ((num + key_val) % 26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)

        return result

