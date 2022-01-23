class map_node:
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self.next = None


class hashmap:
    def __init__(self,size) :
        self.size = size
        self.array = [None]*self.size
        self.count = 0

    def get_index(self,hashed_value) : # Compression function
        return abs(hashed_value)%self.size

    def get_loading_factor(self) :
        return self.count/self.size

    def rehash(self) :
        temp = self.array
        self.size = 2*self.size
        self.array = [None]*self.size
        self.count = 0
        for head in temp :
            while head :
                self.insert(head.key,head.value)
                head = head.next
        print("New loading factor is",self.get_loading_factor())
        return

    def insert(self,key,value) :
        hashed_value = hash(key) # Hash code
        index = self.get_index(hashed_value)
        head = self.array[index]
        while head :
            if head.key == key : # Updating the value if the keys are same
                head.value = value
                print(f"Updated Key = {key} , Value = {value} sucessfully")
                return
            head = head.next
        # When a new key is given we are inserting the value
        new_node = map_node(key,value)
        new_node.next , self.array[index] = self.array[index] , new_node
        self.count += 1
        print(f"Inserted Key = {key} , Value = {value} sucessfully")
        if self.get_loading_factor() >= 0.7 :
            print("Rehashing hashtable to balance the loading factor ...")
            self.rehash()
        return

    def delete(self,key) :
        hashed_value = hash(key) # Hash code
        index = self.get_index(hashed_value)
        head = self.array[index]
        prev = None # Keeping track of the previous node
        while head :
            if prev == None and head.key == key : # Deleting head node
                self.array[index] = head.next
                self.count -= 1
                print(f"Deleted Key = {key} , Value = {head.value} sucessfully")
                return
            if head.key == key : # Deleting tail and other nodes
                prev.next = head.next
                self.count -= 1
                print(f"Deleted Key = {key} , Value = {head.value} sucessfully")
                return
            prev = head
            head = head.next
        print("Given key is not present in hashmap")
        return None # if given key is not present

    def search(self,key) :
        hashed_value = hash(key) # Hash code
        index = self.get_index(hashed_value)
        head = self.array[index]
        while head :
            if head.key == key :
                print(f"Value of given Key = {key} , is Value = {head.value}")
                return
            head = head.next
        print("Given key is not present in hashmap")
        return None # Returning none if that key is not present

m = hashmap(5)
for x in range(10) :
    m.insert(x,x+1)
    print("loading factor : ",m.get_loading_factor())
