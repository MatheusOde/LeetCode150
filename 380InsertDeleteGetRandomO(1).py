import random


class RandomizedSet(object):

    def __init__(self):
        self.dict = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = True
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.dict.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def main():
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    print(param_1)


if __name__ == '__main__':
    main()
