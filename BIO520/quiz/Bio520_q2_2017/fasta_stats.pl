#!/usr/bin/perl

print "Enter file containing a list of fastafile names \n";
# read a filename from standard input
$infile=<STDIN>;
chop($infile);
print "Enter the output file name \n";

# read an output filename from standard input
$outfile=<STDIN>;
chop($outfile);
unless (open(INFILE,$infile)){
   die("cant input file "."\n");}
unless (open(OUTFILE,">$outfile")){
   die("cant open output file "."\n");}

# read lines from the designated file of target filenames (listed in the input file) 
$fileline=<INFILE>;
chop ($fileline);
while ($fileline ne ""){

# open the target files
  unless (open(INFILE2,$fileline)){
     die("cant input file $fileline "."\n");}

# read a line from the target file
  $line=<INFILE2>;

# set counts to zero
  $acount =$ccount = $gcount = $tcount = $xcount = $ncount = $sequence_length = 0;


     while ($line ne "") {
          if ($line =~ /^\>/) {
              chop ($line);
              $sequence_length=$acount + $ccount + $gcount + $tcount + $ncount + $xcount;
              $Sequence_name = $line;
              $acount =$ccount = $gcount = $tcount = $xcount = $ncount = $seqcount = 0;
# process sequence lines
          }else{
              chop ($line);
              $_ = $line;
# counts each base in the current line
              $acount += tr/aA/aA/;
              $ccount += tr/cC/cC/;
              $gcount += tr/gG/gG/;
              $tcount += tr/tT/tT/;
              $ncount += tr/nN/nN/;
              $xcount += tr/xX/xX/;
			  $sequence_length=$acount + $ccount + $gcount + $tcount + $ncount + $xcount;
			  print OUTFILE ("$Sequence_name\t$sequence_length\t$acount\t$ccount\t$gcount\t$tcount\t$ncount\t$xcount\n");
             }
         $line = <INFILE2>;
     }
$sequence_length=$acount + $ccount + $gcount + $tcount + $ncount + $xcount;
$fileline=<INFILE>;
chop ($fileline);
}
