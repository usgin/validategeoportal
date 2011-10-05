from rule_defs import rule_defs
from logger import log, writeout
from lxml import etree

ns = {'gmd': 'http://www.isotc211.org/2005/gmd',
      'srv': 'http://www.isotc211.org/2005/srv',
      'gco': 'http://www.isotc211.org/2005/gco',
      'gml': 'http://www.opengis.net/gml',
      'xlink': 'http://www.w3.org/1999/xlink',
      'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

# First define the Rule Class
class Rule():
    def __init__(self, xpath, criteria, message=None):
        self.xpath = xpath
        self.criteria = criteria
        self.message = message
        
    def validate(self, record):
        # Insure the document is valid: Must be parse-able by lxml
        try:
            doc = etree.fromstring(record.xml)
        except Exception:
            log(False, record.docuuid, self.xpath, "No valid value", "The XML Document itself could not be parsed.")
            return
    
        # Find the XPath in the record
        try:
            nodes = doc.xpath(self.xpath, namespaces=ns)
        except Exception:
            log(False, record.docuuid, self.xpath, "No valid value", "There was a problem finding the XPath.")
            return
        
        for node in nodes:
            # XPath evaluation will either return an element with a text attribute, or a string straight-up
            if hasattr(node, 'text'):
                value = node.text
            else:
                value = node
            
            if not type(value) == str:                    
                log(False, record.docuuid, self.xpath, "No valid value", "XPath evaluation did not return a valid string.")
                continue 
            
            response = self.criteria(value)    
            if not type(response) == bool:
                result = response[0]
                extraMessage = " " + response[1]
            else:
                result = response
                extraMessage = ""
            
            # Log the result
            log(result, record.docuuid, self.xpath, value, self.message + extraMessage)
                
# Then generate a set of Rule objects from the definitions in rule_defs.py
rules = list()
for rule_def in rule_defs:
    rules.append( Rule( rule_def["xpath"], rule_def["criteria"], rule_def["failMsg"] or None ) )