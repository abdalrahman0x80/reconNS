# from dnspython import dns
import dns.resolver
import sys
try:
    try:
        url = sys.argv[1]
        inp = sys.argv[2]
    except:
        print("usage: ReconNS.py {URL} {DNS RECORD}")
    query = dns.resolver.resolve(url,inp) # record and url
    for i in query:
        print(i.to_text())
except : 
    print("Not Found record")