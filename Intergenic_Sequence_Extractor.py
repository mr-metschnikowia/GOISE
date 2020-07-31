reference = input('Name of File containing reference sequence (DNA/Protein) in FASTA format:')

with open(reference, 'r') as f:
    file_data = f.read()

file_data = "".join([i for i in file_data if i.isalpha()])
file_data = file_data.upper()

# Reference sequence is read in and stored as file_data.

# PUL1
gene_4 = ''' 1 atggtgactg aaagtggcga gctttttatc tctcaagctt ttatagacat gtggatcgac
       61 agtttagtgg gctaccttcc gggcgaaact tgcagacacg tctcgcaatt cgtgcagaat
      121 gaatacgttg gaaccttggg tcagctttac gtaacaatca gggacttgag gcaggcaatt
      181 tcggcctttg tcgacctggt aaatggcgag gaaaacaaaa actttctcgc tttcgatgcc
      241 catgtctctg attgcggctg ccatttgcgg gcactgatgc tgatggatct tattcaacgg
      301 tatagaggaa acagaaaaga gttactcctg tttctcgggt tagtggatgc ttgcgacaat
      361 gcccttgtat ccacgtctgc tttgatgaaa gacatttgca ccgaagcgaa atcattgaag
      421 gaattgcaat tgcccaaatc aaccaaagat ccgcttttat tcttgaatgc cattggttgg
      481 aaatttgaat ccaacaattt gtcagaaatc aaatacatct tctactgcta tgtgctttct
      541 cagttcaaaa catacagttt ccggaacaaa caggacagtg tgcatatcga taccgacaag
      601 gaattcaagc agaagaatga aatgatatgc acccacactt gccaaggaaa gggaaagtta
      661 ggcaacggct gccggtactt gaaacacgca agaatcggca aggccgcttt gaaacaatgg
      721 actttgtgct accaagaaag gcttctgaag atgtctgtgg actacttggc gaaaagcgat
      781 tctgaattaa aagaattggt tgaaaacctg cgcaaagagt cgcacaagag tgttgccgca
      841 gtaccgagtt atgtgcagtt caagatctcg gaaaggctct gggcctttaa tcaatttcct
      901 tttcttttgt ccatgagggt cttcgttgat gagggtcacg aggatattta tgctcgagca
      961 tttgttgggc gcgacttgaa atggaatatc cagtttgtgg ccagtgacgt gttggaggat
     1021 actccgcata ttattgttgc gggccactgt cgtgtgccac atggctacaa tgacaccaac
     1081 aagcttaacc ttgcaaactt atcgttggac gcgcaccaga acatgcgttc attttggtat
     1141 tcgttcatga gccagcacaa acagtacccc tttgacactg cgttggggtg tgacgacgac
     1201 ttgcaaaatg tgttacctgc tcacgaattc aaagattaca tgaagttcaa gtctgctggc
     1261 attcgggctt tcaaagacat ggaatttaca cccaaacaca tttttgtgga atatccaagt
     1321 gttgtgttca gcaagcaaag aatgttggcc ggcaaacagg gtgttctctt t'''

gene_4 = "".join([i for i in gene_4 if i.isalpha()])
gene_4 = gene_4.upper()

