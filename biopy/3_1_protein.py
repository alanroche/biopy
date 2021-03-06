from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("AGTACACTGGT", IUPAC.protein)
print("SEQ: ", my_seq)
print("ALPHABET: ", my_seq.alphabet)

assert 'A' == my_seq[0]
assert my_seq.count("T") == 3

my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC', IUPAC.unambiguous_dna)

print ('GC%=', 100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq))
