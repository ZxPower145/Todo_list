from files import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text(key="clock")

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo: ", key="todo")
add_button = sg.Button(image_source="files/add.png",
                       mouseover_colors="green",
                       tooltip="Add",
                       key="Add")

list_box = sg.Listbox(values=functions.list_r(),
                      key='todos',
                      enable_events=True,
                      size=(45, 10))

edit_btn = sg.Button(image_source="files/edit.png",
                     tooltip="Edit",
                     mouseover_colors="brown",
                     key="Edit")

complete_btn = sg.Button(image_source="files/complete.png",
                         mouseover_colors="green",
                         tooltip="Complete",
                         key="Complete")

exit_btn = sg.Button("Exit")

window = sg.Window('Todo List App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box],
                           [edit_btn, complete_btn],
                           [exit_btn]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.list_r()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            if new_todo != "":
                functions.todos_w(todos)
                window['todos'].update(values=todos)
            else:
                sg.popup("Please type in an item first!", text_color="red", font=("Times new roman", 15))
        case "Edit":
            try:
                selected_todo = values['todos'][0]
                new_todo = values['todo']
                todos = functions.list_r()

                if selected_todo in todos:
                    index = todos.index(selected_todo)
                    todos[index] = new_todo
                    functions.todos_w(todos)
                    window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", text_color="red", font=("Times new roman", 15))
        case "todos":
            try:
                window['todo'].update(value=values['todos'][0].replace("\n", ""))
            except IndexError:
                sg.popup("Please select a valid item", text_color="red", font=("Times new roman", 15))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.list_r()
                todos.remove(todo_to_complete)
                functions.todos_w(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first!", text_color="red", font=("Times new roman", 15))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
