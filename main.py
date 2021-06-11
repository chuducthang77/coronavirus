#Main ingredient to access and download the fasta files

import requests

record = {}
searchUrl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
search_params = {"db": 'nucleotide',
                    "term": 'BS000695',
                    "retmode": "json",
                    "usehistory": 'y',
                    "idtype": "acc",
                    "retmax": 50000,
                    "retstart": 0,
                    "api_key": "bbceccfdf97b6b7e06e93c918e010f1ecf09"}

handle =requests.get(searchUrl, params=search_params, timeout=30)
record["qkey"] = [handle.json()["esearchresult"]["querykey"]]
record["webenv"] = handle.json()["esearchresult"]["webenv"]
record["count"] = int(handle.json()["esearchresult"]["count"])
record["accn"] = handle.json()["esearchresult"]["idlist"]

print(record)

fetchUrl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
fetch_params = {"db": 'nucleotide',
                    "retmode": "text",
                    "rettype": "fasta",
                    "api_key": 'bbceccfdf97b6b7e06e93c918e010f1ecf09',
                    "WebEnv": record['webenv'],
                    "query_key": record['qkey'],
                    "retstart": 0,
                    "retmax": 50000,
                    "term": 'BS000695'}
fetchHandle = requests.get(fetchUrl, params=fetch_params,timeout=30)
fasta = fetchHandle.text
print(fetchHandle)