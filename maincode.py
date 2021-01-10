import joblib
loaded_model = joblib.load('donebyme.pkl')
print(".....")


from googletrans import Translator

import io
import urllib.request as urllib2

import requests

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split

from sklearn.utils import shuffle

from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import chi2
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

import re


from sklearn.svm import LinearSVC
import io
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
ps = PorterStemmer()
import string
import random
#ignore
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()





def wait_for_internet_connection():
  while True:
    try:
      print("...")
      response = urllib2.urlopen('https://www.amazon.in/',timeout=3)
      return
    except urllib2.URLError:
      pass


#this bag of wors will have all the text present in all urls(i.e total text)
def listToString(s):  
    # initialize an empty string
    str1 = ""  
   
    # traverse in the string  
    for ele in s:  
        str1 = str1 + " " + ele  
   
    # return string  
    return str1  
       
def Doall(string_url):
  if string_url[0:3] == "htt":
    url_1 = string_url
    url_2 = string_url
  else:
    url_1 = "https://"+string_url
    url_2 = "http://"+string_url

  try:
    try:
      wait_for_internet_connection()
      print("Trying With->")
      print(url_1)
      source = requests.get(url_1, allow_redirects=True)
      code = source.status_code
      print(source.url)
      source = source.text
      soup = BeautifulSoup(source, features='lxml')
      for script in soup(["script", "style"]):
        script.extract()    # rip it out
      text = soup.get_text()

      # break into lines and remove leading and trailing space on each
      lines = (line.strip() for line in text.splitlines())
      # break multi-headlines into a line each
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
          # drop blank lines
      text = ', '.join(chunk for chunk in chunks if chunk)
      text = text.replace(',', ' ')
      text = text.replace(',', '')
      punctuations = '''!()-[]{};:'"\,|<>./?@#$%^&*_~'''

      # traverse the given string and if any punctuation
      # marks occur replace it with null
      for x in text.lower():
        if x in punctuations:
          text = text.replace(x, "")

      l = text.split(" ")
      mn = [translator.translate(k) for k in l]
      #removing ' ' elements
      done = [i for i in mn if i != '']
      #convert to string
      done = [str (item) for item in done]


      for i in range(0, len(done)):
        if done[i] not in no_duplicates:
          no_duplicates.append(done[i])
      # duplicates removed
      #stemming start
      ans = [ps.stem(w) for w in done]
      retrntext = listToString(ans)

      #stemming end
      #filling the bag of words

      return retrntext
    except:
      wait_for_internet_connection()
      print("Trying with->")
      print(url_2)
      source = requests.get(url_2, allow_redirects=True)
      code = source.status_code
      print(source.url)
      print(code)
      source = source.text

      soup = BeautifulSoup(source, features='lxml')
      for script in soup(["script", "style"]):
        script.extract()    # rip it out
      text = soup.get_text()

      # break into lines and remove leading and trailing space on each
      lines = (line.strip() for line in text.splitlines())
      # break multi-headlines into a line each
      chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
      # drop blank lines
      text = ', '.join(chunk for chunk in chunks if chunk)
      text = text.replace(',', ' ')
      text = text.replace(',', '')
      punctuations = '''!()-[]{};:'"\,|<>./?@#$%^&*_~'''

      # traverse the given string and if any punctuation
      # marks occur replace it with null
      for x in text.lower():
        if x in punctuations:
            text = text.replace(x, "")
      l = text.split(" ")
      #removing ' ' elements
      done = [i for i in l if i != '']
      #convert to string
      done = [str (item) for item in done]
      # duplicates removed
      #stemming start
      ans = [ps.stem(w) for w in done]
      #stemming end
      #stemming end
      #filling the bag of words
      retrntext = listToString(ans)
      return retrntext
  except:
    print("cannot open this url")
    print(string_url)
    #if url was not succesfully opened
    return " "
    pass


def dataframpredict(datafr):
  length_of_data_fram = len(datafr)
  temp = [[]]
  l = []
  j = 0
  print(j)
  j+=1
  tmn = Doall(datafr)
  if len(tmn) < 100:
  print("##############################")
  print('there was an issue...')
  print("##############################")
  print(tmn)
  l.append(tmn)
  return l
print("...")
while True:
xyz = input()
xyz = dataframpredict(xyz)

result = loaded_model.predict(xyz)
result_confidence = loaded_model.predict_proba(xyz)
print(result)
print(result_confidence)

Confidence_array = ["Arts & Entertainment", "Autos & Vehicles", "Beauty & Fitness", "Books & Literature",
"Business & Industry", "Career and Education", "Comps & Electronics", "Finance", "Food & Drink", "Games", "Health", "Law & Government", "News & Media", "Pets & Aimals",
"Recreation & Hobbies", "Reference", "Science", "Shopping", "Sports", "travel"]

for i in range(0, len(result_confidence[0])):
print(result_confidence[0][i], "-->", Confidence_array[i])