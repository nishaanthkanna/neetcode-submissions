class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity
        self.size = 0
        # self.last_element = -1

    def get(self, i: int) -> int:
        print(self.array)
        print(i)
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        print(self.array)
        self.array[i] = n

    def pushback(self, n: int) -> None:
        print(self.array)
        if self.size < self.capacity:
            self.array.append(n)
            self.size += 1
        else:
            self.resize()
            self.pushback(n)

    def popback(self) -> int:
        self.size -= 1
        element = self.array.pop()
        return element

    def resize(self) -> None:
        # self.array.extend([] * self.capacity)
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
