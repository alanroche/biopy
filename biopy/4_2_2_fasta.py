from Bio import SeqIO
record = SeqIO.read("./plasmid.fna", "fasta")

print(record)
print(record.id)
print(record.name)
print(record.description)