# Scholary document summarization

### Part 1: Data Extraction

#### Implementation details:
- Download dataset from [here](https://ncg-task.github.io/data.html)
- Code: [Data Extraction.ipynb](https://github.com/Rohan191/research-contribution-extraction/blob/master/code/Data%20Extraction.ipynb)
- Loop through data to extract abstract, sentences and store data in a dataframe

### Part 2: Extractive summary for contributing statements
#### Implementation details:
- Code: [Extractive summary for contributions.ipynb](https://github.com/Rohan191/research-contribution-extraction/blob/master/code/Extractive%20summary%20for%20contributions.ipynb)
- Use SBert (Sentence-Bert) based [sentence transformer](https://huggingface.co/sentence-transformers) to generate embeddings for each sentence
- Use LSTM based model on top of SBert embeddings to classify a sentence as contributing or not
- Extract contributing statements for each document

![Model architecture for extractive text summarization](/assets/images/model_architecture.png)

### Part 3: Generate abstractive summary 
#### Implementation details:
- Code: [Abstractive summary.ipynb](https://github.com/Rohan191/research-contribution-extraction/blob/master/code/Abstractive%20summary.ipynb)
- Use [Facebook Bart model](https://huggingface.co/sshleifer/distilbart-cnn-12-60) to generate abstractive summary from contributing statements
- Calculate scores on metrics - rouge1, rouge2, rougel, bert score

### Part 4: Apply all the above steps on a new pdf scholarly document
#### Implementation details:
- Code: [Application to new papers.ipynb](https://github.com/Rohan191/research-contribution-extraction/blob/master/code/Application%20to%20new%20papers.ipynb)
- Use [`pymupdf`](https://pymupdf.readthedocs.io/en/latest/tutorial.html) python library to extract blocks of text from a given pdf document
- Extract abstract and sentences from the pdf document
- Apply steps in Part 1, 2 and 3 to generate summary and metrics 


### References:
- Liu, Yang. "Fine-tune BERT for extractive summarization." arXiv preprint arXiv:1903.10318 (2019).
- Reimers, Nils, and Iryna Gurevych. "Sentence-bert: Sentence embeddings using siamese bert-networks." arXiv preprint arXiv:1908.10084 (2019).
- Lewis, Mike, et al. "Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension." arXiv preprint arXiv:1910.13461 (2019).
- Bi, Keping, et al. "Aredsum: Adaptive redundancy-aware iterative sentence ranking for extractive document summarization." arXiv preprint arXiv:2004.06176 (2020).
- Allahyari, Mehdi, et al. "Text summarization techniques: a brief survey." arXiv preprint arXiv:1707.02268 (2017).
