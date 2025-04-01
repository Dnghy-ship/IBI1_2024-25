#largest_intron
#create the RNA string
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
#import the regular expression library
import re
#find the intron sequence
find=re.findall(r'GT.*?AG',seq)
#extact the intron from the list
intron=max(find, key=len)
#print the intron and the length
print(intron)
print("Length: ", len(intron))
