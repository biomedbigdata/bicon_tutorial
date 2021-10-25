import pandas as pd
import mygene
import argparse
import warnings
warnings.filterwarnings("ignore")
parser = argparse.ArgumentParser()
parser.add_argument("--gene_id", help="Specify gene IDs in your network. Possible options: 'entrezgene', 'ensemblgene',\
                    'symbol','refseq', 'unigene', 'homologene', 'uniprot', for other option please refer to \
                    https://docs.mygene.info/en/latest/doc/query_service.html#available_fields ",required=True,)
parser.add_argument("--convert_to", help="Specify gene IDs you need to convert to, Possible options: 'entrezgene', 'ensemblgene',\
                    'symbol','refseq', 'unigene', 'homologene', 'uniprot', for other option please refer to \
                    https://docs.mygene.info/en/latest/doc/query_service.html#available_fields",required=True,)
parser.add_argument("--path", help="Specify path to your network",required=True,)


parser.add_argument("--species", help = "Specify species. Options: 'human', 'mouse', 'rat'. Default: human",
                   default = 'human',required=False)

args = parser.parse_args()

network = pd.read_csv(args.path, sep = "\t", header = None)
network = network.astype(str)
all_genes = list(set(list(network[0]) + list(network[1])))
mg = mygene.MyGeneInfo()
print("Querying genes ...")
out = mg.querymany(all_genes, args.gene_id, species = args.species, 
                   fields=args.convert_to, verbose=False, 
                   as_dataframe = True)
mapping = out[out.notfound.isna()][args.convert_to].to_dict()
print("Replacing the values ...")

network[0] = network[0].map(mapping)
network[1] = network[1].map(mapping)
network.to_csv(f"network_{args.convert_to}.tsv", sep = "\t", header = None, index = False)