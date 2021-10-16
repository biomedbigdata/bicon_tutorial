# Tutorial for BiCoN package
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
