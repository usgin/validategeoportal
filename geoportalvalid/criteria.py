import urllib2, ftplib
from urlparse import urlparse

### Define Criteria Here ###
# Criteria should be functions that, when given a value, determine
#   whether or not that value is valid. Upon determining validity,
#   the function should return True or False, valid or invalid.
# Criteria can return an optional second argument. This should be
#    a string meant to be appended to a failure message

def has_ten_words(value):
    if len(value.split(" ")) > 10:
        return True
    else:
        return False
    
def has_two_words(value):
    if len(value.split(" ")) > 1:
        return True
    else:
        return False
    
def url_resolves(value):
    url_bits = urlparse(value)
    supported_protocols = [ "http", "https", "ftp" ]
    if url_bits.scheme not in supported_protocols:
        return False, "The " + url_bits.scheme + " protocol is not supported at this time. Supported protocols are: " + str(supported_protocols)
    
    if url_bits.scheme in [ "http", "https" ]:
        try:
            y = urllib2.urlopen(value, timeout=5)
        except urllib2.HTTPError, err:
            return False, "URL returned HTTP error code: " + str(err.code)
        except urllib2.URLError, err:
            return False, "URL raised an error: " + str(err.reason.message)
        
        if y.code in [ 200 ]:
            return True
        else:
            return False, "URL returned status code: " + str(y.code)
        
        y.close()
    elif url_bits.scheme in [ "ftp" ]:
        try:
            f = ftplib.FTP(url_bits.netloc)
        except:
            return False, "Error connecting to FTP host: " + url_bits.scheme
        
        try:
            f.login()
        except:
            return False, "Error connecting to FTP host: " + url_bits.scheme +". Does the server allow anonymous logins?"
        
        try:
            files = f.nlst(url_bits.path)
            if len(files) > 0:
                return True
            else:
                return False, "Could not find given file on FTP site."
        except:
            return False, "Error locating file on FTP site."