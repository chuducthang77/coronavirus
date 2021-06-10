import requests

record = {}
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
search_params = {"db": 'nucleotide',
                    "term": 'NC_045512',
                    "retmode": "json",
                    "usehistory": 'y',
                    "idtype": "acc",
                    "retmax": 50000,
                    "retstart": 0,
                    "api_key": "bbceccfdf97b6b7e06e93c918e010f1ecf09"}

handle =requests.get(url, params=search_params, timeout=30)
record["qkey"] = [handle.json()["esearchresult"]["querykey"]]
record["webenv"] = handle.json()["esearchresult"]["webenv"]
record["count"] = int(handle.json()["esearchresult"]["count"])
record["accn"] = handle.json()["esearchresult"]["idlist"]

print(record)