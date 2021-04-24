"""
Palindrome class realization.
"""
from arraystack import ArrayStack   # or from linkedstack import LinkedStack

class Palindrome:
    """
    Represents a palindrome finder.
    """

    def __init__(self):
        """
        initialise instance vars with empty lists
        """
        self.words = []
        self.palindromes = []

    def read_file(self, filename):
        """
        reads all the words from the file, strips the redundance.
        """
        self.words = [
            word.split('/')[0].split(' ')[0].strip()
            for word in open(filename, 'r').readlines()
            if not word.startswith(' +')
        ]
        return self.words

    @staticmethod
    def is_palindrome(word):
        """
        this function checks whether a word is a palindrome ('A'!='a')
        """
        # word = word.lower() -- why through? :(
        return word[::-1] == word

    def find_palindromes(self, file_from, file_to):
        """
        fincs all the palindromes and writes them to file_to
        """
        self.read_file(file_from)
        palindromes = ArrayStack()
        for word in self.words:
            if self.is_palindrome(word):
                palindromes.push(word)
        self.palindromes = []
        while True:
            try:
                word = palindromes.pop()
                # if len(word) > 1: -- would've been useful for end version
                self.palindromes.append(word)
            except KeyError:
                break
        self.palindromes = self.palindromes[::-1]
        self.write_to_file(file_to)
        return self.palindromes

    def write_to_file(self, filename):
        """
        writes the palindromes to filename
        """
        with open(filename, 'w') as f_out:
            f_out.write("\n".join(self.palindromes))


if __name__ == "__main__":
    palindrome = Palindrome()
    palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("words.txt", "palindrome_en.txt")
