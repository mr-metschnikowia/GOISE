# does not support repeats that are 100% identical
import os
# importing dependancies

def read_in_reference():
    global reference
    path = r'C:\Users\Rhino\PycharmProjects\sfam\genomes\apc1.2.fasta'
    with open(path, 'r') as f:
        reference = f.read()
        reference = "".join([i for i in reference if i.isalpha()])
        reference = reference.upper()
        if reference.find('SEQUENCE') >= 0:
            bearing_4 = reference.find('SEQUENCE') + len('SEQUENCE')
            reference = reference[bearing_4: len(reference)]

# reads in .fasta reference sequence, removes the descriptive line and all special characters

name_list = []
gene_list = []
orient = []
gene_number = 9

# records number of genes we are dealing with

def read_in_genes():
    global gene_list
    global name_list
    for file in os.listdir(r'C:\Users\Rhino\PycharmProjects\sfam\pul_seqs\apc1.2'):
        name_list.append(file[0:4])
        path = r'C:\Users\Rhino\PycharmProjects\sfam\pul_seqs\apc1.2\\' + file
        with open(path, 'r') as f:
            gene = f.read()
            gene = "".join([i for i in gene if i.isalpha()])
            gene = gene.upper()
            if gene[0:3] == 'ATG' or gene[0:3] == 'TAC':
                orientation = '+'
            elif gene[len(gene) - 3:len(gene)] == 'GTA' or gene[len(gene) - 3:len(gene)] == 'CAT':
                orientation = '-'
            else:
                orientation = 'NA'
            orient.append(orientation)
            # orientation of each gene is obtained based on location of ATG/TAC start codon
            gene_list.append(gene)
    # All genes in folder are read in and optimised
    # Name of each gene is extracted from file name

def find_order():
    global order
    locations = []
    for key in dictionary_1:
        location = reference.find(dictionary_1[key])
        locations.append(location)
    dictionary_2 = dict(zip(locations,name_list))
    locations.sort()
    order = []
    for location in locations:
        o = dictionary_2[location]
        order.append(o)

# function determines sequence of genes

read_in_reference()
read_in_genes()
dictionary_1 = dict(zip(name_list, gene_list))
dictionary_3 = dict(zip(name_list,orient))
# orientation is associated with gene name
find_order()
# number of times function read_in_gene is called is equal to gene_number
# gene sequences and names are kept together in dictionary_1
ordered_orient = []
for i in order:
    reshuf = dictionary_3[i]
    ordered_orient.append(reshuf)
# orientation is ordered based on ordered names

ordered_seqs = []

for item in order:
    ordered_seqs.append(dictionary_1[item])

# gene sequences are ordered

intergenic_seqs = []
x = 0
y = 1

for i in range(len(ordered_seqs)-1):
    coords_1 = reference.find(ordered_seqs[x]) + len(ordered_seqs[x])
    coords_2 = reference.find(ordered_seqs[y])
    chunk = reference[coords_1:coords_2]
    intergenic_seqs.append(chunk)
    x += 1
    y += 1

# intergenic sequences are extracted and stored

array = []
duo = []
for seq in intergenic_seqs:
    unknown = seq.find('N')
    if unknown > -1:
        len_seq = 'NA'
    else:
        len_seq = str(len(seq))
    duo.append(len_seq)
    duo.append(seq)
    array.append(duo)
    duo = []

# list of intergenic sequences is iterated through
# length of sequence + sequence are coupled and stored in array
# if an 'N' is found in the sequence, length = NA

with open(r'C:\Users\Rhino\PycharmProjects\sfam\inter_seqs\apc1.2.txt','a') as h:
    strain_name = 'apc1.2'
    h.write(strain_name+ '\n')
    order = '>'.join(order) + '\n'
    h.write(order)
    ordered_orient = '>'.join(ordered_orient) + '\n'
    h.write(ordered_orient)
    h.writelines([" ".join(i) + "\n" for i in array])
    h.write('\n')

# file inter_seqs.txt is created
# file contains strain name, sequence of genes, orientation of each gene and a table: column 1 = sequence length, column 2 = sequence
