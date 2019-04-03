#!/usr/local/bin/python3
import sys

def main():
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    map_filename = sys.argv[3]
    with open(map_filename, "r") as map_file:
        gene_ids_to_names = {line.split()[1]: line.split()[0] for line in map_file if line.split()[0] != 'gene_id'}
    with open(outfilename, "w") as out_file:
        with open(infilename, "r") as data_file:
            first = True
            for line in data_file:
                split_line = line.split()
                if not first:
                    gid = split_line[0]
                    if gid in gene_ids_to_names:
                        name = gene_ids_to_names[gid]
                        split_line[0] = name
                        out_file.write("\t".join(split_line) + "\n")
                else:
                    first = False
                    split_line[0] = "gene_name"
                    out_file.write("\t".join(split_line) + "\n")

main()

