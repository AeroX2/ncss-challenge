import re

pattern = "_([a-z])"
replace = lambda pat: pat.group(1).upper()

def to_camel(ident):
    return re.sub(pattern,replace,ident)
