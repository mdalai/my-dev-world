#!/usr/bin/perl -T

use strict;
use warnings;

## Try to use following if the module is installed
#use File::Slurp;


our $FILE = 'data.txt';
our $CONTENT = qq{
    Hello, this is a test text;
    line 2: applec.
    line 3: orangec.
};

# pure perl read
sub read_file {
    my ($filename) = @_;
 
    open my $in, '<:encoding(UTF-8)', $filename or die "Could not open '$filename' for reading $!";
    local $/ = undef;
    my $all = <$in>;
    close $in;
 
    return $all;
}
 
# pure perl write
sub write_file {
    my ($filename, $content) = @_;
 
    open my $out, '>:encoding(UTF-8)', $filename or die "Could not open '$filename' for writing $!";;
    print $out $content;
    close $out;
 
    return;
}

# replicate the slurp
sub slurp {
    my $file = shift;
    open my $fh, '<', $file or die;
    local $/ = undef;
    my $cont = <$fh>;
    close $fh;
    return $cont;
}


write_file($FILE, $CONTENT);
my $rv = read_file($FILE);
print $rv;

END {
   unlink $FILE;
}

