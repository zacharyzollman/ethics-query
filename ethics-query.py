import requests
import re
from bs4 import BeautifulSoup

def standardize_entity(entity):
    """
    returns a entity string with lowercase letters and dashes instead of spaces and prints the altered version
    >>> standardize_entity("The North Face")

    """
    entity = str(entity)
    # replace spaces with dashes
    entity = entity.replace(' ', '-')
    ## make entity lowercase
    #replace spaces with -?

    print("👍 accepted " + entity + " as entity to query")
    return entity

def good_on_you_checker(entity):
    entity = entity.lower()
    good_on_you_url = 'https://directory.goodonyou.eco/brand/' + entity
    ## get response from Good On You URL
    good_on_you_response = requests.get(good_on_you_url)
    ## parse page text
    good_on_you_response_parsed = BeautifulSoup(good_on_you_response.text, 'html.parser')
    ## get cleaner text
    good_on_you_text = good_on_you_response_parsed.get_text()
    pattern = re.compile("Rated*:*:")
    if pattern.search(good_on_you_text) != None:
        Good_On_You_listed = True
        print("👀 found Good On You entity profile at " + good_on_you_url)
        # find index of text
        overall_good_on_you_rating_index = good_on_you_text.index("Rated: ")
        # retrieve text at index
        good_on_you_overall_score_text = good_on_you_text[overall_good_on_you_rating_index+7:overall_good_on_you_rating_index+22]

        #patterns to look for
        great_pattern = re.compile("Great")
        not_good_enough_pattern = re.compile("Not good enough")
        good_pattern = re.compile("Good")
        its_a_start_pattern = re.compile("It's a start")
        we_avoid_pattern = re.compile("We avoid")

        if great_pattern.search(good_on_you_overall_score_text) != None:
            print("😃 overall score: 5/5, great!")
        elif not_good_enough_pattern.search(good_on_you_overall_score_text) != None:
            print("🙁 overall score: 2/5, not good enough")
        elif good_pattern.search(good_on_you_overall_score_text) != None:
            print("🙂 overall score: 4/5, good")
        elif its_a_start_pattern.search(good_on_you_overall_score_text) != None:
            print("😐 overall score: 3/5, it's a start")
        elif we_avoid_pattern.search(good_on_you_overall_score_text) != None:
            print("😧 overall score: 1/5, we avoid")
        

        #get subscores
        #"Planet\d" "People\d" "Animals\d"
        planet_good_on_you_rating_index = good_on_you_text.index('Planet')
        print("🌎 planet score: " + good_on_you_text[planet_good_on_you_rating_index + len('Planet')] + "/5")
        people_good_on_you_rating_index = good_on_you_text.index('People')
        print("👥 people score: " + good_on_you_text[people_good_on_you_rating_index + len('People')] + "/5")
        animals_good_on_you_rating_index = good_on_you_text.index('Animals')
        print("🦋 animals score: " + good_on_you_text[animals_good_on_you_rating_index + len('Animals')] + "/5")


    elif pattern.search(good_on_you_text) == None:
        Good_On_You_listed = False
    return Good_On_You_listed

def b_corps_checker(entity):
    b_corps_url = 'https://bcorporation.net/directory/' + entity
    ## get response from B Corps URL
    b_corps_response = requests.get(b_corps_url)
    ## parse page text
    b_corps_response_parsed = BeautifulSoup(b_corps_response.text, 'html.parser')
    ## get cleaner text
    b_corps_text = b_corps_response_parsed.get_text()
    pattern = re.compile("B Impact Score")
    if pattern.search(b_corps_text) != None:
        b_corps_listed = True
        print("👀 found B Corps entity profile at " + b_corps_url)
        # find index of text
        overall_b_corps_rating_index = b_corps_text.index("Overall B Impact Score")
        # retrieve text at index
        b_corps_overall_score_text = b_corps_text[overall_b_corps_rating_index+len('Overall B Impact Score')+43:overall_b_corps_rating_index+len('Overall B Impact Score')+50]
        b_corps_overall_score = str(float(b_corps_overall_score_text))
        print("⚫️ overall B Impact Score: " + b_corps_overall_score + "/200")
    elif pattern.search(b_corps_text) == None:
        b_corps_listed = False
    return b_corps_listed


