import argparse
import sys

from amrgene.amr_gene_script import AMR_gene_concat

def main():
    parser = argparse.ArgumentParser(
        description='Concatenate AMR gene results from RGI output files'
    )
    parser.add_argument(
        'folder',
        help='Path to the folder containing your AMRFinder results file (should end in .fasta.gz.txt)',
    )

    args = parser.parse_args()
    AMR_gene_concat(args.folder)

if __name__ == "__main__":
    main()