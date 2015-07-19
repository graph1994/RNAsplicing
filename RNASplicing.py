AminoTable = {     'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
             'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
             'TTA': 'L', 'TCA': 'S', 'TAA': 'STOP', 'TGA': 'Stop',
             'TTG': 'L', 'TCG': 'S', 'TAG': 'STOP', 'TGG': 'W',
             'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
             'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
             'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
             'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
             'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
             'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
             'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
             'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
             'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
             'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
             'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
             'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
        }


f = open('test.txt', 'r')
f.readline();
realString = f.readline().rstrip();
temp = realString.rstrip();
for line in f:
    temp = temp.replace(line.rstrip(),'');

chain = ""
for i in range(0, len(temp), 3):
    chain += AminoTable[temp[i:i+3]];

print(chain)





