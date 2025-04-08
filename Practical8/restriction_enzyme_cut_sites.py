#restriction_enzyme_cut_sites
def cut(dna,enzyme):
    #Check if both sequences contain only canonical nucleotides (learnt from copilot)
    if not all(base in "ACGT" for base in dna.upper()) or not all(base in "ACGT" for base in enzyme.upper()):
        return "Error: Wrong sequence!"
    #find the cutting positions
    position=[]
    #calculate the length
    l=len(dna)-len(enzyme)
    for i in range(0,l+1):
        if dna[i:i+len(enzyme)]==enzyme:
            position.append(i+1)
    return position

#Example:
#input
dna1='AAGCTTAGCTAGCTTACGTAAGCTT'
enzyme1='AAGCTT'
#output
pos1=cut(dna1,enzyme1)
print(pos1)