from connection import make_query as run_queries
from rules import rules, writeout

def validate_records(records):
    for record in records:
        for rule in rules:
            rule.validate(record)

def run_validation():
    try:
        # Call run_queries routine. This will paginate the queries and
        #    call the validate_records function each time results are 
        #    retrieved
        run_queries(validate_records)
        
        # Completed. WriteOut
        writeout()
    except Exception, ex:
        print "Problem running queries: " + str(ex)