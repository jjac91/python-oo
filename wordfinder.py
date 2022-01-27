"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
def __init__(self, path,):
    self.path = path
def read_all_lines(self):
    count = 0
    with open(f"{self.path}","r") as file:
        for line in file:
            count+=1
    print(f"{count} words read")