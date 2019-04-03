#!/usr/local/bin/python3
import sys

def main():
    gene_ids_filename = sys.argv[1]
    gene_names_filename = sys.argv[2]
    output_filename = sys.argv[3]

    with open(gene_names_filename, 'r') as gene_names_file:
        gene_names = {line.strip(): None for line in gene_names_file}
    with open(gene_ids_filename, 'r') as gene_ids_file:
        for line in gene_ids_file:
            for gene_name in gene_names.keys():
                if gene_name in line and not gene_names[gene_name]:
                    gene_id = line.split()[0].strip()
                    description = line.split(gene_id)[1].strip()
                    gene_id = gene_id.strip('>')
                    gene_names[gene_name] = (gene_id, description)
                    break
    with open(output_filename, 'w') as output_file:
        output_file.write("gene_name\tgene_id\tdescription\n")
        for gene_name in sorted(gene_names):
            if gene_names[gene_name]:
                gene_id = gene_names[gene_name][0]
                description = gene_names[gene_name][1]
                output_file.write(gene_name + "\t" + gene_id + "\t" + description + "\n") 
            else:
                print(gene_name, 'had no gene id matches')

main()

