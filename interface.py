
import tkinter as tk # Gui libraries
from tkinter import ttk # Gui libraries
import time
import datetime as dt
import connections as con
from tkinter import messagebox # GUI
import dataStructures as ds
import pickle 


con.checkForTheFile()

Index = 0 # index of the user in the list

def signIn(): # Method to sign in, to create new account

    root = tk.Tk()
    root.geometry("800x500")
    root.resizable(0, 0)
    root.title("myDiary Log In")
    root.config(bg="white")


    ##################################

    labelLogin = tk.Label(root, text="myDiary Log In", font=("Arial", 20, "bold italic"), bg="white")
    labelLogin.place(x=300, y=50)

    labelName = tk.Label(root, text="Username", font=("Arial", 20, "bold"), bg="white")
    labelName.place(x=100, y=150)

    entryName = tk.Entry(root, font=("Arial", 20), bg="white")
    entryName.place(x=300, y=150)

    labelPassword = tk.Label(root, text="Password", font=("Arial", 20, "bold"), bg="white")
    labelPassword.place(x=100, y=250)

    entryPassword = tk.Entry(root, font=("Arial", 20), bg="white", show="●")
    entryPassword.place(x=300, y=250)

    labelPassword2 = tk.Label(root, text="Confirm", font=("Arial", 20, "bold"), bg="white")
    labelPassword2.place(x=100, y=350)

    entryConfirmPassword = tk.Entry(root, font=("Arial", 20), bg="white", show="●")
    entryConfirmPassword.place(x=300, y=350)

    ##################################

    def createAccount():
        username = entryName.get()
        password = entryPassword.get()
        confirmPassword = entryConfirmPassword.get()

        if password == confirmPassword:
            con.createAccount(username, password)
            messagebox.showinfo("Sign In", "Account created successfully")
            root.destroy()
            logIn()
        
        else:
            messagebox.showinfo("Sign In", "Password does not match\nTry Again")
        
    buttonCreateAccount = tk.Button(root, text="Create Account", font=("Arial", 15, "bold"), bg="white", bd = 5, command = createAccount)
    buttonCreateAccount.place(x=300, y=420)

    ####################################

    root.mainloop()

#signIn()

#################################################################

def newNote(): # Function that generates a windo for new Note
    root = tk.Tk()
    root.geometry("900x600")
    root.resizable(0, 0)
    root.title("New myDiary")
    root.config(bg="white")

    #####################################

    labelTitle = tk.Label(root, text="Title", font = ("ariel", 20, "bold italic"), bg = "white")
    labelTitle.place(x = 10, y = 5)

    entryTitle = tk.Entry(root, font = ("ariel", 20), bg = "white", width = 53)
    entryTitle.place(x = 92, y = 5)

    notes = tk.Text(root, font = "ariel 12 bold", bg = "white", height = 26, width = 98)
    notes.place(x = 5, y = 45)


    def addNote(): # Function that adds the note to the list (Save Button)
        title = entryTitle.get()
        note = notes.get("1.0", "end-1c")

        con.addNote(title, note, Index)

        root.destroy()
        homePage()

    def clear():
        entryTitle.delete(0, "end")
        notes.delete("1.0", "end")

    

    buttonSave = tk.Button(root, text=35 * " " + "Save" + 35 * " " , font=("Arial", 15, "bold"), bg="white", command=addNote)
    buttonSave.place(x=5, y=555)

    buttonClear = tk.Button(root, text=28 * " " + "Clear" + 28 * " " , font=("Arial", 15, "bold"), bg="white", command=clear)
    buttonClear.place(x=489, y=555)




    #####################################


    root.mainloop()


#newNote()

#####################################################################################

