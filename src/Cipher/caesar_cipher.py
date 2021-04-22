from typing import Optional

class caesar_cipher:

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
        else : raise Exception("Please use alphabetical characters only!")
        return num

    def encipher(self, text: str, key: int, shift_left: Optional[bool] = True):
        text = ''.join(text.split())
        result = ''
        self.capitalized = []
        if (shift_left):
            for i, char in enumerate(text):
                num = self.get_num(char, i)
                num = ((num+key)%26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)
        else:
            for i, char in enumerate(text):
                num = self.get_num(char, i)
                num = ((num - key) % 26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)

        return result

    def decipher(self, text: str, key: int, shift_left: Optional[bool] = True):
        text = ''.join(text.split())
        result = ''
        self.capitalized = []
        if (shift_left):
            for i, char in enumerate(text):
                num = self.get_num(char, i)
                num = ((num-key)%26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)
        else:
            for i, char in enumerate(text):
                num = self.get_num(char, i)
                num = ((num + key) % 26) + 65
                if (not self.capitalized[i]): num += 32
                result += chr(num)

        return result




# print(encipher('eazy', 2))
# for i in range(ord('a'), ord('z')):
#         print(i)
# for i in range(ord('A'), ord('Z')):
#         print(i)
# for i in range(65, 123):
#     print(str(i)+': '+chr(i))