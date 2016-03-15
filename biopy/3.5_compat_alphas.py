from Bio.Seq import Seq
from Bio.Alphabet import generic_nucleotide
from Bio.Alphabet import generic_dna
from Bio.Alphabet import IUPAC

nuc_seq = Seq("GATCGATGC", generic_nucleotide)
dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)
print(nuc_seq)
print(dna_seq)
print((nuc_seq + dna_seq).alphabet)


list_of_seqs = [Seq("ACGT", generic_dna), Seq("AACC", generic_dna), Seq("GGTT", generic_dna)]
concatenated = Seq("", generic_dna)
for s in list_of_seqs:
    concatenated += s

print(concatenated, ' ', concatenated.alphabet)

print(sum(list_of_seqs, Seq("", generic_dna)))

print(concatenated.lower())