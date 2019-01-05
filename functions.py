def findSearchButton(driver):
    search = driver.find_element_by_xpath('//*[@id="submit"]')
    return search

def findField(driver):
    pole = driver.find_element_by_xpath('//*[@id="id-search-field"]')
    return pole

def search2(driver):
    searchsecond=driver.find_element_by_xpath('/html/body/div/div[3]/div/section/form/p/input[1]')
    return searchsecond