from random import choice


def is_valid_checking(str_to_check):
    if len(str_to_check) != 5 or (not (str_to_check.isalpha())):
        return 0
    if str_to_check not in open("russian_words.txt", encoding="utf-8").read():
        return 0
    return 1


def is_win(checking_value, right_answer):
    result = []
    for i, j in zip(checking_value, right_answer):
        if i == j:
            result += [j]
        elif i in right_answer:
            result += ["#"]
        else:
            result += ["0"]
    return "".join(result)


if __name__ == "__main__":
    print(
        "Добро пожаловать в игру 5 букв! Пришлите мне существительное из 5 букв, а я пришлю результат проверки в таком формате:"
        "# - буква есть в слове, но она стоит не на своем месте. 0 - буквы нет в слове. "
        "Буква написана - буква стоит на правильном месте")
    print("Давайте начнём игру! Жду Ваше слово")
    words = open("russian_words.txt", encoding="utf-8").readlines()
    right_ans = choice(words)
    game_history = []
    while len(game_history)<6:
        get_ans = input()
        str_to_print = ""
        if is_valid_checking(get_ans):
            res_checking = is_win(get_ans,right_ans)
            game_history += [f"{get_ans} - {res_checking}\n"]
            str_to_print+="- - - - - - - - - -\n"
            str_to_print+="".join(game_history)
            str_to_print+="- - - - - - - - - -\n"
            if res_checking==right_ans:
                str_to_print+="Это правильное слово!"
                break
        else:
            str_to_print+="Это слово не подходит!"
        print(str_to_print)
    else:
        print(f"У вас закончились попытки. Загаданное слово: {right_ans}")