to_remove = [
    ":", "-",  "'", ";", ",", 
    "/", "\\", "]", "[", "(", 
    ")", "{",  "}", "?", "!",  
    "."
]

to_ignore = [
    'the',	    
    'at',	    
    'there',
    'some',	
    'my',
    'of',    
    'be',    	    
    'use',	    
    'her',	    
    'than',
    'and',	    
    'this',	
    'an',  
    'would',
    'first',
    'a',	    
    'have',	
    'each',	
    'make',	
    'to',  
    'from',	
    'which',	
    'like',	
    'been',
    'in',	    
    'or',	    
    'she',	    
    'him',	    
    'call',
    'is',	    
    'one',	    
    'do',	    
    'into',	
    'who',
    'you',	    
    'had',	    
    'how',	    
    'that',	    
    'by',	    
    'their',
    'has',	    
    'its',
    'it', 	    
    'word',	
    'if',	    
    'look',	
    'now',
    'he',	    
    'but',	    
    'will',	
    'two',	    
    'find',
    'was',	    
    'not',	    
    'up',   
    'more',	
    'long',
    'for',	    
    'what',	
    'other',	
    'write',	
    'down',
    'on',	    
    'all',	    
    'about',	
    'go',	    
    'day',
    'are',	    
    'were',	
    'out',	    
    'see',	    
    'did',
    'as',	    
    'we',	    
    'many',	
    'get',
    'with',	
    'when',	
    'then',	
    'no',	    
    'come',
    'his',	    
    'your',	
    'them',	
    'way',	    
    'made',
    'they',	
    'can',	    
    'these',	
    'could',	
    'may',
    'I',
    'i',	    
    'said',	
    'so',	
    'you',
    'he',
    'she',
    'it',
    'we',
    'they',
    'me',
    'him',
    'her',
    'its',
    'us',
    'them',
    'my',
    'your',
    'his',
    'our',
    'your',
    'their',
    'mine',
    'yours',
    'hers',
    'ours',
    'theirs',
    'myself',
    'yourself',
    'himself',
    'herself',
    'itself',
    'ourselves',
    'yourselves',
    'themselves',
    'do',
    "don't",
]

def clean_string ( string ) :
    aux_string = string
    for item in to_remove:
        aux_string = aux_string.replace(item, ',')
    return aux_string