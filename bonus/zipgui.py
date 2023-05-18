import PySimpleGUI as sg
import zipfile as zf
import pathlib as pl
import threading


def make_arc(filepaths_lc, dest_dir, filename):
    dest_path = pl.Path(dest_dir, filename)
    with zf.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths_lc:
            filepath = pl.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def compress_files(filepaths_lc, folder_lc, zipname_lc):
    if filepaths_lc and folder_lc and zipname_lc:
        make_arc(filepaths_lc, folder_lc, f"{zipname_lc}.zip")
        window['output'].update(value="Compression complete", text_color="green")
    else:
        window['output'].update(value="Please fill all the required fields", text_color="red")


label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
btn1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
btn2 = sg.FolderBrowse("Choose", key='folder')

label3 = sg.Text("Zip name: ")
input3 = sg.Input(key='zipname')
btn3 = sg.Button("Compress", key='compress')

label4 = sg.Text(key='output')

window = sg.Window("File compressor", layout=[[label1],
                                              [input1, btn1],
                                              [label2],
                                              [input2, btn2],
                                              [label3],
                                              [input3, btn3],
                                              [label4]])

while True:
    event, values = window.read()
    if event == 'compress':
        filepaths = values["files"].split(';')
        folder = values["folder"]
        zipname = values["zipname"]
        threading.Thread(target=compress_files, args=(filepaths, folder, zipname)).start()
    elif event == sg.WIN_CLOSED:
        break

window.close()
