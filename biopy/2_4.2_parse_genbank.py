from Bio import SeqIO
for seq_record in SeqIO.parse("../data/ls_orchid.gbk", "genbank"):
    print('ID: ', seq_record.id)
    print('SEQ: ',repr(seq_record.seq))
    print('SEQ_LEN: ',len(seq_record))
    print('-------------')