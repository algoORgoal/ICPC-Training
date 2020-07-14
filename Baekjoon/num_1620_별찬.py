# name: 나는야 포켓몬 마스터 이다솜
# date: July 14, 2020
# status: solved

from sys import stdin


def solution():
    total_pokemons, total_quizzes = list(map(int, stdin.readline().split(' ')))
    numbering_book = {}
    naming_book = {}
    for i in range(total_pokemons):
        pokemon = stdin.readline()
        if '\n' in pokemon:
            pokemon = pokemon[:-1]
        numbering_book[i + 1] = pokemon
        naming_book[pokemon] = i + 1
    for i in range(total_quizzes):
        quiz = stdin.readline()
        if '\n' in quiz:
            quiz = quiz[:-1]
        if quiz in naming_book:
            print(naming_book[quiz])
        elif int(quiz) in numbering_book:
            print(numbering_book[int(quiz)])


solution()
