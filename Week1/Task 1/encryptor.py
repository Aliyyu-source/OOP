# encryptor.py

class Encryptor:
    KEY = 3  # Simple Caesar cipher shift value

    @staticmethod
    def encrypt(text: str) -> str:
        result = ""
        for char in text:
            result += chr(ord(char) + Encryptor.KEY)
        return result

    @staticmethod
    def decrypt(text: str) -> str:
        result = ""
        for char in text:
            result += chr(ord(char) - Encryptor.KEY)
        return result
