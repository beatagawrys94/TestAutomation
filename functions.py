import unittest
from selenium import webdriver

def findSearchButton(driver):
    search = driver.find_element_by_xpath('//*[@id="submit"]')
    assert "GO" in search.text
    return search

def findField(driver):
    pole = driver.find_element_by_xpath('//*[@id="id-search-field"]')
    return pole

def search2(driver):
    searchsecond=driver.find_element_by_xpath('/html/body/div/div[3]/div/section/form/p/input[1]')
    return searchsecond

def searchbutton(driver):
    searchbutton2 = driver.find_element_by_xpath('/html/body/div/div[3]/div/section/form/p/input[2]')
    assert "Search" in searchbutton2.text
    return searchbutton2

def about(driver):
    about=driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[1]/a')
    assert "About" in about.text
    return about

def downloads(driver):
    downloads=driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[2]/a')
    assert "Downloads" in downloads.text
    return downloads

def doc(driver):
    doc=driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[3]/a')
    assert "Documentation" in doc.text
    return doc

def community(driver):
    community = driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[4]/a')
    assert "Community" in community.text
    return community

def successS(driver):
    success = driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[5]/a')
    assert "Success Stories" in success.text
    return success

def news(driver):
    new = driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[6]/a')
    assert "News" in new.txt
    return new

def events(driver):
    event = driver.find_element_by_xpath('/html/body/div/header/div/nav/ul/li[7]/a')
    assert "Events" in event.text
    return event