from math import ceil

class BinarySearch(list):
    
    def __init__(self, a, b):

        # initializing the list 
        num = b
        for i in range(0, a):
            self.append(num)
            num += b
         
        self.length = len(self)


    def search(self, value):
        dictionary = {}
        count = 0   
        minimum = 0
        maximum = self.length - 1
 
        if value == self[maximum]:
            dictionary['count'] = 0
            dictionary['index'] = maximum
            return dictionary

        while maximum >= minimum:
            count += 1
            guess = int(ceil((maximum + minimum) / 2))
            print("Guess is %s, maximum is %s, minimum is %s on count %s" % (guess, maximum, minimum, count))
            
 
            if self[guess] == value:
                dictionary['count'] = count
                dictionary['index'] = guess
                return dictionary
            elif self[guess] > value:
                maximum = guess - 1
            elif self[guess] < value:
                minimum = guess + 1

        dictionary['count'] = 3
        dictionary['index'] = -1 # not found
        return dictionary 
