from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML


record = SeqIO.read("../data/input_hypothetical_sequence.fasta", "fasta")

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=record.seq
)

with open("../results/blast_results.xml", "w") as b:
    b.write(result_handle.read())

print("Blast Search Completed")


with open("../results/blast_results.xml") as b:
    blast_record = NCBIXML.read(b)

print(len(blast_record.alignments))

print("Functional Annotation (Top 10 Hits):")

for alignment in blast_record.alignments[:9]:
    print("Protein Annotation:", alignment.title)
    print("Organism Information: Extracted from annotation")
    print("Length of HSPs:", len(alignment.hsps))
    print("-"*30)
