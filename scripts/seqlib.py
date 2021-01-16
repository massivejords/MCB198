import gzip

def read_fasta(filename):

    name = None
    seqs = []

    fp = None 
    if filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
    else: fp = open(filename)

    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            if len(seqs) > 0:
                seq = ''.join(seqs)
                yield(name, seq)
                name = line[1:]
                seqs = []
            else:
                name = line[1]
        else:
            seqs.append(line)
    yield(name, ''.join(seqs))
    fp.close()
