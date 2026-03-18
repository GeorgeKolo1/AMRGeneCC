import argparse

from amrgene.amr_gene_script import AMR_gene_concat

def main():
    parser = argparse.ArgumentParser(
        description='Concatenate AMR gene results from RGI output files'
    )
    parser.add_argument(
        'folder',
        help='Path to the folder containing your AMRFinder results file (should end in .fasta.gz.txt)',
    )
    parser.add_argument(
        'column_1',
        help='Name of the column in the AMRFinder results file',
    )
    parser.add_argument(
        'column_2',
        help='Name of another column in the AMRFinder results file',
    )

    args = parser.parse_args()
    AMR_gene_concat(args.folder, args.column_1, args.column_2)

if __name__ == "__main__":
    main()