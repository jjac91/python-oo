"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    """Finds random words from a given file
    >>> wf= WordFinder("test1.txt")
    3 words read

    >>> wf.random() in ["Hi", "Bye", "Shy"]
    True
    """
    def __init__(self, path,):
        """Reads file and reports number of words read"""
        self.path = path
        self.content = self.get_content()
        print(f"{len(self.content)} words read")
    def get_content(self):
        """Reads the file and gnerates the word list"""
        with open(f"{self.path}","r") as file:
            content = file.readlines()
        return content
    def random(self):
        """Returns random word"""
        return random.choice(self.content).strip()

class SpecialWordFinder(WordFinder):
    """WordFinder that excludes empty lines
    >>> swf.SpecialWordFinder("swords.txt")
    2 words read
    >>> swf.random() in ["longsword","Greatsword"]
    True
    """
    def get_content(self):
        with open(f"{self.path}","r") as file:
            content = file.readlines()
        stripped_content=[]
        for line in content:
            if not line.startswith("#") and not line.startswith("\n"):
                stripped_content.append(line.strip())
        return stripped_content