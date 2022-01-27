"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0,):
        self.start = start
        self.now = start
    
    def generate(self):
        """Returns the current value of SerialGenerator
         and then incrments it"""
        self.now +=1
        return self.now -1
    def reset(self):
        """Sets the now of the SerialGenerator back to the start value"""
        self.now = self.start

