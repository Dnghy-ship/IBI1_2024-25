#tata_box
#open the file
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
store=open('tata_genes.fa','w')
#use re library
import re
#read through the file to find all the genes
content=file.read()
seq=content.split('>')[1:]
#define the tata box and tata gene
tata=r'TATA[AT]A[AT]'
gene=[]
#find the tata box in each sequence
for s in seq:
    #process each sequence to be a connect sequence
    line=s.split('\n')
    header=line[0]
    sequences=''.join(line[1:])
    #check the tata box
    if re.search(tata,sequences):
        find=re.findall(r'gene:(\S+)\s',header)
        name=find[0]
        #store them into file
        store.write(f">{name}\n")
        for i in range(0, len(sequences), 60):
            store.write(sequences[i:i+60]+'\n')
#close the file
file.close()
store.close()

        



