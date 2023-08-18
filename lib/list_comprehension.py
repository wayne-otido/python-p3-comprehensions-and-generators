#!/usr/bin/env python3

def return_evens(num_list):
    even_list = ([n for n in num_list if(n % 2)==0])
    print(even_list)
    return(even_list)

def make_exclamation(sentence_list):
    exclam_list = ([f"{n}!" for n in sentence_list])
    print(exclam_list)
    return(exclam_list)

return_evens([0, 1, 3, 5, 7, 8, 9])
make_exclamation(["Hello", "I'm doing great", "Python is fun"])