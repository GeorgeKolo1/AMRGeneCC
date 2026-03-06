import pandas as pd
import glob
import os


def AMR_gene_concat(folder):
    

    # Get all .fasta.gz.txt files
    files = glob.glob(os.path.join(folder, '*.fasta.gz.txt'))

    d_gene = {}
    d_antimicrobial = {}


    for f in files:
        basename = os.path.basename(f)
        # Extract the part between the time stamp and .scaffold
        # e.g. "2025-12-02_10:00:09.078_SAL_EA1800AA_AS.scaffold.fasta.gz.txt"
        #  -> "SAL_EA1800AA_AS"
        sample_name = basename.split('.scaffold')[0]           # everything before .scaffold
        sample_name = '_'.join(sample_name.split('_')[2:])     # drop date and time parts

        temp_df = pd.read_csv(f, sep='\t')
        temp_df['sample'] = sample_name
        for i in temp_df['sample']:
            d_gene[f'{i}'] = temp_df['Best_Hit_ARO']
            d_antimicrobial[f'{i}'] = temp_df['Antibiotic']

    temp_df_gene = pd.DataFrame(data=d_gene)
    temp_df_antibiotic = pd.DataFrame(data=d_antimicrobial)

    temp_df_gene.to_csv(folder + 'AMR_genes_results.csv')
    temp_df_antibiotic.to_csv(folder + 'AMR_antibiotic_results.csv')

    

    
