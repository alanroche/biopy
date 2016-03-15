from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
assert 'TCATGTGACCA' == str(my_seq.complement())
assert 'TCATGTGACCA' == str(my_seq.reverse_complement())