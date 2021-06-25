#Main ingredient to access and download the fasta files
import requests

def search(accession):
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
                        "retmode": "xml",
                        "rettype": "gb",
                        "api_key": 'bbceccfdf97b6b7e06e93c918e010f1ecf09',
                        "WebEnv": record['webenv'],
                        "query_key": record['qkey'],
                        "retstart": 0,
                        "retmax": 50000,
                        "term": 'BS000695'}
    fetchHandle = requests.get(fetchUrl, params=fetch_params,timeout=30)
    result = xmltodict.parse(fetchHandle.content)
    
    print(result['GBSet']['GBSeq']['GBSeq_locus'])

def main():
    

    accessionList = ["EPI_ISL_402119", "EPI_ISL_402120", "EPI_ISL_402121", "EPI_ISL_402123", "EPI_ISL_402124", "EPI_ISL_402125"]

    myList = search(accessionList)
    
    # insert(myList, myGisaid)

    # cursor = myGisaid.find()
    # for x in cursor:
    #     print(x)

if __name__ == "__main__":
    main()