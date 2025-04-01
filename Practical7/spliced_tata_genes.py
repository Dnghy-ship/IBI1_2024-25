#spliced_tata_genes
import re
#input donor and accepter
com=input()
#protect the code by validating the input
if com not in ['GTAG','GCAG','ATAC']:
    print("Error")
    exit()
#define splice pattern
donor=com[:2]
acceptor=com[2:]
splice=re.escape(donor)+r".*?"+re.escape(acceptor)
#open the relative files
store=open(f"{com}_spliced_genes.fa",'w')
file=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
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
    if re.findall(splice,sequences):
        spl=re.findall(splice,sequences)
        for targets in spl:
            if re.search(tata,targets):
                #find the name
                find=re.findall(r'gene:(\S+)\s',header)
                name=find[0]
                # Count the number of TATA boxes in the intron
                count = len(re.findall(tata, targets))
                # Write the results to the output file
                store.write(f">{name}   {count}\n")
                store.write(f"{targets}\n")
#close the file
file.close()
store.close()
