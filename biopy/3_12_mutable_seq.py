from Bio.Seq import MutableSeq
from Bio.Alphabet import IUPAC
mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)

print(mutable_seq)
mutable_seq[5] = "C"
print(mutable_seq)

