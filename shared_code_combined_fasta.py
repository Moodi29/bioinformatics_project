# code for the phylogenetic tree
from Bio import SeqIO

def combine_fasta_files(*fasta_files):
    combined_sequences = []

    for fasta_file in fasta_files:
        with open(fasta_file, "r") as file:
            sequences = list(SeqIO.parse(file, "fasta"))
            combined_sequences.extend(sequences)
            
    combined_file = "combined_organisms.fasta"  # Define the output file name here
    
    with open(combined_file, "w") as output_file:
        SeqIO.write(combined_sequences, output_file, "fasta")
        
    return output_file

