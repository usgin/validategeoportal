import psycopg2
from config import dbString as connection_string, progressFilePath

getAllRecordsSQL =  "SELECT gpt_resource_data.id, gpt_resource_data.docuuid, gpt_resource_data.xml "
getAllRecordsSQL += "FROM gpt_resource_data INNER JOIN gpt_resource ON gpt_resource_data.docuuid = gpt_resource.docuuid "
getAllRecordsSQL += "WHERE gpt_resource.approvalstatus = 'approved' AND gpt_resource.findable = 'true' "
getAllRecordsSQL += "ORDER BY gpt_resource_data.id"

# Make the db connection
db = psycopg2.connect(connection_string)

# Count the number of records, setup pagination parameters
countSQL = "SELECT COUNT(*) FROM (" + getAllRecordsSQL + ") AS foo"
cur = db.cursor()
cur.execute(countSQL)
total_records = cur.fetchone()[0]
cur.close()

records_per_query = 10

# A record class to make the results easier to deal with
class record:
    def __init__(self, id, docuuid, xml):
        self.id = id
        self.docuuid = docuuid
        self.xml = xml    
        
def make_query(callback, start_record=0):
    if start_record >= total_records:
        # All queries have been made
        return
    
    # Build the query string
    next_setSQL = getAllRecordsSQL + " LIMIT " + str(records_per_query) + " OFFSET " + str(start_record)
    
    # Make the query
    cur = db.cursor()
    cur.execute(next_setSQL)
    response = cur.fetchall()
    
    # Build a list of records
    records = list()
    for row in response:
        records.append(record(row[0], row[1], row[2]))
    
    # Execute the callback function    
    callback(records)
    
    f = open(progressFilePath, "a")
    f.write(str(start_record + records_per_query) + " of " + str(total_records) + " complete.\n")
    f.close()
    
    # Completed callback for these records, move on
    make_query(callback, start_record + records_per_query)
    
    

    