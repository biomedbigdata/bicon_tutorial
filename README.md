# Tutorial for BiCoN package
## Running the notebooks
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

1. Performe steps 1-5 from the previous section if you havn't done that yet.
2. Prepare your data:
### Gene expression

Gene expression is accepted in the following format:
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


### Network

An interaction network should be present as a table with two columns that represent two interacting genes. **Without a header!**

For instance:

| 6416 | 2318 |
|------|------|
| 6416 | 5371 |
| 6416 | 351  |
| 6416 | 409  |
| 6416 | 5932 |
| 6416 | 1956 |

There is an example of a PPI network from BioiGRID with experimentally validated interactions [here](https://drive.google.com/drive/folders/1J0XRrklwcV_Cgy_9Ay_6yJrN_x28Cosk?usp=sharing).
