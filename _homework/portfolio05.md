---
layout: default
title: "Kata 5 (Due 4/14)"
nav_order: 9
nav_exclude: true
---

# Programming Kata 5

Change your working directory to your portfolio and __create a new branch
for this assignment__.

```
$ cd <your-portfolio-directory>
$ git checkout main
$ git checkout -b <your-branch-name>
```

Now, create a subdirectory for this exercise and change your working directory
to inside it.

```
$ mkdir exercise05
$ cd exercise05
```

For this exercise, you've been given some starter code. You can do the following
to download and extract it:

```
$ curl http://251.systems/assets/kata05-starter.tar.gz | tar -xz
```

Now create your C file and start coding!

```
$ vim sentiment.c
```

# Assignment

For this assignment, you will write a program that performs [sentiment
analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) for text input from
standard in.

## Sentiment Analysis

__Sentiment analysis__ is the algorithmic analysis of text that aims to identify
and quantify the subjective feeling behind written text.

For example, the sentence: "I hate Mondays" has negative sentiment, while the
sentence "I love lasagna" has positive sentiment.

These examples are obvious, but others may be more complex. There is a rich body
of research surrounding sentiment analysis; [this
paper](https://link.springer.com/article/10.1007/s10462-022-10386-z) is a recent
survey of work in the area.

We will be implementing a fairly naive sentiment analysis algorithm: assign each
word in a sentence a sentiment value (positive or negative), and sum the
sentiment of each word.

For example, suppose we have the following map from words to sentiment values:

| word | sentiment (postive, negative) |
|---|---|
| i | (+0, -0.0625) |
| love | (+0.3875, -0.0125) |
| hate | (+0.0625, -0.5625) |
| lasagna | (+0, -0) |

The value of each sentence would then be:

| sentence | sum of sentiments | total | verdict |
| "I hate Mondays" | 0 - 0.0625 + 0.0625 - 0.5625 | __-0.5625__ | negative |
| "I love lasagna" | 0 - 0.0625 + 0.3875 - 0.0125 + 0 - 0 | __0.3125__ | positive |

## Data set

We will be using a dataset pre-populated with sentiment values for words. It is
already present on lily/iris and can be found via the path
`/opt/share/251/data/sentiments.txt`. A description of the dataset can be found
[here](https://github.com/aesuli/SentiWordNet). 

{: .note }
The quality of this dataset is not really an objective of the lab, we are just
using it because it is readily available and relatively straightforward to
parse. You can find a ton of open datasets on
[Kaggle](https://www.kaggle.com/datasets?search=sentiment+analysis) and linked
from papers in the survey linked previously.

If you open the data set to take a look at it
(e.g., in Vim---`$ vim /opt/share/251/data/sentiments`), you'll see that it has
the following format:

* Comment lines are prefixed with `#`.
* Non comment lines consist of 6 fields that are separated by tabs. The six
  fields are:

  1. Part of speech: adjective (`a`), adverb (`r`), noun (`n`), or verb (`v`).
  2. Word ID: a unique ID from the [Wordnet](http://wordnet.princeton.edu)
     database.
  3. Positive score: a value indicating the positive sentiment of the word.
  4. Negative score: a value indicating the negative sentiment of the word.
  5. A list of terms: terms are of the format `word#sense`. There may be
     multiple terms per line; if so, they are separated by spaces.

     {: .note }
     The sense number refers to how the word is used. There are multiple ways to
     use the word "cool", for example: "It was cool outside, so I rode my cool
     skateboard to work. I fell off while going off a curb, but played it cool."
     In this database, cool would therefore appear three times as `cool#1`,
     `cool#2`, and `cool#3` with different sentiments (e.g., one is neutral and
     describes temperature, the second is positive and denotes the
     fashionable nature of a skateboard, and the third is positive and describes
     self-control. The numbering also corresponds to part of speech, so there
     may be up to four `cool#1` entries (adjective, adverb, noun, verb)---and
     in the case of "cool", there are indeed four.

  6. A definition of the term/terms.

## Program specification

Your program should accept one command line parameter: the name of the file to
read the sentiment data from (`/opt/share/251/data/sentiments.txt`). It should
read the file and compute the mean sentiment for every word in the file.

* You should keep track of the __average__ positive and negative sentiment
  values for a word, since our program will not be intelligent enough to account
  for parts of speech. 

* You should keep track of _normalized_ words and discard punctuation like
  hyphenation or capitalization.

After reading and processing the input file, your program should accept lines of
text from standard in and compute the sentiment value for each line (simply sum
the positive and negative sentiments for each word).

Here's an example:

```
$ ./sentiment /opt/share/251/data/sentiments.txt
loading sentiment map...loaded.
I hate Mondays
I hate Mondays : -0.562500
I love lasagna
I love lasagna : 0.312500
I love him so much he is perfect. He is my rotten soldier. He’s such a silly guy. Just a little guy really. He WILL eat all your lasagna. He took my Baja Blast.
I love him so much he is perfect. He is my rotten soldier. He’s such a silly guy. Just a little guy really. He WILL eat all your lasagna. He took my Baja Blast. : 0.676786
```

## Handout code

For this exercise, you've been given a decent chunk of starter code. Namely:

* You will use your map from lab 3 to implement this assignment. Your code will
  use a map to keep a mapping from strings (words) to their sentiment values.

* You have a struct `sentiment_t` that should be used to keep track of the
  positive and negative sentiments for a word. This struct also has a `count`
  field that you can use when you are computing mean values (see tips below).

* You have been given a function `lower_and_strip` that can normalize a string
  by removing all non-letter characters and converting all letters to lowercase.
  You can call this function with words from the dataset and from input text.

* There are a couple of functions that can be used to manipulate your map:
  `dump_sentiments` and `free_map_values`.

* You've been given the start of a function `build_sentiment_map` that you will
  complete to construct the sentiment map. 


## Tips

* Remember that since you are using a library, you will need to link the `map.o`
  code with yours:

  ```
  $ gcc -o sentiment sentiment.c map.o
  ```

* When you are constructing the map and have a word that you want to add, you
  will need to use `map_get` in order to check whether a value is in the map and
  get the existing value.

  * If so, you need to update that value with the new averages/count and then
    put it back in the map using `map_put`.
  * If not, you will need to _create a new struct on the heap_ to put in the map
    with the first values that you read.

  The values you should be storing in the map are pointers to sentiments, so
  you'll have something that looks similar to this to get a value:

  ```
  sentiment_t *senti;
  int in_map = map_get(sentiments, term, (void**) &senti);
  ```

* You can compute an updated mean without the history of terms using the
  following:

  ```
  new_mean = old_mean + (new_value - old_mean) / count
  ```

* When you compute the sentiment of a line of input, you can tokenize the input
  on spaces, and use `lower_and_strip` to normalize the word.

* When tokenizing the input file, `\t` is the character that represents a tab.

* You can use `atof` to parse a string into a double.

* When parsing a line, you'll want to use `strtok` to split the line on tabs.
  You'll also want to further split the words field on spaces, and each word
  based on the `#`. For example, a line will look like the following (`\t`
  represents tab characters):

  ```
  n\t08783812\t0\t0\trodhos#1 rhodes#2\ta Greek island in the southeast Aegean ...
  ```

  You will need to split the line on tabs to retrieve the fields, and you'll
  need to split the field `rodhos#1 rhodes#2` on spaces. You'll further need to
  extract `rodhos` and `rhodes` from `rodhos#1` and `rhodes#2`, respectively.

  __Be aware that you cannot use `strtok` to start parsing a string while you
  are in the middle of parsing another string__.

  There are multiple ways to code this, including using `strtok`, but you can
  also look at `strchr` and `strtok_r`, which may make your life easier.

# Turning it in

When you are complete, commit your code and create a pull request with your
exercise. 

Change to the root directory of your repository:

```
$ cd ..                 
```

Add a line to the `.gitignore` file to exclude your binary.

```
$ echo exercise05/sentiment >> .gitignore
```

Add the new directory (and file) to your staged commit and verify your files 
are staged.

```
$ git add exercise05
$ git status
```

Commit your code and push it to GitHub!

```
$ git commit -m "<your commit message>"
$ git push -u origin <your-branch>
```

There will be a link to create a pull request in the upload message. Click the
link and create a PR. Add me as reviewer.
