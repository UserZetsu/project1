# write tests for parsers

import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Now you can import your modules
from seqparser import FastaParser, FastqParser

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    aparser = FastaParser('data/test.fa')
    
    for i, (header, line) in enumerate(aparser):
        # Checks correct formatting
        assert header == f'seq{i}'
        



def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    qparser = FastqParser('data/test.fq')
    for i, (header, line, quality) in enumerate(qparser):
        assert header == f'seq{i}'
