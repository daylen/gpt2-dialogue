# Conversational Agents with GPT-2

This repo contains several git submodules.

## Preparing the Personal Chat History dataset

1. Follow the instructions in the `converscope` repo to prepare the `inbox.pb` data file. We are not supplying data for privacy reasons.
2. `python3 converscope/dump_gpt2.py` to dump train and test text files.

## Finetuning GPT-2

We experimented with several existing implementations of GPT-2 training.

### gpt-2-simple
The `gpt-2-simple` repo features a [Colab notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) that enables free GPU training on Colaboratory without having to pay for a GPU on Google Cloud

### transformers
We used the `transformers` repo to train GPT-2 models and evaluate perplexity. The following commands assume you are in the `transformers/examples` directory.

To finetune:

```
python3 run_lm_finetuning.py --output_dir=/home/daylenyang/gpt2_out/ --model_type=gpt2 --model_name_or_path=gpt2 --do_train --train_data_file=gpt2_train_daylenyang.txt --do_eval --eval_data_file=gpt2_test_daylenyang.txt --per_gpu_train_batch_size=2 --per_gpu_eval_batch_size=2
```

To evaluate perplexity, we drop the `--do_train` flag and make sure `--model_name_or_path` points to the correct path.

To generate:

```
python3 run_generation.py --model_type gpt2 --model_name_or_path=/home/daylenyang/gpt2_out/ --length 100
```