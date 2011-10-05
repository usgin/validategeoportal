This module is intended to provide a simple means for checking that metadata records in an ESRI Geoportal have decent content. By defining validation criteria functions and assigning those criteria to an XPath in the metadata document, you can check that the content of your Geoportal is up-to-snuff.

Notes: 
- This implementation requires the following python modules: lxml, psycopg2
- This implementation assumes that your Geoportal content is housed in a PostgreSQL database.
- The database prerequisite could be pretty easily circumvented by replacing connection.py with something that works through CSW GetRecords and GetRecordsById requests.

To use this module:
1) Add the geoportalvalid folder to your python-path.
2) Copy config-example.py to config.py, and customize appropriately for your Geoportal.
3) Adjust any rule_defs and create any new criteria.
3) From a command line: python -c "import geoportalvalid; geoportalvalid.validate();"
