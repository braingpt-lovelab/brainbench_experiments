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
3. Run inference with all LLMs on BrainBench test cases under the **swapped context** condition: `python run_choice_swap.py --use_human_abstract <True|False>`.
4. Run memorization analysis:
    * First compile data from biorxiv and arxiv: `python compile_biorxiv.py` and `python compile_arxiv.py`. For now, need to manually adjust year range inside the scripts.
    * Run inference to obtain zlib entropy of BrainBench test cases: `python run_choice_zlib.py`.
    * Run inference to obtain zlib entropy and perplexity of all compiled data from biorxiv, arxiv and the Gettysburg Address: `python dataset_ppl_zlib.py`. For now, the choice of which data source to run needs to be set manually inside the script.

### Results and plotting
* All analyses results (pre-plotting) are saved in `model_results` grouped by LLM names and further organized by experiment type such as inference without context.
* For obtaining figures in the paper, please refer to the dedicated repo for plotting here: https://github.com/braingpt-lovelab/brainbench_results.

### Attribution
```
@article{luo_large_2024,
	title = {Large language models surpass human experts in predicting neuroscience results},
	issn = {2397-3374},
	url = {https://www.nature.com/articles/s41562-024-02046-9},
	doi = {10.1038/s41562-024-02046-9},
	abstract = {Abstract
            Scientific discoveries often hinge on synthesizing decades of research, a task that potentially outstrips human information processing capacities. Large language models (LLMs) offer a solution. LLMs trained on the vast scientific literature could potentially integrate noisy yet interrelated findings to forecast novel results better than human experts. Here, to evaluate this possibility, we created BrainBench, a forward-looking benchmark for predicting neuroscience results. We find that LLMs surpass experts in predicting experimental outcomes. BrainGPT, an LLM we tuned on the neuroscience literature, performed better yet. Like human experts, when LLMs indicated high confidence in their predictions, their responses were more likely to be correct, which presages a future where LLMs assist humans in making discoveries. Our approach is not neuroscience specific and is transferable to other knowledge-intensive endeavours.},
	language = {en},
	urldate = {2024-11-29},
	journal = {Nature Human Behaviour},
	author = {Luo, Xiaoliang and Rechardt, Akilles and Sun, Guangzhi and Nejad, Kevin K. and Yáñez, Felipe and Yilmaz, Bati and Lee, Kangjoo and Cohen, Alexandra O. and Borghesani, Valentina and Pashkov, Anton and Marinazzo, Daniele and Nicholas, Jonathan and Salatiello, Alessandro and Sucholutsky, Ilia and Minervini, Pasquale and Razavi, Sepehr and Rocca, Roberta and Yusifov, Elkhan and Okalova, Tereza and Gu, Nianlong and Ferianc, Martin and Khona, Mikail and Patil, Kaustubh R. and Lee, Pui-Shee and Mata, Rui and Myers, Nicholas E. and Bizley, Jennifer K. and Musslick, Sebastian and Bilgin, Isil Poyraz and Niso, Guiomar and Ales, Justin M. and Gaebler, Michael and Ratan Murty, N. Apurva and Loued-Khenissi, Leyla and Behler, Anna and Hall, Chloe M. and Dafflon, Jessica and Bao, Sherry Dongqi and Love, Bradley C.},
	month = nov,
	year = {2024},
}
```
