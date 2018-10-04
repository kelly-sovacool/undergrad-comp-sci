#!/usr/bin/perl
# http://stackoverflow.com/questions/11088538/how-to-get-post-values-in-perl
#
use strict;
use warnings FATAL => 'all';
use CGI qw();

#
# NOTE: this example does NOT produce a complete HTML document.......
#

my $c = CGI->new;
	if (!$c->request_method) {
		print "You're on the command line!\n";
		exit;
	}

print $c->header('text/plain');

if ('GET' eq $c->request_method) {
	if ($c->param('lname') && $c->param('fname') && $c->param('mname')) {
#		print "All parameters present.....";
		my $output = do_conversion($c, $c->param('lname'),
			$c->param('fname'),
			$c->param('mname')
			);
#		print "Output = ", $output;
	} else {
		print "Missing a parameter";
		exit;
	}
}
exit;

sub
do_conversion {
# note: poorly named variables
    my $form= $_[0];
	my $a	= $_[1];
	my $b	= $_[2];
	my $c	= $_[3];
	my $rc	= "Just a demo";


	print "do_conversion: ", $a, " ", $b, " ", $c;
	return $rc;
}



