# PUL2
gene_3 = '''    1 aatcaatcta gtgagcttga tttgagcatc tggtcggacc acaaacgtgt ctgccgcaac
       61 cttgagctcg ccttccaagg ctacctcaaa agtaaacaat acctttgcta tctcggtctt
      121 gatcaagacc tcagcaaagt tctttcccaa acaacgtcta gggcccgatc caaatgtcac
      181 actcgacatg agaatgtctc tgttgttaag ccccaagaac ctatcggagt cgaaagtagc
      241 accgtaatcc gtcctcttat ctgcaggatt ccacaatgga gacttataat tcaattggta
      301 ttgatccacg acaatgggcg tgttggcctc gattttgtgg ccatcaatca ccatagcgct
      361 tgaagactgc tctgggaagc cgtaccagag aagtggatgt aaccgcaaga tttcaagtaa
      421 aacacggtgg agaactgtgt ctgtcctctt gcaatattca tccaccagct gcaagttctc
      481 caagacctcc aatctcaaac gggcctgctc atgcttgttg cggcccatct caaccaacga
      541 ccacgacatg attgtcgcag tgacatcgat attggcaaac aaaatctcgt cgaggctctg
      601 gatccagtta tccaaggtca agtcacgtga ctcgactaat ttgtacaatt cactggcaac
      661 ggttgggttt tccgcgtcac gtgccagttc caccatggcc aacgataaag acttgaatga
      721 gtcctggaaa aatttaagat ctttcatcct ttgaaacggg aagtattggt atattttgaa
      781 ccggccccag aacgtggtaa acgcgtgcgt catcaactca ctatggagcg gcaccaagtt
      841 cttcaattca gtcaaaatcc gccctgaaca ttgctcattt ccgtacaaat atttggcaat
      901 acacgtgaaa ggcaccgtgg caacaaaatc aaacgcgtcc acggaaaact cattttgcga
      961 atcatgctcc agaatccagc cgtcaataaa tgcgatcatc gcgggcaacg ttttcgcagc
     1021 caacgtatgt gtgaaaaaca aattaaacag tttccgcatc cgcgtccaca gctcaccatt
     1081 ttgaaagccc aaacactccc ctaataatgc cacaagatac tggcccgcgc cgaaggagtc
     1141 taattttttg tggtctttgg tatgcagaga ataatactgc ttcaattggc ttggcgtggt
     1201 gagcaccact tcatagcgaa atccatcacg atgtgaatag atcgatccat attgattctt
     1261 atttttttcg gagatttcgg gtccttgagt gatcttcttg ccctcgacat ttctatggga
     1321 tcgtgggatt ttcttgaacg gtggttgttt ctggaaagcg cgaagctttg acttcagaga
     1381 aacgagacac aagctcacca ccaaaaccca aaacactggg aacaggagaa tggttatcat'''

gene_3 = "".join([i for i in gene_3 if i.isalpha()])
gene_3 = gene_3.upper()

# PUL3
gene_1 = '''        1 atggcgatct cgcaactcgt ggcgattttc gccagttact gcgatttcaa gatccacaac
       61 ttcaaggtca acagcaataa cggacccact ttcgtgtgca gtttcatcat tcttgcagtc
      121 acggctttgc tagtgtttgt gttggaaaac ccggccgtcc ccacaaagaa aacgagcttg
      181 agtttcacaa aggcattgca agggtttttc agtgctccaa aatggacttt ggctggtggt
      241 atcattcttt tgtggggcat gtttttcgcg tcgttcttga tgagcgaggt ggtatacttc
      301 atgccggtgt ttttgaccga gtcgctagga tgggaaacca aattccaggg tgttgctttc
      361 atggtagcat ccatcattgg aatctgcggc agtctcgtgt ttcctcactt gatagagatg
      421 ccaatcagaa agaaggaaaa ggagctcaat tcccaagccg agagccaact gaagctcagt
      481 gaaaaaagcg atatcagcca caacagcgag gaatctgctg accggaaaca agagttcgag
      541 gcatacaaga agaacgcact ttataacaat caaattgtgc tttcgctagt gtcacttttg
      601 atcgctttag tgggccaggc cttcatgatt ggtgcagcac aggttttccg ccataggagc
      661 ttgccccata tcaacaccgg gtgctttttc gtgggcggta tgtcgctcgt gatgttggct
      721 tataacggca tggcatcgac tttcccggcc ttgttttctg tttatatcga cccacaagtc
      781 aagttgcaat tgatgcctgc aattggcgcg gtggctgcgc tcggcaaatt gatcgcgcca
      841 attgtgcttt ctaacttata tcagacgaaa ttaggccttt cgattgctgt tggtttgggc
      901 atgattttga ccgcgttgac gcttatgccg gtatttttgc tcaaggataa gaaacac'''

gene_1 = "".join([i for i in gene_1 if i.isalpha()])
gene_1 = gene_1.upper()

