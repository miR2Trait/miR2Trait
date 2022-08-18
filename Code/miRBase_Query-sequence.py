mirs=[]
question = input("Do you wish to input a single sequence (1) or a batch of sequences (2) ?")
if question == '1':
    mir = input("Enter the sequence whose information you wish to retrieve")
    mirs=[mir]
else:
    fh = input("Enter the filename with the sequences, one per line")
    with open(fh, 'r') as infile:
        for line in infile.readlines():
            line=line.strip()
            if line:
                mirs.append(line)

def retrieve_mirs(mirs):
    acc=[]
    URLs=[]
    names=[]
    for mir in mirs:
        fh = open('mirbase_human.csv', 'r')
        lines = fh.readlines()
        for line in lines:
            elems = line.split(',')
            if mir.lower() in elems[3].lower():
                acc.append(elems[1])
                URLs.append("https://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=" + elems[1])
                names.append(elems[0])
                break            
        fh.close()

    zipped = list(zip(names, acc, mirs, URLs))
    print("miRNA\t\tAcc.ID \nSequence\nRef.URL\n\n")

    for item in zipped:
        print(item[0]+'\t\t'+item[1]+'\n'+item[2]+'\n'+item[3]+'\n\n')

retrieve_mirs(mirs)
