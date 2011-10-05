import csv
from config import reportFilePath

failed_results = dict()

class LogEntry():
    def __init__(self, xpath, value, message):
        self.xpath = xpath
        self.value = value
        self.message = message or "No message was given."

def log(valid, recordId, xpath, value, message=""):
    if not valid:
        log_entry = LogEntry(xpath, value, message)
        if recordId in failed_results:
            failed_results[recordId].append( log_entry )
        else:
            failed_results[recordId] = [ log_entry ]
            
def writeout():
    logWriter = csv.writer(open(reportFilePath, "wb"))
    logWriter.writerow([ "DOCUUID", "XPATH", "VALUE", "MESSAGE" ])
    
    fail_count = 0
    for id in failed_results:
        for entry in failed_results[id]:
            fail_count = fail_count + 1
            
            logWriter.writerow([ id, entry.xpath, entry.value, entry.message ])
            
    print str(len(failed_results)) + " metadata records failed one or more validation rules."        
    print str(fail_count) + " records in the log."
    
    
    