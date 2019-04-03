#!/usr/bin/perl -w

sub e5_1 {
	print "Example 5-1\n";
	$word = 'MNIDDKL';
	if ($word eq 'QSTVSGE') {
		print "QSTVSGE\n";
	}
	elsif ($word eq 'MNIDDKL') {
		print "MNIDDKL -- the magic word!\n";
	}
	else {
		print "Is \"$word\" a peptide? This program isn't sure.\n";
	}
	print "\n";
}
sub e5_2 {
	print "Example 5-2\n";
	$filename = 'protein.pep';
	unless (open(protein_file, $filename)) {
		print "couldn't open file $filename!\n";
		exit;
	}
	while ($protein = <protein_file>) {
		print " ###### Here is the next line of the file:\n";
		print $protein;
	}
	close protein_file;
	print "\n";
}
sub e5_3 {
	print "Example 5-3\n";
	print "Enter protein seq filename: ";
	$filename = <STDIN>;
	chomp $filename; # remove newline
	unless (-e $filename ) {
		print "File $filename doesn't exist\n";
		exit;
	}
	unless ( open(dna_file, $filename) ) {
		print "Can't open file \"$filename\"";
		exit;
	}
	@protein = <dna_file>;
	close dna_file;
	$protein = join('', @protein);  # convert to string
	$protein =~ s/\s//g;  # strip whitespace
	do {
		print "Enter motif: ";
		$motif = <STDIN>;
		chomp $motif; # remove newline
		if ($protein =~ /$motif/) {
			print "Found it!\n";
		}
		else {
			print "Couldn\'t find it.\n";
		}
	}
	until ( $motif =~ /^\s*$/);
	print "\n";
}
sub e5_4 {
	print "Example 5-4\n";
	$filename = 'small.dna'; 
	open(dna_file, $filename);
	@dna = <dna_file>;
	close dna_file;
	$dna = join('', @dna); # convert to string
	$dna =~ s/\s//g; # strip whitespace
	@dna = split('', $dna); # explode string to array
	$countA = 0;
	$countC = 0;
	$countG = 0;
	$countT = 0;
	$errors = 0;
	foreach $base (@dna) {
		if ($base eq 'A') {
			++$countA;
		}
		elsif ($base eq 'C') {
			++$countC;
		}
		elsif ($base eq 'G') {
			++$countG;
		}
		elsif ($base eq 'T') {
			++$countT;
		}
		else {
			print "Error: unrecognized base: $base\n";
			++$errors;
		}
	}
	print "A: $countA\n";
	print "C: $countC\n";
	print "G: $countG\n";
	print "T: $countT\n";
	print "Errors: $errors\n";
	print "\n";
}
sub e5_5 {
	print "Example 5-5\n";
	$num = 1234;
	$str = '1234';
	print $num, " ", $str, "\n";
	$add = $num + $str;
	print $add, "\n";
	$cat = $num . $str;
	print $cat, "\n";
	print "\n";
}
sub e5_6 {
	print "Example 5-6\n";
	open(dna_file, 'small.dna');
	@dna = <dna_file>;
	close dna_file;
	$dna = join('', @dna); # convert to string
	$dna =~ s/\s//g; # strip whitespace
	@dna = split('', $dna); # explode string to array
	$countA = 0;
	$countC = 0;
	$countG = 0;
	$countT = 0;
	$errors = 0;
	for ($pos = 0; $pos < length $dna; $pos++) {
		$base = substr($dna, $pos, 1);
		if ($base eq 'A') {
			$countA++;
		}
		elsif ($base eq 'C') {
			$countC++;
		}
		elsif ($base eq 'G') {
			$countG++;
		}
		elsif ($base eq 'T') {
			$countT++;
		}
		else {
			print "Error: unrecognized base: $base\n";
			$errors++;
		}
	}
	print "A: $countA\n";
	print "C: $countC\n";
	print "G: $countG\n";
	print "T: $countT\n";
	print "Errors: $errors\n";
	print "\n";
}
sub e5_7 {
	print "Example 5-7\n";
	$dna_filename = "small.dna";
	open(dna_file, $dna_filename);
	@dna = <dna_file>;
	close dna_file;
	$dna = join('', @dna);
	$dna =~ s/\s//g;
	$a = 0;
	$c = 0;
	$g = 0;
	$t = 0;
	$e = 0;
	while($dna =~ /a/ig) {$a++}
	while($dna =~ /g/ig) {$g++}
	while($dna =~ /c/ig) {$c++}
	while($dna =~ /t/ig) {$t++}
	while($dna =~ /[^acgt]/ig) {$e++}
	print "A=$a C=$c G=$g T=$t errors=$e\n";
	$outfilename = "count_base";
	unless ( open(count_base, ">$outfilename") ) {
			print "Can't open file \"$outfilename\"\n\n";
			exit;
	}	
	print count_base "A=$a C=$c G=$g T=$t errors=$e\n";
	close count_base;
}
e5_1();
e5_2();
e5_3();
e5_4();
e5_5();
e5_6();
e5_7();
exit;

