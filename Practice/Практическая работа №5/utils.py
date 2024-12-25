import os

def get_word_list(file_name="words"):
    try:
        with open(file_name, "r", encoding="utf-8") as word_file:
            word_data = word_file.read().strip().splitlines()
        if not word_data:
            raise ValueError("Список слов пуст.")
        return word_data
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_name} не найден. Проверьте его наличие.")
    except Exception as error:
        raise Exception(f"Произошла ошибка при чтении слов: {error}")

def get_high_score(file_name="record.txt"):
    if not os.path.exists(file_name):
        return 0
    try:
        with open(file_name, "r", encoding="utf-8") as record_file:
            return int(record_file.read().strip() or 0)
    except ValueError:
        return 0

def update_high_score(new_score, file_name="record.txt"):
    try:
        with open(file_name, "w", encoding="utf-8") as record_file:
            record_file.write(str(new_score))
    except Exception as error:
        raise Exception(f"Ошибка при обновлении рекорда: {error}")