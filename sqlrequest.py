#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:16:44 2019

@author: elias
"""

import mysql.connector 
from mysql.connector import Error

def sqlconnect():
    return mysql.connector.connect(host='localhost', 
                                   database='LCMK', 
                                   user='root', 
                                   password='root', 
                                   port='8889')

def sqlcreate(connection):
    try:    
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS SitesRef (
                                  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                                  url VARCHAR(3000),
                                  classtype VARCHAR(300),
                                  name VARCHAR(300)
                                  );
                            """)
                               
            print("SitesRef Table created successfully ")                 
                                
            cursor.execute("""
                               CREATE TABLE IF NOT EXISTS ChooseArticle (
                                  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                                  name VARCHAR(300),
                                  url VARCHAR(3000),
                                  article VARCHAR(300)
                                  );
                            """)
                               
            print("ChooseArticle Table created successfully ")
            
            filedatabase(connection)
            
            print("SitesRef Table filled successfully ")

    except Error as e:
        print("Error while connecting to MySQL", e)
        
def sqladdSite(connection, reference):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO SitesRef (url, classtype, name) 
                          VALUES("%s", "%s", "%s")""", reference)
        connection.commit()
  
def sqladdArticle(connection, reference):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO ChooseArticle (name, url, article) 
                          VALUES("%s", "%s", "%s")""", reference)
        connection.commit()    
    
def sqldelete(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("DELETE FROM SitesRef")
        connection.commit()
        cursor.execute("ALTER TABLE SitesRef AUTO_INCREMENT = 1")
        connection.commit()
    
def sqlselect(connection, specif, Table):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT "+ specif +" FROM "+ Table)
        
        
        myresult = cursor.fetchall()
        
        connection.commit()
        
        return myresult

def sqldeco(connection):
    if (connection.is_connected()):
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def addinlist(link, sites):
    sites.append(link)
     

def filedatabase(connection):
    sites = []
    
    #It's work
    name = 'TheDropDate'
    url = 'https://www.thedropdate.com'
    classname = 'main'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'FrenchRaffle'
    url = 'https://frenchraffle.com'
    classname = ''
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'SneakersNews'
    url = 'https://sneakernews.com/release-dates/'
    classname = 'wrapper'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'Shinzo'
    url = 'https://www.shinzo.paris/fr/27-chaussures-sportswear'
    classname = 'product-list-grid product_list row lg-columns-4 desktop-columns-3 tablet-columns-3 mobile-columns-2'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'FootPatrol'
    url = 'https://www.footpatrol.com/sale/'
    classname = 'splitRightContainer'
    specifications = [url, classname, name]
    #addinlist(specifications, sites)
    
    #It's work
    name = 'FootDistrict'
    url = 'https://footdistrict.com/fr/sneakers.html'
    classname = 'category-products'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'TheNextDoor'
    url = 'https://thenextdoor.fr/collections/promotions'
    classname = 'page-width'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'NoirFonce'
    url = 'https://www.noirfonce.fr/collections/coming-soon'
    classname = 'grid grid--uniform grid--collection'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'AfexStore'
    url = 'https://de.afew-store.com/collections/sneaker-releases'
    classname = 'row product-row'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #It's work
    name = 'OffSpring'
    url = 'https://www.offspring.co.uk/view/category/offspring_catalog/NEWIN?pageSize=100&sort=releaseDate'
    classname = 'productList row'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    #Pb
    name = 'TitoloShop'
    url = 'https://en.titoloshop.com/coming-soon'
    classname = 'large-12 grid-mode columns'
    specifications = [url, classname, name]
    addinlist(specifications, sites)  
    
    #It's work
    name = 'OpiumParis'
    url = 'https://www.opiumparis.com/fr/71-raffles?page=3'
    classname = 'products row'
    specifications = [url, classname, name]
    addinlist(specifications, sites)    

    #It's work
    name = 'Antonia'
    url = 'https://www.antonia.it/es/launches/'
    classname = 'launches-list row'
    specifications = [url, classname, name]
    addinlist(specifications, sites)    
    
    #It's work
    name = 'JuiceStore'
    url = 'https://juicestore.com/blogs/editorial/tagged/raffle'
    classname = 'blog--list-view'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    name = 'Nike'
    url = 'https://www.nike.com/fr/w/hommes-chaussures-nik1zy7ok'
    classname = 'product-grid css-14yqij9'
    specifications = [url, classname, name]
    addinlist(specifications, sites)
    
    for i in range(len(sites)):
        sqladdSite(connection, sites[i])
   