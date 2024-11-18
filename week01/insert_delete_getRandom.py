class RandomizedSet:

    def __init__(self):
        self.data = []
        self.data_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.data_to_idx:
            return False
        self.data.append(val)
        self.data_to_idx[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_to_idx:
            return False
      
        idx_to_remove = self.data_to_idx[val]
    
       
        last_val = self.data[-1]

      
        self.data[idx_to_remove] = last_val
        self.data_to_idx[last_val] = idx_to_remove

        
        self.data.pop()

       
        del self.data_to_idx[val]
        return True
    


    def getRandom(self) -> int:
        import random
        return self.data[random.randint(0, len(self.data)-1)]
      

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()