def homePage():

    root = tk.Tk()
    root.geometry("900x600")
    root.resizable(0, 0)
    root.title("myDiary")
    root.config(bg="white")


    #####################################

    def setReminder():
        root2 = tk.Tk()
        root2.geometry("350x100")
        root2.title("Set Reminder")
        root2.config(bg="azure")

        #####################################

        labelTitle = tk.Label(root2, text="Title", font=("Arial", 15, "bold italic"), bg="azure")
        labelTitle.place(x=10, y=10)

        entryTitle = tk.Entry(root2, font=("Arial", 15), bg="white")
        entryTitle.place(x=100, y=10)

        labelPriority = tk.Label(root2, text="Priority", font=("Arial", 15, "bold italic"), bg="azure")
        labelPriority.place(x=10, y=40)

        entryPriority = tk.Entry(root2, font=("Arial", 15), bg="white", width = 3)
        entryPriority.place(x=100, y=40)

        buttonAddReminder = tk.Button(root2, text=3 * " " + "Add" + " " * 3, font=("Arial", 15, "bold"), bg="white", bd = 3, command = lambda : [con.addReminder(entryTitle.get(), entryPriority.get(), Index), addReminderTree(), root2.destroy()])
        buttonAddReminder.place(x=180, y=50)

        addReminderTree()

        #####################################
        root2.mainloop()
    
    labelReminder = tk.Label(root, text="Reminders", font=("Arial", 15, "bold italic"), bg="white")
    labelReminder.place(x=719, y=12)

    scroll_y_Reminder=tk.Scrollbar(root,orient="vertical")
    treeviewReminder=ttk.Treeview(root,height=6,columns=("Title","Priority"),show="headings",yscrollcommand=scroll_y_Reminder.set)
    scroll_y_Reminder.pack(side="right", fill="y")
    scroll_y_Reminder.config(command=treeviewReminder.yview)

    treeviewReminder.heading("Title",text="Title")
    treeviewReminder.heading("Priority",text="Priority")


    treeviewReminder.column("Title",width=170,anchor="center")
    treeviewReminder.column("Priority",width=60,anchor="center")

    treeviewReminder.place(x=650,y=45)

    buttonNewReminder = tk.Button(root, text=10 * " " + "New" + 10 * " " , font=("Arial", 10, "bold"), bg="white", command = setReminder)
    buttonNewReminder.place(x=650, y=195)

    buttonDeleteReminder = tk.Button(root, text=7 * " " + "Delete" + 7 * " " , font=("Arial", 10, "bold"), bg="white", command = lambda : [con.deleteReminder(Index), addReminderTree()])
    buttonDeleteReminder.place(x=773, y=195)

    buttonClearReminder = tk.Button(root, text=33 * " " + "Clear" + 33 * " " , font=("Arial", 7, "bold"), bg="white", command = lambda : [con.clearReminder(Index), addReminderTree()])
    buttonClearReminder.place(x=650, y=225)


    def addReminderTree():
        #treeviewReminder.insert("", "end", text="1", values=("Title","Priority"))

        file = open("dataBase.txt", "rb")
        data = pickle.load(file)
        data = data.array[Index].reminder
        file.close()

        for i in treeviewReminder.get_children(): # delete all items
            treeviewReminder.delete(i)

        if data.isEmpty():
            pass
            
        else:
            temp = data.head
            while temp:
                #print(temp.data, end = " ")
                treeviewReminder.insert("", "end", text="1", values=(temp.data,str(temp.priority)))
                temp = temp.next
    
    addReminderTree()


        

    #########################################

    labelNotes = tk.Label(root, text="Entries", font=("Arial", 25, "bold italic"), bg="white")
    labelNotes.place(x=20, y=202)

    scroll_y_Notes=tk.Scrollbar(root,orient="vertical")
    treeviewNotes=ttk.Treeview(root,height=16,columns=("Title","Date_of_Creation","Time_of_Creation"),show="headings",yscrollcommand=scroll_y_Notes.set)
    scroll_y_Notes.pack(side="left", fill="y")
    scroll_y_Notes.config(command=treeviewNotes.yview)

    treeviewNotes.heading("Title",text="Title")
    treeviewNotes.heading("Date_of_Creation",text="Date of Creation")
    treeviewNotes.heading("Time_of_Creation",text="Time of Creation")


    treeviewNotes.column("Title",width=455,anchor="center")
    treeviewNotes.column("Date_of_Creation",width=200,anchor="center")
    treeviewNotes.column("Time_of_Creation",width=200,anchor="center")
 
    treeviewNotes.place(x=20,y=250)

    #####################################

    def openNote(title):

        root3 = tk.Tk()
        root3.geometry("900x600")
        root3.resizable(0, 0)
        root3.title(title)
        root3.config(bg="white")

        #####################################

        notes = tk.Text(root3, font = "ariel 12 bold", bg = "azure", height = 28, width = 98)
        notes.place(x = 5, y = 5)

        notes.insert("end",con.readNote(title, Index))



    buttonNewNote = tk.Button(root, text=10 * " " + "New" + 10 * " " , font=("Arial", 12, "bold"), bg="white", command=lambda : [root.destroy(), newNote()])
    buttonNewNote.place(x=150, y=210)

    buttonOpenNote = tk.Button(root, text=10 * " " + "Open" + 10 * " " , font=("Arial", 12, "bold"), bg="white", command = lambda : [openNote(treeviewNotes.item(treeviewNotes.selection())["values"][0])])
    buttonOpenNote.place(x=320, y=210)

    buttonDeleteNote = tk.Button(root, text=10 * " " + "Delete" + 10 * " " , font=("Arial", 12, "bold"), bg="white", command = lambda : [con.deleteNote(treeviewNotes.item(treeviewNotes.selection())["values"][0], Index), addNotesTree()])
    buttonDeleteNote.place(x=500, y=210)

    #####################################

    def addNotesTree():
        #treeviewReminder.insert("", "end", text="1", values=("Title","Priority"))

        file = open("dataBase.txt", "rb")
        data = pickle.load(file)
        data = data.array[Index].notes
        file.close()

        for i in treeviewNotes.get_children(): # delete all items
            treeviewNotes.delete(i)

        if data.isEmpty():
            pass
            
        else:
            temp = data.head
            while temp:
                #print(temp.data, end = " ")
                treeviewNotes.insert("", "end", text="1", values=(temp.title, temp.dateCreated, temp.timeCreated))
                temp = temp.next
    
    addNotesTree()

    #####################################

    clock=tk.Label(root,font="ariel 50 bold",bg="white")
    clock.place(x=130 + 50,y=18 + 20)

    date_label=tk.Label(root,text="date",font="ariel 20 bold",bg="white")
    date_label.place(x=180 + 50,y=100 + 20)
    
    
    def tick():
        time_string=time.strftime("%H : %M : %S")
        clock.config(text=time_string)
        clock.after(1,tick)
    
    tick()
    
    
    def tok():
        today=dt.date.today()
        day=today.ctime()
        date_label_info=day[0:4]+", "+day[4:11]+", "+day[20:24]
        date_label.config(text=date_label_info)
    
    tok()
    


    #####################################
    root.mainloop()

