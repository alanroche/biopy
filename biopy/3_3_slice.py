from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)

print(my_seq[4:12])
print(my_seq[4:12].alphabet)

print(my_seq[0::3]) # every 3rd
