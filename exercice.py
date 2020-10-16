#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    
    new_dict = {}
    for i in some_list:
        new_dict[i] = some_list.index(i)
    return new_dict

def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    #coloursHex = []
    #for color in colors:
    #    coloursHex.append((color, cnames[color]))
    #return coloursHex
    
    return [(color, cnames[color]) for color in colors]

def odd_integer_for_loop(end: int) -> list:
    odd_numbers = []
    for number in range (end+1):
        if number % 2 == 1:
            odd_numbers.append(number)
    return odd_numbers


def odd_integer_list_comprehension(end: int) -> list:
    return [num for num in range(end+1) if num % 2 == 1]

def loop_traversal(integers: list) -> None:
    for index, banane in enumerate(integers):
        print(index,banane)


def word_dict_for_loop(words) -> dict:
    
    new_dict = {}
    for word in words:
        new_dict[word[0].upper()] = word
    return new_dict


def word_dict_comprehension(words) -> dict:
    return {word[0].upper(): word for word in words}


def dictionary_traversal(words: dict) -> None:
    for index, (key, value) in enumerate(sorted(words.items(), key=lambda x: x[0])):
        print(index, key, value)

    for index, key in enumerate(sorted(words.keys())):
        print(index, key, words[key])
        
    

def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_for_loop(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")
    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")
    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initialisation", "ajout", "modification", "suppression", "dictionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")   
    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")
    loop_traversal(words_comprehension)


if __name__ == '__main__':
    main()
