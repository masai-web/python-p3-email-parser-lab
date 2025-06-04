# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
       
        addresses = re.split(r'[,\s]+', self.email_addresses.strip())
        addresses = [addr for addr in addresses if addr]  
        
        
        valid_emails = []
        email_pattern = re.compile(r'^[A-Za-z][\w.%+-]*@[\w.-]+\.[a-zA-Z]{2,6}$')
        for addr in addresses:
            if email_pattern.fullmatch(addr):
                valid_emails.append(addr)
        
       
        unique_emails = sorted(list(set(valid_emails)))
        return unique_emails