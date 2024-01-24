class RandomizedSet:
    
    
    def __init__(self):
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        else:
            self.arr.append(val)
            # print(self.arr)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            # print(self.arr)
            return True
        else:
            return False
        
        
    def getRandom(self) -> int:
        import random
        if self.arr:
            random_elem = random.choice(self.arr)
            return random_elem
        else:
          return None
            
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(2)
param_1 = obj.insert(0)
# param_2 = obj.remove(1)
param_3 = obj.getRandom()

print(param_1)
# print(param_2)
print(param_3)