from Bio import Entrez, SeqIO
Entrez.email = 'thang@ualberta.ca'
handle = Entrez.efetch(db='nucleotide', id='NC_045512', retmode='xml')
record = Entrez.read(handle)
print(handle.text)