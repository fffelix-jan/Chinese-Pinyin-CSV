# Chinese and Pinyin CSV Maker
# (designed for Quizlet)
# Copyright (c) 2020 Felix An
# Licenced under the MIT License: https://opensource.org/licenses/MIT
import pinyin   # You must install this module using pip
import csv

inFile = open("input.txt", "r")
characters = inFile.readlines()
inFile.close()

characters = [ele.strip() for ele in characters]

for ca, xa in enumerate(characters):
    characters[ca] = [characters[ca], pinyin.get(characters[ca])]

with open("output.csv", "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(characters)
