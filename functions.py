def findSearchButton(driver):
    search = driver.find_element_by_xpath('//*[@id="submit"]')
    return search

def findField(driver):
    pole = driver.find_element_by_xpath('//*[@id="id-search-field"]')
    return pole