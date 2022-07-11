import datetime as dt

class nodePriority: # Node for Priority queue
    def __init__(self, value, priority):     
        self.data = value
        self.priority = priority
        self.next = None

class priorityQueue:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else: 
            return False
    
    def enqueue(self, value, priority):

        newNode = nodePriority(value, priority)


        if self.isEmpty():
            self.head = newNode
            return
        
        else:
            if self.head.priority > priority:
                newNode.next = self.head
                self.head = newNode
                return
            
            else:
                current = self.head
                while current.next:
                    if priority <= current.next.priority:
                        break
                    
                    current = current.next
                
                newNode.next = current.next
                current.next = newNode
                return
    
    def dequeue(self):
        if self.isEmpty():
            return
            
        else:
            self.head = self.head.next
            return
    
    def peek(self):
        if self.isEmpty():
            return None
        
        else:
            return self.head.data
    
    def traverse(self):
        if self.isEmpty():
            return "Queue is Empty!"
            
        else:
            current = self.head
            while current:
                print(current.data, end = " ")
                current = current.next
        
        print(" ")
    
    def clear(self):
        self.head = None
        return

###################################################################


class NodeL: # Node for Linked List
    def __init__(self, title, note):
        self.note = note
        self.title = title
        self.dateCreated = dt.date.today()
        self.timeCreated = dt.datetime.now().time()
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else: 
            return False
    
    def add(self, title, note):
        newNode = NodeL(title, note)
        
        if self.isEmpty():
            self.head = newNode
            return
        
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = newNode
            return
    
    def remove(self, title):
        if self.isEmpty():
            return
        
        else:
            current = self.head
            if current.title == title:
                self.head = current.next
                return
            
            while current.next:
                if current.next.title == title:
                    current.next = current.next.next
                    return
                current = current.next
            return
    
    def read(self, title):
        if self.isEmpty():
            return "List is Empty!"
            
        else:
            current = self.head
            while current:
                if current.title == title:
                    return current.note
                current = current.next


    def traverse(self):
        if self.isEmpty():
            return "List is Empty!"
            
        else:
            current = self.head
            while current:
                print(current.data, end = " ")
                current = current.next
        
        print(" ")
    
    def removeAll(self):
        self.head = None
    
#####################################

class arrayList:
    def __init__(self):   
        self.array = []
    
    def add(self, item):
        self.array.append(item)