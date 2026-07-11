from genomeinsight.io.fastq import read_fastq

reads = read_fastq("examples/sample.fastq")

for read in reads:
    print(read)