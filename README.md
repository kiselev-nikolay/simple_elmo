# Simple ELMo
Minimal Python code to get vectors from pre-trained ELMo models in TensorFlow.

Based on https://github.com/ltgoslo/simple_elmo


# Instalation

`pip install git+https://github.com/machineandme/simple_elmo.git#egg=simple_elmo`

# Usage example

... ii ll write in next commit

# Text classification

Use this code to perform document pair classification (like in text entailment or paraphrase detection).

Simple average of ELMo embeddings for all words in a document is used;
then, the cosine similarity between two documents is calculated and used as a classifier feature.

Example datasets for Russian (adapted from http://paraphraser.ru/):
- https://rusvectores.org/static/testsets/paraphrases.tsv.gz
- https://rusvectores.org/static/testsets/paraphrases_lemm.tsv.gz (lemmatized)

`python3 text_classification.py --input paraphrases_lemm.tsv.gz --elmo ~/PATH_TO_ELMO/`


