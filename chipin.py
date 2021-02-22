# Chinese and Pinyin CSV Maker
# (designed for Quizlet)
# Copyright (c) 2020 Felix An
# Licenced under the MIT License: https://opensource.org/licenses/MIT
import pinyin   # You must install this module using pip
import csv

inFile = open("input.txt", "r", encoding="utf-8")
characters = inFile.readlines()
inFile.close()

characters = [ele.strip() for ele in characters]

for ca, xa in enumerate(characters):
    characters[ca] = [characters[ca], pinyin.get(characters[ca], format="diacritical", delimiter=' ')]

with open("output.csv", "w", encoding="utf-8") as csvFile:
    writer = csv.writer(csvFile, lineterminator='\n')
    writer.writerows(characters)
