import os
import PySimpleGUI as sg
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def optimize_image(file_path, compression_quality):
    image = Image.open(file_path)
    image.save(file_path, optimize=True, quality=compression_quality)
    return f"Изображение {file_path} сжато с качеством {compression_quality}%"

def convert_pdf_to_docx(file_path):
    docx_file_path = file_path.replace('.pdf', '.docx')
    converter = Converter(file_path)
    converter.convert(docx_file_path)
    converter.close()
    return f"Файл {file_path} преобразован в {docx_file_path}."

def convert_docx_to_pdf(file_path):
    convert(file_path)
    return f"Файл {file_path} преобразован в PDF."

interface_layout = [
    [sg.Text("Выберите директорию"), sg.Input(key="-DIRECTORY-", enable_events=True), sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, size=(50, 10), key="-FILES LIST-")],
    [sg.Button("Конвертировать PDF в DOCX"), sg.Button("Конвертировать DOCX в PDF"), sg.Button("Сжать изображения"), sg.Exit()]
]

window = sg.Window("Office Tweaks", interface_layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "-DIRECTORY-":
        directory = values["-DIRECTORY-"]
        try:
            file_names = os.listdir(directory)
        except FileNotFoundError:
            file_names = []
        files_in_directory = [f for f in file_names if os.path.isfile(os.path.join(directory, f))]
        window["-FILES LIST-"].update(files_in_directory)
    elif event == "-FILES LIST-":
        selected_files = values["-FILES LIST-"]
    elif event == "Конвертировать PDF в DOCX":
        for file in selected_files:
            if file.endswith(".pdf"):
                result_message = convert_pdf_to_docx(os.path.join(directory, file))
                sg.popup(result_message)
    elif event == "Конвертировать DOCX в PDF":
        for file in selected_files:
            if file.endswith(".docx"):
                result_message = convert_docx_to_pdf(os.path.join(directory, file))
                sg.popup(result_message)
    elif event == "Сжать изображения":
        for file in selected_files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                result_message = optimize_image(os.path.join(directory, file), compression_quality=50)
                sg.popup(result_message)

window.close()
