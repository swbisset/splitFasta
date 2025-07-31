# splitFasta
Splits a fasta file, using information from a supplementary table 

```
usage: splitFasta.py [-o OUTPUT] [-f] [-x] [-v] fasta_file split_text

positional arguments:
  fasta_file            Fasta file to be read in
  split_text		Text file containing entries to keep/ discard

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file to write to
  -f, --fasta           Use if comparing two fasta files (i.e. split_text is also a fasta)
  -x, --exclude         Exclude entries from split_text
  -v, --verbose         Set verbose
  ```
  
## Usage 
Takes a fasta file (**fasta_file**), and takes a list of gene/ protein names/ identifiers (**split_text**) which contains at least some of the reads from **fasta_file**, and writes a new file (which can be specified by **OUTPUT**) which contains only the fasta sequences matching the names in **split_text**. 

## Optional flags

1. *-o --output* 

   Allows the output file names to be specified. If this is not given, the output file will be **fasta_file_split.fasta**. 

2. *-f --fasta*

   This is used if two fasta files are being compared. This essentially tells the script that **split_text** should also be read in as a fasta file. 

3. *-x --exclude* 

   Sets the script to exclude the entries provided in **split_text**, rather than keep them. 
