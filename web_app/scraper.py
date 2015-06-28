#scraping zipped files
import requests, zipfile, StringIO
with open("to_scrape.txt","r") as f:
    to_scrape = f.read().split("\n")

for uri in to_scrape:
    if ".zip" in uri:
        print "started scraping"
        r = requests.get(uri)
        print "unzipping"
        z = zipfile.ZipFile(StringIO.StringIO(r.content))
        print "saving"
        z.extractall()
