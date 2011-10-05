dbHost = "localhost"
dbPort = 5432
dbName = "{database name}"
dbUser = "{secret username}"
dbPass = "{secret password}"

reportFilePath = "{where to put the report}"

##### No Need to adjust the line below #####
dbString = "host=%s port=%s dbname=%s user=%s password=%s" % (dbHost, dbPort, dbName, dbUser, dbPass)