from genomeinsight.io.fasta import read_fasta

sequences = read_fasta("examples/sample.fasta")

for seq in sequences:
    print(seq)