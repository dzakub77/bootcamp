# napis funkcje ktore otwieraja, wczytuja i zamykaja plik
#
import sys
import pickle

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Niestety otworzenie tego pliku nie jest możliwe")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    return line

def next_block(the_file):
    category = next_line(the_file)
    number = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, number, question, answers, correct, explanation

def welcome(title):
    print("Witamy w quizie")
    print(title)
def main():
    f = open_file("quiz.txt", 'r')
    title = next_line(f)
    welcome(title)
    score = 0
    category, number, question, answers, correct, explanation = next_block(f)
    while category:
        print(category)
        print(number)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        answer = input("Podaj swoją odpowiedź: ")
        if answer == correct:
            print("Brawo twoja odpowiedz jest prawidlowa")
            if number == "1\n":
                score += 4
            elif number == "2\n":
                score += 7
        else:
            print("Niestety odpowiedz jest nieprawidlowa!")
        print(explanation)
        print(f"Wynik {score}")
        category, number, question, answers, correct, explanation = next_block(f)
    f.close()
    print("To bylo ostatnie pytanie! twoj wynik: ", score)
main()