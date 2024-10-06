from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser and FastqParser
    
    aparser = FastaParser('data/test.fa')
    qparser = FastqParser('data/test.fq')
    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console

    for i, (seq, line) in enumerate(aparser):
        print(i, seq, line)
        
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console

    #for line in qparser:
    #    print(line)

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    
    #for line in aparser: 
    #    print(transcribe(line[1]))
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    
    #for line in qparser: 
    #    print(reverse_transcribe(line[1]))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
