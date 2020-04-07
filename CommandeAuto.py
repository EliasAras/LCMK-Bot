#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:27:01 2020

@author: elias
"""

from selenium import webdriver
import time

#Connection/Requete sql
import sqlrequest as sqr

chromedriver = "/Users/elias/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
                   
size_converter = {str((i+330)/10):str(i/10) for i in range(70,150,5)}

#For Nike
def nike():
    driver.get("https://www.nike.com/fr/t/chaussure-air-max-270-react-eng-pour-F6qMKf/CK2595-500")

    size_value = driver.find_elements_by_class_name('css-181a6of')

    size = { taille.text : 0 for taille in size_value }

    size = {}

    index_xpath = 0

    print("Quelle taille souhaitez vous ?")

    for taille in size_value:
        size[taille.text] = index_xpath
        index_xpath += 1
        print(taille.text)

    size_choose = input('Choix : ')

    size_value[ size[size_choose] ].click()

    # size_value = driver.find_element_by_xpath('//*[@id="buyTools"]/div[1]/fieldset/div/div[3]/label')
    # size_value.click()

    time.sleep(2)

    addbasket = driver.find_element_by_xpath('//*[@id="buyTools"]/div[2]/button[1]')
    addbasket.click()

    time.sleep(3)

    GoPaiement = driver.find_element_by_xpath('//*[@id="PDP"]/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/div/button[2]')
    GoPaiement.click()

    time.sleep(2)

    InvitePaiement = driver.find_element_by_xpath('//*[@id="qa-guest-checkout"]')
    InvitePaiement.click()

    time.sleep(5)

    #Info Paiement
    PrenomBox = driver.find_element_by_xpath('//*[@id="firstName"]')
    PrenomBox.send_keys('Elias')

    NomBox = driver.find_element_by_xpath('//*[@id="lastName"]')
    NomBox.send_keys('AAA')

    ManuelEnterForAdress = driver.find_element_by_xpath('//*[@id="addressSuggestionOptOut"]')
    ManuelEnterForAdress.click()

    AdresseBox = driver.find_element_by_xpath('//*[@id="address1"]')
    AdresseBox.send_keys('37 quai de grenelle')

    ZipBox = driver.find_element_by_xpath('//*[@id="postalCode"]')
    ZipBox.send_keys('75015')

    CityBox = driver.find_element_by_xpath('//*[@id="city"]')
    CityBox.send_keys('Paris')

    MailBox = driver.find_element_by_xpath('//*[@id="email"]')
    MailBox.send_keys('joadje@gmail.com')

    PhoneBox = driver.find_element_by_xpath('//*[@id="phoneNumber"]')
    PhoneBox.send_keys('0676546565')

    ContinuetoPaiementInfos = driver.find_element_by_xpath('//*[@id="shipping"]/div/div/div/form/div/div/div/div[2]/button')
    ContinuetoPaiementInfos.click()

    time.sleep(3)

    PasserauPaiement = driver.find_element_by_xpath('//*[@id="shipping"]/div/div/div/div[5]/div/button')
    PasserauPaiement.click()



#For Thenextdoor Promotions
def thenextdoor(url, article):
    driver.get(url)
    
    name_article = article
    
    index_max = 1
    path1 = '//*[@id="Collection"]/ul[1]/li['
    path2 = ']/div/a'

    path = path1 + str(index_max) + path2
    
    try:
        while True:
            article = driver.find_element_by_xpath(path)
            print(article.text)
            if name_article.upper() == article.text.upper():
                driver.get(article.get_attribute('href'))
                break
            index_max += 1
            
            path = path1 + str(index_max) + path2 

    except :
        print("L'article n'a pas été trouvé")
        
    Taille = "40.5"
    path1 = '//*[@id="ProductSection-product-template"]/div/div[2]/div/div[1]/form/div[1]/div[2]/div/div['
    path2 = ']/label/span'

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
 
    UniteTaille = driver.find_element_by_xpath('//*[@id="ProductSection-product-template"]/div/div[2]/div/div[1]/form/div[1]/div[1]')
    
    if "US" in UniteTaille.text:
        Taille = size_converter[Taille]
    if "UK" in UniteTaille.text:
        Taille = size_converter[Taille]
        
    print()

    for size in DriverTaille:
        if Taille in size.text:
            size.click()
            find = 1
            break

    if find:
        work = 0        
        while work==0 :
            try : 
                Ajouter_Panier = driver.find_element_by_xpath('//*[@id="AddToCartText-product-template"]')
                Ajouter_Panier.click()
                work = 1
                
            except Exception as e:
                print(e)
                time.sleep(1)
            
        time.sleep(3)
        driver.get("https://thenextdoor.fr/cart")
        time.sleep(5)
        Paiement = driver.find_element_by_xpath('//*[@id="shopify-section-cart-template"]/div/form/div/div[2]/div/div/div/div[3]/input[2]')
        Paiement.click()

        email = "e.aras75@gmail.com"
        passeword = "lcmkppe2020"
        adresse = "37 quai de grenelle"
        Zip = "75015"
        Ville = "Paris"
        telephone = "0687879876"

        MailBox = driver.find_element_by_xpath('//*[@id="CustomerEmail"]')
        MailBox.send_keys(email)

        PasswordBox = driver.find_element_by_xpath('//*[@id="CustomerPassword"]')
        PasswordBox.send_keys(passeword)

        Connexion = driver.find_element_by_xpath('//*[@id="customer_login"]/div/input')
        Connexion.click()
        
        AdresseBox = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]')
        AdresseBox.send_keys(adresse)
        
        ZipBox = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]')
        ZipBox.send_keys(Zip)
        
        VilleBox = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]')
        VilleBox.send_keys(Ville)
        
        TelephoneBox = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]')
        TelephoneBox.send_keys(telephone)

    elif not find:
        print("Votre taille n'est pas disponible pour cette article")


def shinzo(url, article):
    driver.get(url)

    nom = "AAA"
    prenom = "Elias"
    email = "elias.aras@edu.ece.fr"
    adresse = "35 quai de grenelle"
    Zip = "75015"
    Ville = "Paris"
    telephone = "0687879876"
    name_article = article
    Taille = "44"

    index_max = 2
    path1 = '//*[@id="center_column"]/div[2]/div['
    path2 = ']/div/div[3]/h3/a'

    path = path1 + str(index_max) + path2

    try:
        while True:
            article = driver.find_element_by_xpath(path)
            print(article.text)
            if name_article.upper() == article.text.upper():
                driver.get(article.get_attribute('href'))
                break
            index_max += 1
            
            path = path1 + str(index_max) + path2 

            if index_max == 7:
                path = '//*[@id="center_column"]/div[2]/div[7]/div/div[4]/h3/a'

    except :
        print("L'article n'a pas été trouvé")


    #Size
    index_max = 1

    path1 = '//*[@id="attributes"]/fieldset[2]/div/ul/li['
    path2 = ']/label'

    path = path1 + str(index_max) + path2

    try : 
        while True:
            taille_propose = driver.find_element_by_xpath(path)

            if Taille == taille_propose.text:
                taille_propose.click()
                time.sleep(3)
                ajouter_panier = driver.find_element_by_xpath('//*[@id="add_to_cart"]/button')
                ajouter_panier.click()

                time.sleep(5)

                break

            index_max += 1
            path = path1 + str(index_max) + path2     
            
    except :
        print("Taille indisponible")

    driver.get('https://www.shinzo.paris/fr/commande#/tunnel/etape-1/invite')
    time.sleep(5)
    PrenomBox = driver.find_element_by_xpath('//*[@id="customer_firstname"]')
    PrenomBox.send_keys(prenom)
    NomBox = driver.find_element_by_xpath('//*[@id="customer_lastname"]')
    NomBox.send_keys(nom)
    EmailBox = driver.find_element_by_xpath('//*[@id="email"]')
    EmailBox.send_keys(email)
    AdresseBox = driver.find_element_by_xpath('//*[@id="address1"]')
    AdresseBox.send_keys(adresse)
    ZipBox = driver.find_element_by_xpath('//*[@id="postcode"]')
    ZipBox.send_keys(Zip)
    VilleBox = driver.find_element_by_xpath('//*[@id="city"]')
    VilleBox.send_keys(Ville)
    TelBox = driver.find_element_by_xpath('//*[@id="phone_mobile"]')
    TelBox.send_keys(telephone)

    Etape1Fini = driver.find_element_by_xpath('//*[@id="submitGuestAccount"]')
    Etape1Fini.click()

    time.sleep(3)

    Condition = driver.find_element_by_id('uniform-cgv')
    print(Condition.is_selected())
    Condition.click()
    print(Condition.is_selected())

    Etape2Fini = driver.find_element_by_xpath('//*[@id="carrier_area"]/div/div[6]')
    Etape2Fini.click


def initstring(connection):
    liste = sqr.sqlselect(connection, "name, url, article", "ChooseArticle")
    newliste = [[0 for i in range(3)] for j in range(0,len(liste))]
    
    #Remove " from the site
    for ligne in range(len(liste)):
        for column in range(len(liste[ligne])):
            newliste[ligne][column] = liste[ligne][column].replace("'", '')
    
    return newliste

def main():
    connection = sqr.sqlconnect()
    articles = initstring(connection)
    
    for name, url, article in articles:
        if name == "Shinzo":
            shinzo(url, article)
            time.sleep(5)
        if name == "Nike":
            nike()
        if name == "TheNextDoor":
            thenextdoor(url, article)

    sqr.sqldeco(connection)



main()