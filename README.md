# splitFasta
Splits a fasta file, using information from a supplementary table 

```
usage: splitFasta.py [-h] [-n NAME] [-i INFO] [-o OUTPUT]
                     fasta_file info_file split_string

positional arguments:
  fasta_file            Fasta file containing reads to be split
  info_file             File in csv or tsv format which contains parameters
                        for filtering/ splitting
  split_string          String to filter or split reads by. Should appear in a
                        column of info_file

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Column of info_file which contains names of reads in
                        fasta_file. Default is 1
  -i INFO, --info INFO  Colum of info_file which conatins splitting
                        informaton. Default is 2
  -o OUTPUT, --output OUTPUT
                        Name of output file
  ```
  
## Usage 
Takes a fasta file (**fasta_file**), and takes reads and writes to a new fasta file based on a second table (**info_file**) which contains at least some of the reads from **fasta_file**, and has an additional column with extra information. An additional string (**split_string**) is supplied, which is used to filter out the reads from **fasta_file** to write to a new file. 

The main use for this was to split reads from a metagenomic fasta file, which contained a mixture of bacterial and fungal reads, into bacteria-specific and fungal-specific files. The info file was created by blasting the fasta file against a database of bacterial and fungal 16S/18S rRNA sequences, which resulted in a table of reads with a second column containing information describing the best match (*i.e.* bacterial or fungal origin). The program then takes the fasta file, info file, and a string to split by (for example, '*Bacteria*' or '*Fungi*'), and splits the fasta file accordingly. 

## Optional flags

1. *-n --name* 

   This flag takes an integer, which directs the column in **info_file** which contains the read IDs that appear in **fasta_file**. This expects the lowest value to be 1, not 0. The default value is 1. 


2. *-i --info*

   This flag takes an integer, which directs the column in **info_file** which contains the information in which **split_string** will be searched against. This expects a lowest value of 1, not 0. The default value is 2. 

3. *-o --output* 

   Allows the output file to be named. The format will be a fasta file, so should probably end in .fasta. If no output name is supplied, then the file will be named `[fasta_file]_[split_string].fasta`. 
