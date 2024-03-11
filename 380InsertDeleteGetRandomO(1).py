import random


class RandomizedSet(object):

    def __init__(self):
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.list:
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            index = self.list.index(val)
            self.list.pop(index)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)


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
