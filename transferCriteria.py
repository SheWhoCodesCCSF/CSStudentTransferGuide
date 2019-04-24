## The CSStudentTransferGuide
from urllib import request as req

# This function will extract information from 
# a school website and add a row in transfer data file.
def extract_info(linkline, out):
    
    link = linkline.split()[1]

    http = req.urlopen(link).read().decode().split('>')

    out.write('\n' + linkline + '\n')
    for line in http:
        if line:
            if "total " and " semester credit" in line:
                out.write(line + '\n')   
            elif "minimum " and "GPA " in line:
                out.write(line + '\n')
            elif "required " in line:
                out.write(line + '\n')
            elif "fee" in line:
                out.write(line + '\n')      


# Feeding URL data here, to be parsed by the extract_info

outfile = open("transferInfo.txt", 'wt', newline = "\r\n")

for line in open("schoolURL.txt"):
    line = line.strip()
    if line:
#        print(line)
        extract_info(line, out = outfile)
outfile.close()
