import tkinter
import random
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog


#
def update_tasks():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)
    numtask = len(tasks)
    label_dsp_count['text'] = numtask


def clear_listbox():
    lb_tasks.delete(0, "end")


def add_task():
    label_dsply["text"] = ""
    Ntask = text_input.get()
    if Ntask != "":
        tasks.append(Ntask)
        update_tasks()
    else:
        label_dsply["text"] = "Nothing added"
    text_input.delete(0, 'end')


def delete_all():
    conf = messagebox.askquestion(
        'Delete All?', 'Confirm Deletetion?')
    print(conf)
    if conf.upper() == "YES":
        global tasks
        tasks = []
        update_tasks()
    else:
        pass


def delete_one():
    de = lb_tasks.get("active")
    if de in tasks:
        tasks.remove(de)
    update_tasks()


def sort_asc():
    tasks.sort()
    update_tasks()


def sort_dsc():
    tasks.sort(reverse=True)
    update_tasks()


def save_file():
    f = asksaveasfile(initialfile = '.txt',
defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    for listitem in tasks:
        f.write('%s\n' % listitem)
    f.close()



#def save_act():
  #  savecon = messagebox.askquestion(
    #    'Save Confirmation', 'Save your progress?')
    #if savecon.upper() == "YES":
      #  with open("SaveFile.txt", "w") as filehandle:
        #    for listitem in tasks:
          #      filehandle.write('%s\n' % listitem)
    #else:
      #  pass


def load_info():
    messagebox.showinfo(
        "Info", "Created by Thomas",)
    
    
def open_files():
    path= filedialog.askopenfilename(title="Select a file", filetypes=(("text files","*.txt"),
("all files","*.*")))
    f=open(path, "r")
    for listitem in f:
        tasks.append(listitem)
#         f.write('%s\n' % listitem)
    f.close()
    update_tasks()




#def load_act():
  #  loadcon = messagebox.askquestion(
    #    'Save Confirmation', 'save your progress?')
    #if loadcon.upper() == "YES":
      #  tasks.clear()

        #with open('SaveFile.txt', 'r') as filereader:
          #  for line in filereader:
            #    currentask = line
              #  tasks.append(currentask)
            #update_tasks()

    #else:
      #  pass


def exit_app():
    confex = messagebox.askquestion(
        'Quit Confirmation', 'Are you sue you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass


root = tkinter.Tk()
# change root background col and ect
root.configure(bg="white")
root.title("To Do List")
root.geometry("260x300")

#prevent window resizing
root.resizable(False, False)

# database
tasks = []
# tasks = ['tes 1', 'best2', 'dest3']


# GUI (graphical user interface)
# main root app


label_title = tkinter.Label(root, text="", bg="white")
label_title.grid(row=0, column=0)

label_dsply = tkinter.Label(root, text="Number of tasks: ", bg="white")
label_dsply.grid(row=0, column=1)

label_dsp_count = tkinter.Label(root, text="", bg="white")
label_dsp_count.grid(row=0, column=3)

#Entry Box
text_input = tkinter.Entry(root, width=15)
text_input.grid(row=1, column=1)

# button section
text_add_bttn = tkinter.Button(
    root, text="Add Task", bg="white", fg="green", width=15, command=add_task)
text_add_bttn.grid(row=1, column=0)

delone_bttn = tkinter.Button(
    root, text="Complete Task", bg="white", width=15, command=delete_one)
delone_bttn.grid(row=3, column=0)

delall_bttn = tkinter.Button(
    root, text="Delete all", bg="white", width=15, command=delete_all)
delall_bttn.grid(row=4, column=0)

sort_asc = tkinter.Button(root, text="sort (ascending)",
                          bg="White", width=15, command=sort_asc)
sort_asc.grid(row=5, column=0)

sort_dsc = tkinter.Button(root, text="sort (descending)",
                          bg="White", width=15, command=sort_dsc)
sort_dsc.grid(row=6, column=0)

exit_bttn = tkinter.Button(root, text="Quit",
                           bg="white", width=15, command=exit_app)
exit_bttn.grid(row=7, column=0)

save_button = tkinter.Button(
    root, text="Save List", bg="white", width=15, command=save_file)
save_button.grid(row=11, column=1)

load_button = tkinter.Button(
    root, text="Load Task List", bg="white", width=15, command=open_files)
load_button.grid(row=11, column=0)

info_button = tkinter.Button(
    root, text="Info", bg="white", width=15, command=load_info)
info_button.grid(row=14, column=0, columnspan=2)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7)


# main loop
root.mainloop()
