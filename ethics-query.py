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





# 1% for the Planet
    ## identify 1% for the Planet URL to check
    ## I think I need to use something other than BeautifulSoup bc there isn't much html to compare here
"""def one_percent_planet_checker(entity):

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
    return one_percent_planet_listed"""

# "Wikipedia does not have an article with this exact name" or "Disambiguation pages"
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

"""
def ewg_skindeep(entity):
    entity_spaces = entity.replace("-", "%20")
    url = "https://www.ewg.org/skindeep/search/?brand=" + entity_spaces
    response = requests.get(url)
    ## parse page text
    response_parsed = BeautifulSoup(response.text, 'html.parser')
    ## get cleaner text
    text = response_parsed.get_text()
    print(text[500:1000])
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

#https://www.gabv.org/members/bankmecu


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
    # add good shopping guide 
    # add banking info
    # add EWG?
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








"""
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/>
<title>1% for the Planet</title>
<base href="/"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<meta content="Mp0BlVwthSFT2FHMTSqJJzR-EdHWWQR65fxVvhFh8YQ" name="google-site-verification"/>
<link href="favicon.ico" rel="icon" type="image/x-icon"/>
<link href="https://fonts.gstatic.com" rel="preconnect"/>
<style type="text/css">@font-face{font-family:'Montserrat';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_ZpC3gTD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_ZpC3g3D_vx3rCubqg.woff2) format('woff2');unicode-range:U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_ZpC3gbD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_ZpC3gfD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:500;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_ZpC3gnD_vx3rCs.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:600;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_bZF3gTD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:600;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_bZF3g3D_vx3rCubqg.woff2) format('woff2');unicode-range:U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:600;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_bZF3gbD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:600;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_bZF3gfD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:600;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_bZF3gnD_vx3rCs.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_c5H3gTD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_c5H3g3D_vx3rCubqg.woff2) format('woff2');unicode-range:U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_c5H3gbD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_c5H3gfD_vx3rCubqg.woff2) format('woff2');unicode-range:U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;}@font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url(https://fonts.gstatic.com/s/montserrat/v18/JTURjIg1_i6t8kCHKm45_c5H3gnD_vx3rCs.woff2) format('woff2');unicode-range:U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;}</style>
<style type="text/css">@font-face{font-family:'Material Icons';font-style:normal;font-weight:400;src:url(https://fonts.gstatic.com/s/materialicons/v111/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2) format('woff2');}.material-icons{font-family:'Material Icons';font-weight:normal;font-style:normal;font-size:24px;line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-feature-settings:'liga';-webkit-font-smoothing:antialiased;}</style>
<style>body,html{height:100%;}body{margin:0;font-family:Montserrat,sans-serif;}</style><link href="styles.f3ce7901c1ab74e8f5a0.css" media="print" onload="this.media='all'" rel="stylesheet"/><noscript><link href="styles.f3ce7901c1ab74e8f5a0.css" rel="stylesheet"/></noscript></head>
<body>
<app-root></app-root>
<script defer="" src="runtime.deda6d5714f05a7fb9ff.js"></script><script defer="" src="polyfills.0d16e43ab1484b03a145.js"></script><script defer="" src="main.3cef231db7721aea9b29.js"></script>
</body></html>
"""