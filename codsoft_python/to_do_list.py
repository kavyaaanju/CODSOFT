from tkinter import *
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.guiWindow = Tk()
        self.guiWindow.title("To-Do List")
        self.guiWindow.geometry("700x400+550+250")
        self.guiWindow.resizable(0, 0)
        self.guiWindow.configure(bg="#DEB887")  # Cream background

        self.task_label = Label(self.guiWindow, text="TO-DO-LIST\nEnter the Task Title:",
                                font=("arial", "14", "bold"),
                                background="#8B4513",  # Brown background
                                foreground="#FFFFFF")  # White foreground
        self.task_label.place(x=20, y=30)

        self.task_field = Entry(
            self.guiWindow,
            font=("Arial", "14"),
            width=50,
            foreground="black",
            background="white",
        )
        self.task_field.place(x=180, y=30)

        self.add_button = Button(
            self.guiWindow,
            text="Add",
            width=15,
            bg='#D2691E',  # Chocolate brown
            font=("arial", "14", "bold"),
            command=self.add_task,
        )
        self.del_button = Button(
            self.guiWindow,
            text="Remove",
            width=15,
            bg='#D2691E',  # Chocolate brown
            font=("arial", "14", "bold"),
            command=self.delete_task,
        )
        self.del_all_button = Button(
            self.guiWindow,
            text="Delete All",
            width=15,
            font=("arial", "14", "bold"),
            bg='#D2691E',  # Chocolate brown
            command=self.delete_all_tasks
        )

        self.add_button.place(x=20, y=100)
        self.del_button.place(x=20, y=140)
        self.del_all_button.place(x=20, y=180)

        self.task_listbox = Listbox(
            self.guiWindow,
            width=70,
            height=15,
            font=("Arial", "12", "bold"),  # Adjusted font size for better appearance
            selectmode='SINGLE',
            background="WHITE",
            foreground="BLACK",
            selectbackground="#DEB887",  # Cream background for selection
            selectforeground="BLACK"
        )
        self.task_listbox.place(x=180, y=100)

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.list_update()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box == True:
            self.tasks.clear()
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

def main():
    todo_list = ToDoList()
    todo_list.guiWindow.mainloop()

if __name__ == "__main__":
    main()

