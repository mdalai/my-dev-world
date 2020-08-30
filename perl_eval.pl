#!/usr/bin/perl -T

use strict;
use warnings;


## The module may not installed, so use followings instead of use File::Slurp;
eval "use File::Slurp; 1" or warn "File::Slurp is not available: $@";



print "START perl\n";

my ($answer, $a, $b);
$a = 10;
$b = 0;

## Shall exit if use following
#$answer = $a / $b;

## Eat up the error and continue if use following
eval { $answer = $a / $b; }; warn $@ if $@;

print "ans= $answer \n";

## Shall exec following no matter failure or success
END {
    print "END perl NO MATTER WHAT\n";
}


