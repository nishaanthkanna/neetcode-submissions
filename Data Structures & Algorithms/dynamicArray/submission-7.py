class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0
        self.last_element = -1

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        
        if self.size < self.capacity:
            self.last_element += 1
            self.array[self.last_element] = n
            self.size += 1
        else:
            self.resize()
            self.pushback(n)
        print(self.array)

    def popback(self) -> int:
        self.size -= 1
        element = self.array.pop(self.last_element)
        self.last_element -= 1
        return element

    def resize(self) -> None:
        self.array.extend([0] * self.capacity)
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
