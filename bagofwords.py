import os
import sys
from operator import itemgetter
global filepath
global query
global result
global rs
global ranks
ranks=[]
rs={}
result=[]
def main(filepath,query):
   #print()
   bag_of_words = {}
   with open(filepath) as fp:
       cnt = 0
       for line in fp:

           #print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
   sorted_words = order_bag_of_words(bag_of_words, desc=True)

   countlist=[dict(sorted_words)[k] for k in query if k in dict(sorted_words)]
   return_link(countlist,filepath)
   
def return_link(countlist,filepath):
   a=countlist
   b=filepath
   result.append([a,b])


def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           #print(word)
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1


def assign(filepath,query):
   main(filepath,query)

def rst():
    ranks=sorted(result, key=itemgetter(0), reverse=True)
    for i in range(7):
        print(ranks[i][1])


  