def wikipedia_checker(entity):
    wikipedia_url = 'https://en.wikipedia.org/wiki/' + entity
    ## get response from B Corps URL
    wikipedia_response = requests.get(wikipedia_url)
    ## parse page text
    wikipedia_response_parsed = BeautifulSoup(wikipedia_response.text, 'html.parser')
    ## get cleaner text
    wikipedia_text = wikipedia_response_parsed.get_text()
    noname = re.compile("Wikipedia does not have an article with this exact name")
    disambiguation = re.compile("Disambiguation pages")
    if noname.search(wikipedia_text) == None and disambiguation.search(wikipedia_text) == None:
        wikipedia_listed = True
        print("👀 found Wikipedia entity article at " + wikipedia_url)
        # find index of text
        controversies = re.compile("Controversies")
        if controversies.search(wikipedia_text) != None:
            wikipedia_controversies_index = wikipedia_text.index("Controversies")
            # retrieve text at index
            wikipedia_controversy_text = wikipedia_text[wikipedia_controversies_index:wikipedia_controversies_index+150]
            print("~~~")
            print(wikipedia_controversy_text)
            print("~~~")
    elif noname.search(wikipedia_text) != None or disambiguation.search(wikipedia_text) != None:
        wikipedia_listed = False
    return wikipedia_listed



def bank_track_checker(entity):
    #entity = entity.replace("-", "_")

    company_url = "https://www.banktrack.org/company/" + entity
    bank_url = "https://www.banktrack.org/bank/" + entity

    company_response = requests.get(company_url)
    bank_response = requests.get(bank_url)

    ## parse page text
    company_response_parsed = BeautifulSoup(company_response.text, 'html.parser')
    bank_response_parsed = BeautifulSoup(bank_response.text, 'html.parser')
    ## get cleaner text
    company_text = company_response_parsed.get_text()
    bank_text = bank_response_parsed.get_text()

    notfound = re.compile("404")
    if notfound.search(company_text) != None and notfound.search(bank_text) != None:
        listed = False
    elif notfound.search(company_text) == None and notfound.search(bank_text) != None:
        listed = True
        print("👀 found BankTrack entry at " + company_url)
    elif notfound.search(company_text) != None and notfound.search(bank_text) == None:
        listed = True
        print("👀 found BankTrack entry at " + bank_url)
        # could try to extract impact description from pdfs because addresses seem standardized
        # example: https://www.banktrack.org/company/bunge/pdf
    return listed


def gabv_checker(entity):
    url = "https://www.gabv.org/members/" + entity
    response = requests.get(url)
    ## parse page text
    response_parsed = BeautifulSoup(response.text, 'html.parser')
    ## get cleaner text
    text = response_parsed.get_text()
    notfound = re.compile("404")
    if notfound.search(text) != None:
        listed = False
    elif notfound.search(text) == None:
        listed = True
        print("👀 listed as a member of the Global Alliance for Banking on Values at " + url)
    return listed



def multi_checker(entity):
    # add BBB
    # add banking info
    # for nonprofits, could add ProPublica Nonprofit Explorer, Guidestar, Charity Navigator
    good_on_you_listed = good_on_you_checker(entity)
    b_corps_listed = b_corps_checker(entity)
    wikipedia_listed = wikipedia_checker(entity)
    bank_track_listed = bank_track_checker(entity)
    gabv_listed = gabv_checker(entity)

    if good_on_you_listed == False and b_corps_listed == False and wikipedia_listed == False and bank_track_listed == False and gabv_listed == False:
        return False
    else:
        return True

def ethics_query(entity):

    entity = standardize_entity(entity)
    entity_found = multi_checker(entity)
    if entity_found == False:
        print("🔎 nothing so far...")
    
    entity_inc = entity + '-inc'
    entity_ltd = entity + '-ltd'
    entity_llc = entity + '-l-l-c'
    entity_underscores = entity.replace("-", "_")
    entity_spaces = entity.replace("-", "%20")
    entity_nospaces = entity.replace("-", "")

    entity_inc_found = multi_checker(entity_inc)
    print("🌀 checking name variants")
    entity_ltd_found = multi_checker(entity_ltd)
    print("⏳ still checking")
    entity_llc_found = multi_checker(entity_llc)
    if entity != entity_nospaces:
        entity_underscores_found = multi_checker(entity_underscores)
        entity_spaces_found = multi_checker(entity_spaces)
        entity_nospaces_found = multi_checker(entity_nospaces)

    #check for variants like with inc at the end?
    print("🔎 nothing else found")

    # could add variant with dashes between capitalized consecutive letters 
    # because B Corps seems to do this for initialisms
    # for example NAAK INC becomes https://bcorporation.net/directory/n-a-a-k-i-n-c
    # could also remove periods because B Corps seems to do this
    # like for dev.f they have https://bcorporation.net/directory/devf