# PUL4
gene_2 = ''' 1 cccttgctta aatagccatt tatccagatc caattcattg tttttcacat tttccaactc
       61 cttgatcaag tacttattga tgggaatgac acctgtgagg tctatcaaaa gctccatccc
      121 tattttgtac tcagcaaatt caaaactaag ggctggcagc agattaatgt accttgtgag
      181 caccatacat gcaaaccaca cacacaatgt agcatttcgg agagggtacg agaaattcca
      241 gtccaagttc ggcaaaaagt ttctcttgta gaagtaatag tacgcccaaa aatccttgac
      301 gatatttttg gcatcaacca ccgctctggt gtttcgcttt tcgagaagtg caggtaagtt
      361 caacaacatg gaaacgtacg ccttccagca cttgagctca agggtgaaaa gctcgtgtct
      421 gcctataatt tcttcctggg gaaacgactc ctcgaaaaga ctgatttctt cacacaagcg
      481 tgaaagctct tttcgtagta attggtagtt tatttcctcg gacttgttta ccacggcaac
      541 gatccccgaa agttccgcga acttgatgcg tagctcgaaa aaaacttcca cataccggtt
      601 tttcatctgc acatgtgctg tagtcgagat ttttgaacgc atcaagggcg gagcatggcc
      661 atgaaaagtg gcgagcatgc agctggaaca ccagaggccc caaaaagcaa tcaccaaccc
      721 atattcctct gtgtttattt ccacacggga catctgggtc aacccgatgg atatcgctat
      781 ttgtagcgca tggtacgaga tgtacatctg ggtttcgggc gtgagcaaga tactcataaa
      841 atttgccatg acagctaggc cacggaaacc atgtcgggac ggagctttca acatgctggg
      901 aataagttct cttgcccttg agtaatggcc atacgcctca gaggccatgg cagggagttt
      961 caagccgatt ttttcgggaa cttcaaccat cgtatcctgt ctctggccca ccaaatctcg
     1021 ttttgccaat gtcaacgcgc ccatcgccaa tatcgtagca tgtaagaact cctcgtcctc
     1081 tgctctcacc tgcaacatgt caatattcaa tatcatctcg tgagatacgc ccggaggtgg
     1141 atgtagctta ttgctgaata ccgcgtctat gagtaatttg tgtggcagaa tctcgatctg
     1201 ttccaacggg tcataagacc ctagcggaac ggagtcgtcc aagaaacaga aaaattcgtc
     1261 catactgaag ttcaagtcac cctgaaataa gtccggcaca aagtccggcc attgctgacc
     1321 aatgtctggg cttgggaaga acgtcgggaa ttccgaggca ttaaacgtca gcaaagatcc
     1381 atcgagaccc gcttcgatct ggctgatggg cgatatgagc gtggtttcgg ggatatcctt
     1441 gtaatcgccc gttgtgtcgc agtttttgaa tacaaacacg tcttttccat ttaacttctg
     1501 ccgcttgtcg accctcttgt ctggtgggta ttcgcacgac gtgatgccca agcttagaca
     1561 ccgggaacag ctcggttttg aaccgtcaca tttgagtttt ttcagtttgc atcgcgtgca
     1621 cgtctttgct actttcacca t'''

gene_2 = "".join([i for i in gene_2 if i.isalpha()])
gene_2 = gene_2.upper()

# APC1.2 PUL genes are stored as variables.
# Variable name reflects gene order e.g. gene_1 is at first in the cluster.
# Data is made continuous, upper case and special characters are excluded.

IGS = []

coords_1 = file_data.find(gene_1) + len(gene_1)
coords_2 = file_data.find(gene_2)
chunk = file_data[coords_1:coords_2]
IGS.append(chunk)
coords_3 = coords_2 + len(gene_2)
coords_4 = file_data.find(gene_3)
chunk  = file_data[coords_3:coords_4]
IGS.append(chunk)
coords_5 = coords_4 + len(gene_3)
coords_6 = file_data.find(gene_4)
chunk = file_data[coords_5:coords_6]
IGS.append(chunk)
print('Order: PUL3 > PUL4 > PUL2 > PUL1')
print(IGS[0])
print(IGS[1])
print(IGS[2])

# Position in sequence is used to extract intergenic DNA which is appended to IGS list.
# Order of genes and thus of intergenic DNA in cluster is shown.
