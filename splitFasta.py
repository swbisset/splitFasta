import csv
import sys
import argparse
import time

def readFile(file):
    try:
        open(file)
    except IOError:
        print "Error: cannot open %s. Please submit a valid file" % (file)
        sys.exit()
    colList = []
    mainList = []
    #This just checks the file name of the file to decide whether or not to delimit by comma or tab-separated columns
    if ".csv" in file:
        print "Comma chosen as delimiter"
        delStr = ','
    else:
        print "Tab chosen as delimiter"
        delStr = '\t'
    #This just reads in the file as a two-dimensional list
    with open(file) as r:
        reader = csv.reader(r, delimiter=delStr)
        for row in reader:
            for col in row:
                colList.append(col)
            mainList.append(colList[0:])
            colList[:] = []
    print "%s lines read in from %s" % (str(len(mainList)), file)
    return mainList

def splitFile(fasta_list, info_list, c, i, split_str):
    out_str = ""
    count = 0
    #This just reads through the table containing splitting information (info_list), and where
    #a copy of the string (split_str) is found, the corresponding fasta ID is taken and
    #searched against the initial fasta file (fasta_list)
    for x in range(0, len(info_list)):
        if split_str in str(info_list[x][i]):
            read = str(info_list[x][c])
            for y in range(0, len(fasta_list)):
                if read in str(fasta_list[y]):
                    out_str += "%s\n%s\n" % (str(fasta_list[y]), str(fasta_list[y+1]))
                    count += 1
                    break
    print "%s reads out of %s found containg '%s' in column %s" % (str(count), str(len(fasta_list)/2), split_str, str(i+1))
    return out_str

def writeOutput(out_str, out_file):
    with open(out_file, 'wb') as w:
        w.write(out_str)
    print "Output written to %s" % (out_file)

#Begin main script here
parser = argparse.ArgumentParser()
parser.add_argument('fasta_file', help="Fasta file containing reads to be split")
parser.add_argument('info_file', help="File in csv or tsv format which contains parameters for filtering/ splitting")
parser.add_argument('split_string', help="String to filter or split reads by. Should appear in a column of info_file")
parser.add_argument('-n', '--name', help="Column of info_file which contains names of reads in fasta_file. Default is 1")
parser.add_argument('-i', '--info', help="Colum of info_file which contains splitting informaton. Default is 2")
parser.add_argument('-o', '--output', help="Name of output file")

# Error catch 1: Make sure that some arguments have been supplied
try:
    args = parser.parse_args()
except SystemExit:
    print "Please enter valid file type \ntype 'python splitFasta.py -h for help'"
    sys.exit()

args = parser.parse_args()
starttime = time.time()

# Make sure everything is behaving as expected
if args.output:
    out_file = args.output
else:
    out_file = "%s_%s.fasta" % (args.fasta_file[:-6], args.split_string)
    #If an output name is not supplied, then the original fasta file will be renamed with the
    #splitting string within the name

if args.name:
    c = int(args.name) - 1
else:
    c = 0

if args.info:
    i = int(args.info) - 1
else:
    i = 1

fasta = readFile(args.fasta_file)
info = readFile(args.info_file)
out_str = splitFile(fasta, info, c, i, args.split_string)
writeOutput(out_str, out_file)
#Just see how long the process took to run
print "Process took %s seconds" % (str(time.time() - starttime))