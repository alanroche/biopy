from Bio import SeqIO
record = SeqIO.read("./plasmid.gb", "genbank")
print(record)
print(record.id)
print(record.name)
print(record.description)
print('source:', record.annotations['source'])
print('dbxrefs:', record.dbxrefs)
print('Number of features:', len(record.features))