#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:16:10 2019

@author: elias
"""

# Python3 program for a word frequency 
# counter after crawling a web-page 
import requests 
from bs4 import BeautifulSoup

#Connection/Requete sql
import sqlrequest as sqr

#All the word find in a website
clean_list = []

'''Function defining the web-crawler/core 
spider, which will fetch information from 
a given website, and push the contents to 
the second function clean_wordlist()'''
def recupword(url, classname): 

	# empty list to store the contents of 
	# the website fetched from our web-crawler 
	wordlist = [] 
	source_code = requests.get(url).text
    
	# BeautifulSoup object which will 
	# ping the requested url for data 
	soup = BeautifulSoup(source_code, 'html.parser') 

	# Text in given web-page is stored under 
	# the <div> tags with class <entry-content> 
	for each_text in soup.findAll('div', {'class': classname}): 
		content = each_text.text 

		# use split() to break the sentence into 
		# words and convert them into lowercase 
		words = content.lower().split() 
		lengword = len(words)
		for each_word in words: 
			wordlist.append(each_word) 
		clean_wordlist(wordlist, lengword)

# Function removes any unwanted symbols 
def clean_wordlist(wordlist, lengword): 
	 
	for word in wordlist: 
		symbols = '!@#$%^&*()_+={[}]|\;:"<>?/.,“” '
		
		for i in range (0, len(symbols)): 
			word = word.replace(symbols[i], '') 
			
		if len(word) > 0: 
			clean_list.append(word)
    
def findword(wordtofind, site):
    indice_find = 0
    
    tofind = wordtofind.split()
    
    for word in clean_list: 
        if tofind[indice_find].upper() in word.upper():
            indice_find +=1
        else :
            indice_find = 0
        
        if indice_find == len(wordtofind.split()):
            print('The word ' + wordtofind + ' is present in '+ site)
            return True
                
    print(wordtofind + ' is unfind in '+ site)
    return False

def initsites(connection):
    site = sqr.sqlselect(connection, "url, classtype, name", "SitesRef")
    newsite = [[0 for i in range(3)] for j in range(0,len(site))]
    
    #Remove " from the site
    for ligne in range(len(site)):
        for column in range(len(site[ligne])):
            newsite[ligne][column] = site[ligne][column].replace("'", '')
    
    return newsite

# Driver code 
def main(): 
    connection = sqr.sqlconnect()    
#    sqr.sqlcreate(connection)

    sites = initsites(connection)
    
    word = 'JOYRIDE ENVELOPE ISPA'
    
    for site in sites:
        recupword(site[0], site[1])
        if findword(word, site[2]) : 
            name = site[2]
            url = site[0]
            article = word
            specification = [name, url, article]
            sqr.sqladdArticle(connection, specification)
            
        clean_list[:] = []
    
    sqr.sqldeco(connection)

main()