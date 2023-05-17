import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo: ", key="todo")
add_button = sg.Button("Add")

window = sg.Window('Todo List App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.list_r("list")
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            with open("files/list.txt", 'w') as file:
                file.writelines(todos)
        case sg.WIN_CLOSED:
            break
window.close()
