# Text-generator
A simple text generator based on trigrams.

You will need to unzip the dataset data.zip and put it in the same location as main.py

## Dataset contents:
- https://www.kaggle.com/datasets/mylesoneill/classic-literature-in-ascii
- https://www.kaggle.com/datasets/snapcrack/all-the-news
- I believe I also added some wikipedia paragraphs, but I forget where they were from.

The dataset may include non-words as I have not formatted it to remove these.

### Setup variables:
- wordDelay: delay between words. default 0
- numWords: number of words printed. default 30
- autoUpdate: live print the words. default True

### Dependencies:
- nltk

built in:

- import random
- import pickle
- import time

There may be some missing for commented sections of code.

### Commented sections:
I commented some sections out that were used to convert the dataset into trigrams and save it as a pickle file. If you want to use your own dataset, you will need to uncomment and comment out some parts. I currently have no method to easily do this through the commandline.
