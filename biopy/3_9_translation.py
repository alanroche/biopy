from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
print(coding_dna)
template_dna = coding_dna.reverse_complement()
print(template_dna)
messenger_rna = coding_dna.transcribe()
print(messenger_rna, ' ', messenger_rna.alphabet)

protein = coding_dna.translate()
print('Translate:', protein, ' ', protein.alphabet)

protein = coding_dna.translate(to_stop=True)
print('Translate to stop:', protein, ' ', protein.alphabet)

protein = coding_dna.translate(table="Vertebrate Mitochondrial")
print('Translate michondrian dna:', protein, ' ', protein.alphabet)
protein = coding_dna.translate(table=2)
print('Translate michondrian dna NCBI table num:', protein, ' ', protein.alphabet)

from Bio.Alphabet import generic_dna
gene = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA" + \
            "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT" + \
            "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT" + \
            "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT" + \
            "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA",
            generic_dna)
protein = gene.translate(table="Bacterial")
print('Translate bacterial dna:', protein, ' ', protein.alphabet)

protein = gene.translate(table="Bacterial", cds=True)
print('Translate bacterial dna CDS:', protein, ' ', protein.alphabet)
