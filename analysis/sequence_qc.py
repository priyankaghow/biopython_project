from Bio import SeqIO
from collections import Counter


record = SeqIO.read("../data/input_hypothetical_sequence.fasta", "fasta")
sequence = record.seq
aa_count = Counter(sequence)
total_length = len(sequence)

print("Sequence Quality Analysis")
print("Protein ID:", record.id)
print("Protein Length:", total_length)
print("Amino Acid Composition:")

for aa, count in aa_count.items():
    print(aa, ":", count)
print()

print("Sequence Filtering & Validation")
if total_length < 100:
    print("Sequence rejected: Too short for reliable analysis.")
else:
    print("Sequence accepted: Suitable for downstream analysis.")
