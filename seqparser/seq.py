# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    for char in seq: 
        if char == 'T':
            seq = seq.replace('T', 'U')
    return seq 


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq)[::-1]