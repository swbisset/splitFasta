import csv
import sys
import argparse

def readFasta(infile):
    global log
    try:
        open(infile)
    except IOError:
        print("Error: Cannot open %s. Please submit a valid file name" % (infile))
        sys.exit()
    colList = []
    fastaList = []
    seq_str = ""
    started = False
    with open(infile) as r:
        for line in r:
            if line[0] == '>':
                if not started:
                    colList.append(line.rstrip('\n'))
                    started = True
                else:
                    colList.append(seq_str)
                    fastaList.append(colList[0:])
                    colList[:] = []
                    seq_str = ""
                    colList.append(line.rstrip('\n'))
                    #colList.append(line)
            else:
                #seq_str += line.rstrip('\n')
                seq_str += line
        colList.append(seq_str)
        fastaList.append(colList[0:])
    log_str = ("Number of sequences read in from %s: %s" % (infile, str(len(fastaList))))
    log = ("%s\n%s" % (log, log_str))
    if noisy:
        print(log_str)
    return fastaList

def readFile(inFile):
    global log
    inList = []
    with open(inFile) as r:
        for line in r:
            if len(line) > 1:
                inList.append(line.strip('\n'))
    log_str = ("Number of lines read in from %s: %s" % (inFile, str(len(inList))))
    log = ("%s\n%s" % (log, log_str))
    if noisy: 
        print(log_str)
    return inList

def compareLists(fastaList, stringList):
    global log
    compList = []
    includeList = []
    excludeList = []
    if isFasta:
        for i in range(0, len(stringList)):
            compList.append(stringList[i][0])
    else:
        compList = stringList
    for i in range(0, len(fastaList)):
        hasGene = False
        for j in range(0, len(compList)):
            if str(compList[j]) in str(fastaList[i][0]):
                includeList.append(fastaList[i][0:])
                hasGene = True
                break
        if not hasGene:
            excludeList.append(fastaList[i][0:])
    log_str = ("%s entries were included\n%s entries were excluded" % (str(len(includeList)), str(len(excludeList))))
    log = ("%s\n%s" % (log, log_str))
    if noisy:
        print(log_str)
    if exclude:
        return excludeList
    else:
        return includeList


# Main script 
parser = argparse.ArgumentParser() 
parser.add_argument('fasta_file', help="Fasta file to be read in")
parser.add_argument('split_text', help="Text file containing entries to keep/ discard")
parser.add_argument('-o', '--output', help="Output file to write to")
parser.add_argument('-f', '--fasta', help="Use if comparing two fasta files (i.e. split_text is also a fasta)", action="store_true")
parser.add_argument('-x', '--exclude', help="Exclude entries from split_text", action="store_true")
parser.add_argument('-v', '--verbose', help="Set verbose", action="store_true")

# Error catch 1: Make sure that some arguments have been supplied
try:
    args = parser.parse_args()
except SystemExit:
    print("Please enter valid file type \ntype 'python3 splitFasta.py -h for help'")
    sys.exit()

args = parser.parse_args()

if args.output:
    out_file = args.output
else:
    out_file = ("%s_split.faa" % (args.fasta_file[:-4]))

logfile = ("%s.log" % (out_file[:-4]))
log = "python3 splitFasta.py"

exclude = False
if args.exclude:
    exclude = True

isFasta = False
if args.fasta:
    isFasta = True

noisy = False
if args.verbose:
    noisy = True

# Start execution of script here
fasta = readFasta(args.fasta_file)
if isFasta:
    strings=readFasta(args.split_text)
else:
    strings = readFile(args.split_text)
outList = compareLists(fasta, strings)

# Write fasta file for output
out_str = ("%s\n%s" % (str(outList[0][0]), str(outList[0][1])))
for i in range(1, len(outList)):
    out_str = ("%s\n%s\n%s" % (out_str, str(outList[i][0]), str(outList[i][1])))

# Write output to file
with open(out_file, 'w') as w:
    w.write(out_str)
if noisy:
    print("Output written to %s" % (out_file))

# Write log file
with open(logfile, 'w') as l:
    l.write(log)