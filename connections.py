import os
import pickle
import dataStructures as ds

class userData:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.reminder = ds.priorityQueue()
        self.notes = ds.SingleLinkedList()
 

def files():
    dir_path = r'.'

    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
        
    return res


####################

def checkForTheFile():
    
    if ("dataBase.txt" not in files()):
        # create file
        file = open("dataBase.txt", "wb")
        default = ds.arrayList()
        pickle.dump(default, file)
        file.close()


#####################

def createAccount(username, password):
    newAccount = userData(username, password)
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    data.array.append(newAccount)

    file = open("dataBase.txt", "wb")
    pickle.dump(data, file)
    file.close()


def checkForTheUser(username, password):
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    c = 0

    for i in data.array:
        if i.username == username and i.password == password:
            return True , c
        
        c += 1
    
    return False, -1


def addReminder(reminder, proiority, index):
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    data.array[index].reminder.enqueue(reminder, proiority)

    file = open("dataBase.txt", "wb")
    pickle.dump(data, file)
    file.close()

def deleteReminder(index):
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    data.array[index].reminder.dequeue()

    file = open("dataBase.txt", "wb")
    pickle.dump(data, file)
    file.close()

    
def clearReminder(index):
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    data.array[index].reminder.clear()

    file = open("dataBase.txt", "wb")
    pickle.dump(data, file)
    file.close()
    

    

    


def addNote(title, note, index):

    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    data.array[index].notes.add(title, note)

    file = open("dataBase.txt", "wb")
    pickle.dump(data, file)
    file.close()

def readNote(title, index):
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    return data.array[index].notes.read(title)

def deleteNote(title, index):
    file = open("dataBase.txt", "rb")
    data = pickle.load(file)
    file.close()

    data.array[index].notes.remove(title)

    file = open("dataBase.txt", "wb")
    pickle.dump(data, file)
    file.close()