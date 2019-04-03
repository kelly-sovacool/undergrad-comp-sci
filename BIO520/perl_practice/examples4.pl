#!/usr/bin/perl -w

sub e4_2 {
	print "Example 4-2\n";
	$dna1 = 'ACGGGAGGACGGGAAAATTACTACGGCATTAGC';
	$dna2 = 'ATAGTGCCGTGAGAGTGATGTAGTA';
	print $dna1, $dna2, "\n";
	$dna3 = $dna1 . $dna2;
	print $dna3, "\n";
	print "$dna1$dna2\n";
	print "\n";
}

sub e4_3 {
	print "Example 4-3\n";
	$dna = 'ACGGGAGGACGGGAAAATTACTACGGCATTAGC';
	print "DNA:\t$dna\n";
	($rna = $dna) =~ s/T/U/g;
	print "RNA:\t$rna\n";
	print "\n";
}

sub e4_4 {
	print "Example 4-4\n";
	$dna = 'ACGGGAGGACGGGAAAATTACTACGGCATTAGC';
	print "DNA:\t$dna\n";
	$rev_com = reverse $dna;
	$rev_com =~ tr/ACGTacgt/TGCAtgca/;
	print "Reverse complement:\t$rev_com\n";
	print "\n";
}

sub e4_5 {
	print "Example 4-5\n";
	$filename = 'protein.pep';
	open(protein_file, $filename);
	$protein = <protein_file>;
	print "protein:\t$protein\n";
	close protein_file;
}

sub e4_6 {
	print "Example 4-6\n";
	$filename = 'protein.pep';
	open(protein_file, $filename);
	print "first line\n";
	$seq = <protein_file>;
	print $seq; 
	print "second line\n";
	$seq = <protein_file>;
	print $seq;
	print "third line\n";
	$seq = <protein_file>;
	print $seq;
	close protein_file;
	print "\n";
}

sub e4_7 {
	print "Example 4-7\n";
	$filename = 'protein.pep';
	open(protein_file, $filename);
	@protein = <protein_file>;
	print "protein array:\n";
	print @protein;
	close protein_file;
	
	@bases = ('A', 'C', 'G', 'T');
	print "bases:\n", @bases, "\n";
	$base1 = pop @bases;
	print "last element:\t$base1\n";
	print "remaining array:\n";
	print @bases, "\n";
	
	@bases = ('A', 'C', 'G', 'T');
	$base2 = shift @bases;
	print "element from beginning:\t$base2\n";
	print "remaining array:\n";
	print @bases, "\n";
	
	@bases = ('A', 'C', 'G', 'T');
	$base2 = shift @bases;
	push (@bases, $base2);
	print "element from beginning pushed onto the end:\n";
	print @bases, "\n";

	@bases = ('A', 'C', 'G', 'T');
	print "reversed:\n";
	@reversed = reverse @bases;
	print @reversed, "\n";

	print "length of the array: ";
	print scalar @bases, "\n";
	
	@bases = ('A', 'C', 'G', 'T');
	splice (@bases, 2, 0, 'X');
	print "array with element inserted after 2nd:\n";
	print @bases, "\n";
	print "\n";
}

sub e4_8 {
	print "Example 4-8\n";
	@bases = ('A', 'C', 'G', 'T');
	print "@bases\n";
	$a = @bases;
	print $a, "\n";  # gives the length
	($a, $b) = @bases;  # copies as many elements as possible from bases to another array
	print $a, "\n";
	print $b, "\n";
	exit;

}
e4_2();
e4_3();
e4_4();
e4_5();
e4_6();
e4_7();
e4_8();
exit;
