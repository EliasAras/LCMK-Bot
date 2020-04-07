#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 29 09:41:11 2020

@author: elias
"""

from selenium import webdriver
import time


# options = webdriver.ChromeOptions()
# options.add_argument("/Users/elias/Library/Application Support/Google/Chrome/Default")

chromedriver = "/Users/elias/Downloads/chromedriver"
# driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
driver = webdriver.Chrome(chromedriver)

#Google Form
def GoogleForm():
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfFPr2Oghv2mNDqfeR8188L84YvGlh27PpFxv89g5X06RJJTQ/viewform")

    Prenom = "Elias"
    Nom = "AAAA " + Prenom
    Email = "ea@gmail.com"
    Adresse = "37 quai de Grenelle, Paris"
    Telephone = "0676546565"
    Taille = "44"

    NomBox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
    NomBox.send_keys(Nom)

    MailBox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
    MailBox.send_keys(Email)

    AdressBox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea')
    AdressBox.send_keys(Adresse)

    PhoneBox = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
    PhoneBox.send_keys(Telephone)

    path1 = '//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/span/div/div['
    path2 = ']/label/div'

    path = path1 + str(1) + path2
    index_max = 1
    DriverTaille = []

    try:
        while driver.find_element_by_xpath(path):
            DriverTaille.append(driver.find_element_by_xpath(path))
            index_max += 1
            path = path1 + str(index_max) + path2  

    except :
        print("Nombre max trouver", index_max-1)

    find = 0
    for size in DriverTaille:
        if size.text == Taille:
            size.click()
            find = 1
    
    if not find:
        print("Votre taille n'est pas disponible pour cette article")

def thenextdoorraffle():
    driver.get("https://thenextdoor.fr/pages/air-jordan-1-zoom?fbclid=IwAR18XOZck6GKMzfemOF9EYpeSxYrDkhx9rhWE4isV1bKvNWmywOBM6YJZhA")

    Prenom = "Elias"
    Nom = "AAAA"
    Email = "ea@gmail.com"
    Telephone = "0676546565"
    Taille = "41"
    Insta = "adzoa"

    MailBox = driver.find_element_by_xpath('//*[@id="mce-EMAIL"]')
    MailBox.send_keys(Email)

    PrenomBox = driver.find_element_by_xpath('//*[@id="mce-FNAME"]')
    PrenomBox.send_keys(Prenom)

    NomBox = driver.find_element_by_xpath('//*[@id="mce-LNAME"]')
    NomBox.send_keys(Nom)

    PhoneBox = driver.find_element_by_xpath('//*[@id="mce-PHONE"]')
    PhoneBox.send_keys(Telephone)

    PointureBox = driver.find_element_by_xpath('//*[@id="mce-MMERGE5"]')
    PointureBox.send_keys(Taille)

    InstagramBox = driver.find_element_by_xpath('//*[@id="mce-MMERGE6"]')
    InstagramBox.send_keys(Insta)

    MajeurBox = driver.find_element_by_xpath('//*[@id="mce-MMERGE8-0"]')
    MajeurBox.click()

test()
#driver.close()

