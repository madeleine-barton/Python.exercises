# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:58:06 2018

@author: bar823
"""

# 5. Hamming distance - where two strings differ
# Determine the hamming distance of two strings
# Signature: string + string -> int


def hamming(string1, string2):

    """Determine the hamming distance of two strings

    >>>hamming(AAA, TTT):
    return(3)
    >>>hamming(AAA, AAA):
    return(0)

    """
    hamming_dist = 0
    for i in range(len(string1)):
        if(string1[i] != string2[i]):
            hamming_dist = hamming_dist + 1

    return(hamming_dist)


path = 'C:/Users/bar823/Documents/MGB docs/Data School/Python/rosalind_hamm.txt'
my_strings = open(path).read()
my_strings = my_strings.split()
str1 = my_strings[0]
str2 = my_strings[1]

print(hamming(str1, str2))


# 5. Hamming distance - where two strings differ
# Determine the hamming distance of two strings
# Signature: string(file path) -> int

def hamming_fromfile(file_path):

    """Determine the hamming distance of two strings

    >>>hamming(AAA, TTT):
    return(3)
    >>>hamming(AAA, AAA):
    return(0)

    """
    my_strings = open(file_path).read().split()
    string1 = my_strings[0]
    string2 = my_strings[1]

    hamming_dist = 0
    for i in range(len(string1)):
        if(string1[i] != string2[i]):
            hamming_dist = hamming_dist + 1

    return(hamming_dist)


path = 'C:/Users/bar823/Documents/MGB docs/Data School/Python/rosalind_hamm.txt'
print(hamming_fromfile(path))