#####################################################################################

#homePage()


def logIn():
    global Index

    root = tk.Tk()
    root.geometry("800x500")
    root.resizable(0, 0)
    root.title("myDiary Log In")
    root.config(bg="white")


    #######################################

    labelLogin = tk.Label(root, text="myDiary Log In", font=("Arial", 20, "bold italic"), bg="white")
    labelLogin.place(x=300, y=50)

    labelName = tk.Label(root, text="Username", font=("Arial", 20, "bold"), bg="white")
    labelName.place(x=100, y=150)

    entryName = tk.Entry(root, font=("Arial", 20), bg="white")
    entryName.place(x=300, y=150)

    labelPassword = tk.Label(root, text="Password", font=("Arial", 20, "bold"), bg="white")
    labelPassword.place(x=100, y=250)

    entryPassword = tk.Entry(root, font=("Arial", 20), bg="white", show="●")
    entryPassword.place(x=300, y=250)


    def getData():
        global Index
        username = entryName.get()
        password = entryPassword.get()

        flag, Index = con.checkForTheUser(username, password)

        if not flag:
            messagebox.showinfo("Log In", "User name or password is incorrect")
        
        else:
            root.destroy()
            homePage()

    ####################################

    buttonLogin = tk.Button(root, text="Log In", font=("Arial", 15, "bold"), bg="white", bd = 5, command = getData)
    buttonLogin.place(x=300, y=350)

    labelSignin = tk.Label(root, text="Don't have an account?", font=("Arial", 15), bg="white")
    labelSignin.place(x=250, y=450)

    buttonSignin = tk.Button(root, text="Sign In", font=("Arial", 10, "bold"), bg="white", command = lambda:[root.destroy(), signIn()])
    buttonSignin.place(x=500, y=450)
    ####################################

    


    root.mainloop()

logIn()

####################