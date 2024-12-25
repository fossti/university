import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def switch_directory():
    new_path = input("Введите новый путь к рабочему каталогу: ")
    if os.path.isdir(new_path):
        os.chdir(new_path)
        print(f"Каталог успешно изменён на: {os.getcwd()}")
    else:
        print("Указанный каталог не существует.")

def convert_pdf_to_docx_menu():
    pdf_files = [file for file in os.listdir() if file.endswith('.pdf')]
    if not pdf_files:
        print("PDF-файлы для преобразования отсутствуют.")
        return
    for index, file in enumerate(pdf_files, start=1):
        print(f"{index}. {file}")
    selection = int(input("Выберите номер файла для преобразования (или 0 для всех): "))
    if selection == 0:
        for file in pdf_files:
            transform_pdf_to_docx(file)
    else:
        transform_pdf_to_docx(pdf_files[selection - 1])

def transform_pdf_to_docx(pdf_file):
    docx_name = pdf_file.replace('.pdf', '.docx')
    converter = Converter(pdf_file)
    converter.convert(docx_name)
    converter.close()
    print(f"Файл {pdf_file} преобразован в {docx_name}.")

def convert_docx_to_pdf_menu():
    docx_files = [file for file in os.listdir() if file.endswith('.docx')]
    if not docx_files:
        print("DOCX-файлы для преобразования отсутствуют.")
        return
    for index, file in enumerate(docx_files, start=1):
        print(f"{index}. {file}")
    selection = int(input("Выберите номер файла для преобразования (или 0 для всех): "))
    if selection == 0:
        convert('.')
    else:
        convert(docx_files[selection - 1])
    print("Преобразование завершено.")

def compress_images_menu():
    image_files = [file for file in os.listdir() if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not image_files:
        print("Файлы изображений для сжатия отсутствуют.")
        return
    for index, file in enumerate(image_files, start=1):
        print(f"{index}. {file}")
    selection = int(input("Выберите номер файла для сжатия (или 0 для всех): "))
    compression_quality = int(input("Укажите уровень качества сжатия (1-100): "))
    if selection == 0:
        for file in image_files:
            reduce_image_size(file, compression_quality)
    else:
        reduce_image_size(image_files[selection - 1], compression_quality)

def reduce_image_size(image_file, quality):
    image = Image.open(image_file)
    image.save(image_file, optimize=True, quality=quality)
    print(f"Файл {image_file} успешно сжат с качеством {quality}.")

def batch_file_removal():
    print("1. Удалить файлы, начинающиеся на заданную подстроку")
    print("2. Удалить файлы, заканчивающиеся на заданную подстроку")
    print("3. Удалить файлы, содержащие заданную подстроку")
    print("4. Удалить файлы с указанным расширением")
    action = int(input("Выберите действие: "))
    substring = input("Введите подстроку или расширение: ")
    matching_files = []
    if action == 1:
        matching_files = [file for file in os.listdir() if file.startswith(substring)]
    elif action == 2:
        matching_files = [file for file in os.listdir() if file.endswith(substring)]
    elif action == 3:
        matching_files = [file for file in os.listdir() if substring in file]
    elif action == 4:
        matching_files = [file for file in os.listdir() if file.endswith(f".{substring}")]
    for file in matching_files:
        os.remove(file)
        print(f"Файл {file} удалён.")

def main():
    while True:
        print(f"Текущий рабочий каталог: {os.getcwd()}")
        print("Выберите действие:")
        print("0. Изменить рабочий каталог")
        print("1. Преобразовать PDF в DOCX")
        print("2. Преобразовать DOCX в PDF")
        print("3. Сжать изображения")
        print("4. Удалить файлы")
        print("5. Выйти из программы")
        action = int(input("Ваш выбор: "))
        if action == 0:
            switch_directory()
        elif action == 1:
            convert_pdf_to_docx_menu()
        elif action == 2:
            convert_docx_to_pdf_menu()
        elif action == 3:
            compress_images_menu()
        elif action == 4:
            batch_file_removal()
        elif action == 5:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
