to_remove = [
    ":", "-", "'", ";", ",", 
    "/", "\\", "]", "[", "(", 
    ")", "{", "}", "?", "!",  
    "."
]

def clean_string ( string ) :
    aux_string = string
    for item in to_remove:
        aux_string = aux_string.replace(item, '')
    return aux_string