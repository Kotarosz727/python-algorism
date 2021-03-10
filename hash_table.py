import hashlib

class HashTable(object):
    def __init__(self, size=10):
        self.size = 10
        self.table = [[] for i in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base = 16) % self.size

    def add(self, key, value):
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self):
        for data in self.table:
            print(data)    

    def get(self, key):
        index = self.hash(key)

        for data in self.table[index]:
            if data[0] == key:
                print(data[1])
                return data[1]        

test = HashTable()
test.add("car", "toyota")
test.add("car", "honda")
test.get("car")