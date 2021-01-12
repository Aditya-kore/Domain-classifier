from flask import Flask, render_template, request
import joblib

app = Flask('url_predicturl', template_folder='C:/Users/Adi/PycharmProjects/Sample Webscraper/templates', static_folder='C:/Users/Adi/PycharmProjects/Sample Webscraper/static')
loaded_model = joblib.load('donebyme.pkl')
from googletrans import Translator
translator = Translator()
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

#app code
@app.route('/')
def opening():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        xyz = [request.form['url']]
        #print("this is xyz", xyz[0])

        def wait_for_internet_connection():
            while True:
                try:
                    response = urllib2.urlopen('https://www.amazon.in/', timeout=3)
                    return
                except urllib2.URLError:
                    pass

        # this bag of wors will have all the text present in all urls(i.e total text)
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
                url_1 = "https://" + string_url
                url_2 = "http://" + string_url
            code = 0
            source = " "
            try:
                try:
                    wait_for_internet_connection()
                    print("Trying With->")
                    print(url_1)
                    source = requests.get(url_1, allow_redirects=True)
                    code = source.status_code
                    print("Code sent ->", code)
                    print("Redirected to -> ", source.url)
                    source = requests.get(source.url, allow_redirects=True)
                    code = source.status_code
                    print("Code sent ->", code)
                    source = source.text
                    soup = BeautifulSoup(source, "lxml")
                    for script in soup(["script", "style"]):
                        script.extract()  # rip it out
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
                    # removing ' ' elements
                    done = [i for i in mn if i != '']
                    # convert to string
                    done = [str(item) for item in done]

                    for i in range(0, len(done)):
                        if done[i] not in no_duplicates:
                            no_duplicates.append(done[i])
                    # duplicates removed
                    # stemming start
                    ans = [ps.stem(w) for w in done]
                    retrntext = listToString(ans)

                    # stemming end
                    # filling the bag of words

                    return retrntext
                except:
                    wait_for_internet_connection()
                    print("Trying with->")
                    source = requests.get(url_2, allow_redirects=True)
                    code = source.status_code
                    print("Code sent ->", code)
                    print("Redirected to -->", source.url)
                    print("Code sent ->", code)
                    source = requests.get(source.url, allow_redirects=True)
                    code = source.status_code
                    print(code)
                    source = source.text
                    if str(code)[0:1] == "4":
                        raise Exception()
                    soup = BeautifulSoup(source, "lxml")
                    for script in soup(["script", "style"]):
                        script.extract()  # rip it out
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
                    # removing ' ' elements
                    done = [i for i in l if i != '']
                    # convert to string
                    done = [str(item) for item in done]
                    # duplicates removed
                    # stemming start
                    ans = [ps.stem(w) for w in done]
                    # stemming end
                    # stemming end
                    # filling the bag of words
                    retrntext = listToString(ans)
                    return retrntext
            except Exception as e:
                print(e)
                print("Error, Response Sent - ", code)
                print("Message sent-> ")
                # if url was not succesfully opened
                return " "
                pass

        def dataframpredict(datafr):
            length_of_data_fram = len(datafr)
            temp = [[]]
            l = []
            j = 0
            j += 1
            tmn = Doall(datafr)
            if len(tmn) < 50:
                print(tmn)
            l.append(tmn)
            return l

        predicted_confi = "Some error has occurred, cannot perform the categorization."
        predicted_category = "Some error has occurred, cannot perform the categorization."
        while True:
            #xyz = input("Enter the Url:")
            xyz = dataframpredict(xyz[0])
            if xyz == [" "]:
                print("Error Occured... Cannot perform the categorization")
                return render_template('index_result.html', predicted_url=predicted_category, predicted_confidence=predicted_confi)
            predicted_category = loaded_model.predict(xyz)
            predicted_confi = loaded_model.predict_proba(xyz)
            print(predicted_category)
            Confidence_array = ["Arts & Entertainment", "Autos & Vehicles", "Beauty & Fitness", "Books & Literature",
                                "Business & Industry", "Career and Education", "Comps & Electronics", "Finance",
                                "Food & Drink", "Games", "Health", "Law & Government", "News & Media", "Pets & Animals",
                                "Recreation & Hobbies", "Reference", "Science", "Shopping", "Sports", "Travel"]

            dd = []
            jj =[]
            for i in range(0, len(predicted_confi[0])):
                dd.append([((predicted_confi[0][i]) / (sum(predicted_confi[0]))) * 100, Confidence_array[i]])
            dd.sort()
            jj.append(max(map(lambda x: x[0], dd)))
            print(jj)
            for i in range(len(predicted_confi[0]) - 1, -1, -1):
                print(dd[i][1], " With a confidence level of -> ", dd[i][0])
            predicted_category = predicted_category[0]
            predicted_confi = jj[0]
            break


        #print("the url is:  ",xyz)
        #print("the category is:  ",predicted_category)
        #print("the confidence is:  ",predicted_confi)
        return render_template('index_result.html', predicted_url=predicted_category, predicted_confidence=predicted_confi)
        pass
    return 'ok'


if __name__ == '__main__':
    #app.run("localhost", "9999", debug=True)
    app.run(debug=True)
#app.run()