class VigenereCipher(object):
    def __init__(self, key, alphabet) -> None:
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        print(f"ENCODE: {text}")
        times = len(text) // len(self.key)
        rest = len(text) % len(self.key)
        coded = self.key * times + self.key[:rest]
        encode = ''
        for i, letter in enumerate(text):
            if letter.isupper():
                return text
            if letter in self.alphabet:
                text_index = self.alphabet.find(letter)
                coded_index = self.alphabet.find(coded[i])
                encode += self.alphabet[(text_index + coded_index) % len(self.alphabet)]
            else:
                encode += letter
        return encode

    def decode(self, text):
        print(f"DECODE: {text}")
        times = len(text) // len(self.key)
        rest = len(text) % len(self.key)
        coded = self.key * times + self.key[:rest]
        decode = ''
        for i, letter in enumerate(text):
            if letter.isupper():
                return text
            if letter in self.alphabet:
                text_index = self.alphabet.find(letter)
                coded_index = self.alphabet.find(coded[i])
                decode += self.alphabet[(text_index - coded_index) % len(self.alphabet)]
            else:
                decode += letter
        return decode

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"

C = VigenereCipher(key, abc)
print(C.encode("javascript"))
print(C.decode("yansoqilet"))