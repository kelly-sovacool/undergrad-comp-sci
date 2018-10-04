#!/usr/bin/perl
print "Content-type: text/html\n\n";

# Note, this is the "manual" way of getting the fields/values

my @values = split(/&/,$ENV{QUERY_STRING});

foreach my $i (@values) {
	my($fieldname, $data) = split(/=/, $i);
	print "$fieldname = $data<br>\n";
}

print "\n\n\n - example CGI code from cgi101.com/boot/ch3/text.html\n";
