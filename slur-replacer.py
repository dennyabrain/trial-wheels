from fuzzywuzzy import process, fuzz

slurs_list_lower = ['#rheachakraborty',
 '#498a',
 '#feministmafia',
 '#carryminatiroast',
 '#justiceforswapnilpandey',
 '#arrestranaayyub',
 '#boycottfabindia',
 '#domesticviolence',
 '#dowry']

TWEET = "this is a dowry tweet"

process.extract(TWEET, slurs_list_lower, limit=10, scorer=fuzz.partial_ratio)
