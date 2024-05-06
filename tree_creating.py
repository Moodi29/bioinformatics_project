import Bio as Bio
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator 
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib
import matplotlib.pyplot as plt

def create_tree(aligned_fasta_file):
    aln = open(aligned_fasta_file,'r')
    alignment = AlignIO.read(aln, "clustal")
    calculator = DistanceCalculator('identity')
    dist_matrix = calculator.get_distance(alignment)
#     print(dist_matrix)
    
    constructor = DistanceTreeConstructor(calculator)
    tree = constructor.upgma(dist_matrix)
#     tree = constructor.build_tree(alignment)
    tree.rooted = True
#     print(tree)
    

    fig = Phylo.draw(tree)
    return(fig)


create_tree("aligned_file.aln")
