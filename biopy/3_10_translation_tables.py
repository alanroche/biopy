from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]

print(standard_table)

print(mito_table)

print ('Mito Start codons: ', mito_table.start_codons)
print ('Mito Stop codons: ', mito_table.stop_codons)

print ('Mito lookup: ', mito_table.forward_table["GCA"])