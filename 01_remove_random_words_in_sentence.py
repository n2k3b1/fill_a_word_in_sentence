#!/bin/sh
import sys
import random
import io
#import string

# number of vocabulary want to fill in the sentence
num_param = len(sys.argv)
if num_param < 3:
	print("")
	print("Usage: python 01_remove_random_words_in_sentence.py transcript.txt 10")
	print("transcript.txt: sentence content want to edit")
	print("10: number of vocabulary want to fill in the blank (......) in the sentence above")
	print("")
	exit()

else:
	# input filename parammeter on the console
	filename = sys.argv[1]
	# input number of vocabulary
	nvoc = int(sys.argv[2])
#print(sys.argv)
#exit()
# begin to process text file
f = open(filename, "r")
# read entire a sentence
sentence = f.read()
# declare array sentences variable
sentences = []
idx = []
arr_sentences = sentence.split(" ")
#print(arr_sentences)
print("")
count = len(arr_sentences)
while nvoc > 0:
	n_number_random = random.randint(1, count)
	# remove duplicated index in array
	while n_number_random in idx:
		n_number_random = random.randint(1, count)
		#print("---------------- = " + str(n_number_random))

	#else:
	idx.append(n_number_random)
	#print(idx)

	s_word_remove = arr_sentences[n_number_random]
	print(s_word_remove)
	# replace the word want to fill in a sentence
	arr_sentences[n_number_random] = '______'
	nvoc = nvoc - 1

print("")
s = ' '
sentence = s.join(arr_sentences)
print(sentence)
