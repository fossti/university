import random
from utils import get_word_list, get_high_score, update_high_score


def reveal_word(secret_word, revealed_letters):
    return " ".join(char if char in revealed_letters else "■" for char in secret_word)


def run_game_round(secret_word, attempts):
    revealed_letters = set()
    while attempts > 0:
        print(f"\nТекущее слово: {reveal_word(secret_word, revealed_letters)}")
        print(f"Оставшиеся попытки: {'♥ ' * attempts}")
        user_input = input("Введите букву или отгадайте слово целиком: ").strip().lower()
        if not user_input.isalpha():
            print("Ошибка: введите букву или слово.")
            continue

        if len(user_input) == 1:
            if user_input in revealed_letters:
                print("Вы уже пробовали эту букву.")
            elif user_input in secret_word:
                revealed_letters.add(user_input)
                print("Угадано!")
            else:
                attempts -= 1
                print("Ошибка. Вы теряете попытку.")
        elif user_input == secret_word:
            print(f"Поздравляем, вы угадали слово: {secret_word}!")
            return True
        else:
            attempts -= 1
            print("Неверное слово. Вы теряете попытку.")

        if set(secret_word).issubset(revealed_letters):
            print(f"Вы успешно отгадали слово: {secret_word}!")
            return True

    print(f"Вы проиграли. Загаданное слово: {secret_word}.")
    return False


def start_game():
    try:
        word_list = get_word_list()
        high_score = get_high_score()
        words_guessed = 0

        print("Добро пожаловать в игру 'Поле чудес'!")
        while word_list:
            print(f"\nТекущий рекорд: {high_score}. Угадано слов: {words_guessed}.")
            difficulty_level = input("Выберите уровень сложности (лёгкий, средний, сложный): ").strip().lower()
            attempts = {"лёгкий": 7, "средний": 5, "сложный": 3}.get(difficulty_level, 5)

            secret_word = random.choice(word_list)
            word_list.remove(secret_word)

            if run_game_round(secret_word, attempts):
                words_guessed += 1
                print("Вы победили в этом раунде!")
            else:
                break

            if not input("Хотите продолжить игру? (да/нет): ").strip().lower().startswith("д"):
                break

        print(f"Игра завершена. Вы отгадали {words_guessed} слов(а).")
        if words_guessed > high_score:
            print(f"Поздравляем! Новый рекорд: {words_guessed}.")
            update_high_score(words_guessed)
        else:
            print(f"Ваш рекорд: {high_score}.")
    except Exception as error:
        print(f"Возникла ошибка: {error}. Попробуйте снова.")