#!/usr/bin/perl
# Kelly Sovacool
# 06 Oct. 2017

print "Enter input file name \n";
$infile=<STDIN>;
chop($infile);
print "Enter the output file name \n";
$outfile=<STDIN>;
chop($outfile);
print "Enter the bit score threshold \n";
$bitscore=<STDIN>;
chop($bitscore);
print "Enter the length threshold \n";
$len=<STDIN>;
chop($len);
unless (open(INFILE, $infile)){
   die("cant open input file "."\n");}
unless (open(OUTFILE, ">$outfile")){
   die("cant open output file "."\n");}

$line=<INFILE>;


while ($line ne "") {
        chop($line);
        @ary  = split (/\t/, $line);
        if ($ary[11] >= $bitscore) {
			if ($ary[3] >= $len) {
               print OUTFILE ("$ary[0]\t$ary[1]\t$ary[2]\t$ary[3]\t$ary[4]\t$ary[5]\t$ary[6]\t$ary[7]\t$ary[8]\t$ary[9]\t$ary[10]\t$ary[11]\n");
		}}
$line = <INFILE>;

}

