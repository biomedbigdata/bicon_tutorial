# Tutorial for BiCoN package
1. Download this repository to your computer
2. Create a folder "data" inside and download there everything from this folder https://drive.google.com/drive/folders/1M_cYMbIvPhHoPe5rayqjTxFa3Vo0af8w?usp=sharing
3. Create environment will the nessesary packages with the following command
```{bash}
conda env create -f environment.yml
```
4. Activate the environment
```{bash}
conda activate bicon_env
```
5. Allow jupyter notebook to use the created environment
```{bash}
python -m ipykernel install --user --name=bicon_env
```

6. Run jupyter notebook:
```{bash}
jupyter notebook
```
7. Open notebook_ht and make sure that you are connected to `bicon_env`, alternatevely go to `Kernel` > `Change kernel` > `bicon_env`
