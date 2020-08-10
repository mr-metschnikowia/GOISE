# does not support repeats that are 100% identical

strain_name = input('Please input name of strain:')

# stores name of strain

def read_in_reference():
    global reference
    folder = r'C:\Users\Rhino\PycharmProjects\sfam\genomes'
    file = input('Name of file containing reference sequence (DNA/Protein) in FASTA format (start with \):')
    path = folder + file
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
gene_number = int(input('Please enter number of genes:'))

# records number of genes we are dealing with

def read_in_gene():
    global name_list
    global gene_list
    global gene
    global dictionary_1
    folder = r'C:\Users\Rhino\PycharmProjects\sfam\pul_seqs'
    gene_name = input('Name of gene:')
    name_list.append(gene_name)
    file = input('Name of file containing gene sequence (DNA/Protein) in FASTA format (start with \ ):')
    path = folder + file
    with open(path, 'r') as f:
        gene = f.read()
        gene = "".join([i for i in gene if i.isalpha()])
        gene = gene.upper()
        gene_list.append(gene)

# function reads in gene sequence, removes the descriptive line and all special characters
# name of each gene is also recorded

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

# function determines order of genes

read_in_reference()
for i in range(gene_number):
    read_in_gene()
dictionary_1 = dict(zip(name_list, gene_list))
find_order()

# number of times function read_in_gene is called is equal to gene_number
# gene sequences and names are kept together in dictionary_1

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
    len_seq = str(len(seq))
    duo.append(len_seq)
    duo.append(seq)
    array.append(duo)
    duo = []

# list of intergenic sequences is iterated through
# length of sequence + sequence are coupled and stored in array

with open(r'C:\Users\Rhino\PycharmProjects\sfam\inter_seqs\inter_seqs.txt','a') as h:
    h.write(strain_name + '\n')
    order = '>'.join(order) + '\n'
    h.write(order)
    h.writelines([" ".join(i) + "\n" for i in array])
    h.write('\n')

# file inter_seqs.txt is created
# file contains strain name, order of genes and a table: column 1 = sequence length, column 2 = sequence
