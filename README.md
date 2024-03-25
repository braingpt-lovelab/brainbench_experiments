# brainbench_experiments

### To work with the repo locally:
```
git clone git@github.com:braingpt-lovelab/brainbench_experiments.git --recursive
```
### To create conda environment:
```
conda env create -f conda_envs/environment.yml
```

### Reproducing experiments from scratch:
1. Run inference with all LLMs on BrainBench test cases: `python run_choice.py --use_human_abstract <True|False>`.
2. Run inference with all LLMs on BrainBench test cases under the **without context** condition: `python run_choice_iso.py --use_human_abstract <True|False>`.
3. Run memorization analysis:
    * First compile data from biorxiv and arxiv: `python compile_biorxiv.py` and `python compile_arxiv.py`. For now, need to manually adjust year range inside the scripts.
    * Run inference to obtain zlib entropy of BrainBench test cases: `python run_choice_zlib.py`.
    * Run inference to obtain zlib entropy and perplexity of all compiled data from biorxiv, arxiv and the Gettysburg Address: `python dataset_ppl_zlib.py`. For now, the choice of which data source to run needs to be set manually inside the script.

### Results and plotting
* All analyses results (pre-plotting) are saved in `model_results` grouped by LLM names and further organized by experiment type such as inference without context.
* For obtaining figures in the paper, please refer to the dedicated repo for plotting here: https://github.com/braingpt-lovelab/brainbench_results.
