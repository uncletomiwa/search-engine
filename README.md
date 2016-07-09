
# search-engine

This is the readme for the Webmarks search engine. The search engine allows user to perform keyword searches through a set of outlets the science community trusts. (blogs, news, facebook groups/pages, scholarly and governmental databases)

### Input:
1. Elastic search database containing articles like this:
```
{
	"publish_date": "2015-03-12T00:00:00",
	"body_text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
	tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
	quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
	consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
	cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
	proident, sunt in culpa qui officia deserunt mollit anim id est laborum.l",
	"keywords": "lorem, labore, mollit",
	"title": "Lorem ipsum dolor sit amet",
	"authors": ["Lorem", "Ipsum"],
	"uri": "http://www.lorem.example/",
	"tags": ["lorem", "labore", "mollit"],
	"summary": "Lorem ipsum dolor sit amet, consectetur adipisicing elit"
}
```
2. Article to be matched. An example could look like this:
```
Cenk Uygur, John Iadaola, Jimmy Dore, and Ben Mankiewicz of The Young Turks discuss the reactions by Fox News and others to the recent police shooting in Ferguson, Michigan.\n\nFox News became the scene of a heated debate when Kristen Powers and Andrea Tantaros got into a heated debate over the Ferguson, Michigan shootings against police officers. Tantaros blamed Obama, claiming that the Department of Justice and the Obama Administration were to blame for emboldening the people of Ferguson to fire weapons at police officers. Powers countered that there were shootings against cops before Obama and there likely would be after. This debate was started by Fergusons Police Chief retiring recently over reports of racism in the Police Department.\n\nThe unrest in Ferguson continues, sparked by the killing of Michael Brown when he assaulted Officer Darren Wilson.\n\nIs Fox News wrong to blame Obama? Let us know what you think in the comments section below.\n\nRead more here: http://www.mediaite.com/tv/foxs-powers-and-tantaros-battle-over-ferguson-blame-cops-got-shot-before-obama/
```
### Processing:
Return the most relevant articles that match the articles in elastic search.
Relevance is computed in the following order:
- Title
- Keywords
- tags
- NLP (Automatic Analysis done by Newspaper3k)
- Summary (Summary delivered by the page itself)
- authors
- text

# Modules
## Test indexing script
The indexing script pushes the test articles into elastic search
## Relevance query
This is a query to elastic search that returns articles in decreasing order of relevance
## Search Service
As a POC, a simple flask app that provides an api to elastic search.
# install
```
python virtualenv .venv
. .venv/bin/activate
pip install
python init.py
```