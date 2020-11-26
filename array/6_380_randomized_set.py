import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.map[val] = 1
            return True
        else:
            return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if type(self.map.pop(val, False)) == bool:
            return False
        else:
            return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(list(self.map.keys()))


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
