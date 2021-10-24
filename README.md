# ethics_query 🔎

This Python function takes the name of an entity, such as a brand, and prints English-language ethics information from webpages with matching names.

## Scope
### Sites it can currently check
- General
  - [B Corp](https://bcorporation.net/directory)
  - [Ethical Consumer](https://www.ethicalconsumer.org/)
  - [Wikipedia](https://en.wikipedia.org/)
- Fashion
  - [Good on You](https://directory.goodonyou.eco/)
- Banks
  - [BankTrack](https://www.banktrack.org/)
  - [Global Alliance for Banking on Values](https://www.gabv.org)

### Sites that could be used but are harder to analyze due to JavaScript use
- [1% for the Planet](https://directories.onepercentfortheplanet.org/)
- [Bank Green](https://bank.green/)
- [The Good Shopping Guide](https://thegoodshoppingguide.com)

### Sites that could presumably be added in the future
- [Climate Friendly Supermarkets](https://www.climatefriendlysupermarkets.org/scorecard)
- [CSRHub](https://www.csrhub.com/csrhub-restful-api), which is conceptually similar to this project but caters more to corporate actors than consumers and seems lacking in terms of design, transparency, accessibility, and respect for user privacy
- [WWF Palm Oil Buyers Scorecard](http://palmoilscorecard.panda.org/#/scores)
- EWG [Skin Deep](https://www.ewg.org/skindeep/) and [Foodscores](https://www.ewg.org/foodscores/) guides
- [Open Food Facts](https://fr-en.openfoodfacts.org/data)
- [Mighty Deposits](https://mightydeposits.com/)
- [OpenSecrets](https://www.opensecrets.org/federal-lobbying/top-spenders)

For nonprofits, info from ProPublica Nonprofit Explorer, Guidestar, and Charity Navigator could be added. This data is organized by Employer Identification Number (EIN), so a separate function may be appropriate.

## Example

Here is a test with Veja, a shoe company.

	>>> ethics_query("Veja", is_fashion = True)
	👍 accepted Veja as entity to query
	👀 found B Corps entity profile at https://bcorporation.net/directory/veja
	⚫️ overall B Impact Score: 84.2/200
	🐢 still checking
	👀 found Good On You entity profile at https://directory.goodonyou.eco/brand/veja
	🙂 overall score: 4/5, good
	🌎 planet score: 4/5
	👥 people score: 5/5
	🦋 animals score: 3/5
	🔎 search complete
