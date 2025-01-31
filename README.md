# Shizuka App

![](https://github.com/cat-milk/Anime-Girls-Holding-Programming-Books/blob/master/Rust/Shizuka_Yoshimoto_The_Rust_Programming_Language.png?raw=true)

好本静, Yoshimoto Shizuka is a character from 君のことが大大大大大好きな100人 that talks through voice synthesis software. This repo shares my attempt around synthesizing her voice with the [VITS](https://github.com/jaywalnut310/vits) algorithm.

## Extract

In the anime her voice first appeared in S01E03. Chinese subtitles provided through a collaboration of team Airota, Nekomoe kissaten and LoliHouse (thank you and all voluntary sub teams!) quote all Shizuka lines with 「」, indicating voice synthesis, and also contain Japanese original text inside. It is then trivial to extract timestamps of all Shizuka lines with minimal processing from the subtitles.

As I respect anime copyrights as much as how streaming platforms respect creators, no video or audio artifacts will be provided here. Inside the folder contains scripts I use and extracted timestamp info. The naive criteria of "lines starting with 「 are all Shizuka lines" will have some false positives, and not all lines are clear of voices from other characters, so hand filtered timestamp info is also provided.

## Preprocess

As explained above, no media artifacts will be provided here. In my local directory, I am doing further manual filtering with Kdenlive and storing intermediate processing artifacts (from the notebook to be explained later).

## Training

The notebook provided here is a modified version of the notebook provided at [VITS-fast-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning), with my fixes to revive it in 2025. For the first trained model, I obtained it through training for 200 epochs, 40 minutes with 1 A100 on Google Colab Pro.

## Inference

Inside the folder contains trained model(s) (stored with Git LFS apparently) and associated metadata, a pointer to my fork of [MoeGoe](https://github.com/CjangCjengh/MoeGoe), a voice synthesis engine wrapper, and required info to get a demo running.

For complete starters:

```sh
# install and init Git LFS first, for Archlinux users:
sudo pacman -S git-lfs
git lfs install
# assume Git LFS is ready
git lfs clone --recurse-submodules https://github.com/Richardn2002/shizuka-app
cd shizuka-app/03\ inference
python3.11 -m venv .venv
source activate .venv
pip install -r requirements.txt
python main.py
```

## 🤗 Spaces Deployment

Live demo hosted on [Hugging Face Spaces](https://huggingface.co/spaces/Richardn2002/shizuka-app).

Sadly, HF Spaces does not support initialization of git submodules and require a dedicated repo for uploading applications, so the related files will not be hosted in this repo, however they can be easily accessed [here](https://huggingface.co/spaces/Richardn2002/shizuka-app/tree/main), which include metadata, an application main, and a copy of the forked MoeGoe.
