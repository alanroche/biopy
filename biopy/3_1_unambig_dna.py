from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)
print("SEQ: ", my_seq)
print("ALPHABET: ", my_seq.alphabet)

