# given a source code file, output a new file with only comment and documentation lines
def main():
    # open the source code file
    infile = open('program4_source_text.txt', 'r')
    # open a file to write the comments to
    outfile = open('program4_comments.txt', 'w')
    # for each line in the source code file:
    for line in infile:
        line_split = line.split()
        try:
            # write lines that begin with # to the outfile
            if line_split[0] == '#':
                outfile.write(line)
        except IndexError:
            # write lines with nothing to the outfile (for formatting)
            outfile.write(line)
    infile.close()
    outfile.close()
main()