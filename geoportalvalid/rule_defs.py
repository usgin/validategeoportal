from criteria import *

### Create an array of rules definitions ###
# Each definition should specify an XPath and a criteria. Available criteria are defined
#    in criteria.py. Also specify a message to log if a rule is failed.

rule_defs = [
    {
        "xpath": "/gmd:MD_Metadata/gmd:identificationInfo//gmd:abstract/gco:CharacterString", 
        "criteria": has_ten_words,
        "failMsg": "Abstracts should have at least 10 words." 
    }, {
        "xpath": "/gmd:MD_Metadata/gmd:identificationInfo//gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString", 
        "criteria": has_two_words,
        "failMsg": "Titles should have at least 2 words, don't you think?"
    }, {
        "xpath": "//gmd:URL",
        "criteria": url_resolves,
        "failMsg": "URLs in metadata should be valid."
    }     
]

    
