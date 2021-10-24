"""
def good_shopping_guide_checker(entity):
    url_list = ["https://thegoodshoppingguide.com/subject/printers/"]
    listed = False
    for url in url_list:
        response = requests.get(url)
        ## parse page text
        response_parsed = BeautifulSoup(response.text, 'html.parser')
        ## get cleaner text
        text = response_parsed.get_text()
        print(text)
        entity_present = re.compile(entity)
        if entity_present.search(text) != None:
            listed = True
            print("👀 listed on the Good Shopping Guide at " + url)
    return listed
    """

"""
def bank_green_checker(entity):
    entity_underscores = entity.replace("-", "_")
    url = "https://bank.green/banks/" + entity_underscores
    response = requests.get(url)
    ## parse page text
    response_parsed = BeautifulSoup(response.text, 'html.parser')
    ## get cleaner text
    text = response_parsed.get_text()
    print(response)
    notfound = re.compile("not found")
    if notfound.search(text) != None:
        listed = False
    elif notfound.search(text) == None:
        listed = True
        print("👀 found bank.good entry at " + url)
        rating_index = text.index("Your bank is ") + len("Your bank is ")
        rating = text[rating_index: rating_index + 7]
        print("🏦 bank.green lists this as " + rating)
    return listed
"""

# 1% for the Planet
    ## identify 1% for the Planet URL to check
    ## I think I need to use something other than BeautifulSoup bc there isn't much html to compare here
"""
def one_percent_planet_checker(entity):

    one_percent_planet_url = 'https://directories.onepercentfortheplanet.org/profile/' + entity
    ## get response from Good On You URL
    one_percent_planet_response = requests.get(one_percent_planet_url)
    ## parse page text
    one_percent_planet_response_parsed = BeautifulSoup(one_percent_planet_response.text, 'html.parser')
    ## get cleaner text
    one_percent_planet_text = one_percent_planet_response_parsed.get_text()
    pattern = re.compile("ocation")
    if pattern.search(one_percent_planet_text) != None:
        one_percent_planet_listed = True
        print("Listed on 1% for the planet directory at " + one_percent_planet_url)
    elif pattern.search(one_percent_planet_text) == None:
        one_percent_planet_listed = False
    return one_percent_planet_listed
"""

"""
def ewg_skindeep(entity):
    entity_spaces = entity.replace("-", "%20")
    url = "https://www.ewg.org/skindeep/search/?brand=" + entity_spaces
    response = requests.get(url)
    ## parse page text
    response_parsed = BeautifulSoup(response.text, 'html.parser')
    ## get cleaner text
    text = response_parsed.get_text()
    print(response)
    pdt = re.compile("0 items that")
    if pdt.search(text) != None:
        ewg_listed = False
        # get text at index
    elif pdt.search(text) == None:
        ewg_listed = True
        product_index = text.index("items that")
        number_of_products = text[product_index - 3: product_index]
        print(str(float(number_of_products)) + " products in Skin Deep database")

    return ewg_listed
"""

