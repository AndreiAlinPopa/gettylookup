# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:03:32 2021

@author: Andrei
"""

############################## imports ####################################

from bs4 import *
import requests as rq
import webbrowser
import time

######################### config code ########################################

def find_between( s, first='src="', last='"' ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
    
######################### webpage processing #################################

def request_webpage(search):
    
    usr_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    request_url = "https://www.gettyimages.co.uk/photos/" + search.replace(" ", "-")


    response = rq.get(request_url, headers=usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll('img', {'class':'gallery-asset__thumb gallery-mosaic-asset__thumb'})


    imagelinks = []
    for result in results:
        imagelinks.append(str(result))
        
    return imagelinks

###################### image display ##################################
    
def display_images(search, limit):
    
    link = request_webpage(search)
    counter = 0
    limit = int(limit)

    if link == []:
        print("No results found")
        return 0
    
    for value in link:
        if counter < limit:
            webbrowser.open(find_between(value))
            counter += 1
    
while True:
    print("Welcome to the Getty image retrival program")
    time.sleep(2)
    term = input("Search: ")
    quant = input("Quantity: ")
    
    print("\nJust a moment...\n")
    time.sleep(1)
    display_images(term, quant)
    time.sleep(2)
    for i in range(20):
        print("\n")