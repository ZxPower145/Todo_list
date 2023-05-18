import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo: ", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.list_r(),
                      key='todos',
                      enable_events=True,
                      size=(45, 10))

edit_btn = sg.Button("Edit")

complete_btn = sg.Button("Complete")

exit_btn = sg.Button("Exit")

window = sg.Window('Todo List App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_btn],
                           [complete_btn, exit_btn]],
                   font=("Helvetica", 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.list_r()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            functions.todos_w(todos)
            window['todos'].update(values=todos)
        case "Edit":
            selected_todo = values['todos'][0]
            new_todo = values['todo']
            todos = functions.list_r()

            if selected_todo in todos:
                index = todos.index(selected_todo)
                todos[index] = new_todo
                functions.todos_w(todos)
                window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0].replace("\n", ""))
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.list_r()
            todos.remove(todo_to_complete)
            functions.todos_w(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            window.close()
        case sg.WIN_CLOSED:
            break

window.close()
