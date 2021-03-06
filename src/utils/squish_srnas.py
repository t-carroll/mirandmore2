#!/usr/bin/env python

import argparse, sys
from collections import defaultdict
from pprint import pprint

def squish(mat):
    
    precursors_pos = defaultdict(lambda: defaultdict(dict))
    
    if mat is '-':
        m = sys.stdin
    else:
        m = open(mat, 'r')

    for srna in m:            
        
        f = srna.strip().split()
        pre = f[0].strip()
        mir = f[1].strip()
        start = int(f[2].strip())
        end   = int(f[3].strip())

        if mir in precursors_pos[pre]:
            if start > precursors_pos[pre][mir][0]:
                start = precursors_pos[pre][mir][0]
            if end < precursors_pos[pre][mir][1]:
                end = precursors_pos[pre][mir][1]                    

        precursors_pos[pre][mir] = [start, end]

    m.close()

    #print(pprint(precursors_pos))
    for k,v in precursors_pos.items():
        for kk, vv in v.items():
            outline_list = ['mock', k, kk, '.', str(vv[0]), str(vv[1])]
            print('\t'.join(outline_list))

            

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i','--input', dest = 'infile', required = True, 
                        help = '''A semicolon separated file as '''\
                               '''pre;mature;start;end . Easily '''\
                               '''generated by command '''\
                               '''grep -v "^pre" raw_variants.txt | cut -f1,2,4,5 . '''\
                               '''Outputs a mock mature-table.txt like format.'''\
                               '''Useful to generate an input for gff2maturetable.p -r''')
    
    args = parser.parse_args()

    squish(args.infile)

