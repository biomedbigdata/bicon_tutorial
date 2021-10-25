# Tutorial for BiCoN package
## Running the example 
1. Make sure you have conda/miniconda installed.
You can do that by running any of conda commands, e.g.
```{bash}
conda list
```
If you do not have conda, follow the instruction here for the installation https://conda.io/projects/conda/en/latest/user-guide/install/index.html
3. Download this repository to your computer
4. Create a folder "data" inside and download there everything from this folder https://drive.google.com/drive/folders/1M_cYMbIvPhHoPe5rayqjTxFa3Vo0af8w?usp=sharing
5. Create an environment with the necessary packages with the following command
```{bash}
conda env create -f environment.yml
```
5. Activate the environment
```{bash}
conda activate bicon_env
```
6. Allow jupyter notebook to use the created environment
```{bash}
python -m ipykernel install --user --name=bicon_env
```

7. Run jupyter notebook:
```{bash}
jupyter notebook
```
8. Open notebook_ht and make sure that you are connected to `bicon_env`, alternatively go to `Kernel` > `Change kernel` > `bicon_env`

## Running on your own data
1. Do the steps 1-6 if you haven't done that yet
2. Prepare your input data
Gene expression data is accepted in the following format:
- genes as rows.
- patients as columns.
- first column - genes IDs (can be any IDs).

For instance:

| Unnamed: 0 | GSM748056 | GSM748059 | ... | GSM748278 | GSM748279 | GSM1465989 |
|------------|-----------|-----------|-----|-----------|-----------|------------|
| 1454       | 0.053769  | 0.117412  | ... | -0.392363 | -1.870838 | -1.432554  |
| 201931     | -0.618279 | 0.278637  | ... | 0.803541  | -0.514947 | 2.361925   |
| 8761       | 0.215820  | -0.343865 | ... | 0.700430  | 0.073281  | -0.977656  |
| 2703       | -0.504701 | 1.295049  | ... | 1.861972  | 0.601808  | 0.191013   |
| 26207      | -0.626415 | -0.646977 | ... | 2.331724  | 2.339122  | -0.100924  |


### Network (if you have one)

An interaction network should be present as a table with two columns that represent two interacting genes. **Without a header!**

For instance:

| 6416 | 2318 |
|------|------|
| 6416 | 5371 |
| 6416 | 351  |
| 6416 | 409  |
| 6416 | 5932 |
| 6416 | 1956 |

**BiCoN does not care about gene IDs as long as they are the same for both gene expression and the PPI network.**


So, if you do not have a PPI network you want to use or your network has gene IDs that are different from the ones in your expression data, please do the following:
In the working directory of the tutorial run

```{bash}
python ppi_converter.py --gene_id entrezgene --convert_to "needed gene id" --path data/biogrid.human.entrez.tsv
```
Replace "needed gene id" with gene IDs that you have in your gene expression matrix. Can be 'ensemblgene', 'symbol','refseq', 'unigene', 'homologene', 'uniprot'.
If you do not want to use provided biogrid network, then replace "path data/biogrid.human.entrez.tsv" with the path to the network you need to convert.

For more details on the converted please run:

```{bash}
python ppi_converter.py -h
```

**NOTE if you use gene IDs other than entrez**:

When you are going to process the results, do not forget to modifu origID parameter in this line of code:

```{python}
results = results_analysis(solution, labels, convert = True, origID = 'entrezgene')
```

origID should represent the original gene IDs whch can be 'ensemblgene', 'symbol','refseq', 'unigene', 'homologene', 'uniprot'.
