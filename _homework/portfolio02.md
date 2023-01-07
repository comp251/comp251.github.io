---
layout: default
title: "Programming Portfolio (kata 2)"
nav_order: 5
nav_exclude: true
---

# Programming Kata 2

Change your working directory to your portfolio and __create a new branch
for this assignment__.

```
$ cd <your-portfolio-directory>
$ git checkout -b <your-branch-name>
```

Now, create a subdirectory for this exercise and change your working directory
to inside it.

```
$ mkdir exercise02
$ cd exercise02
```

Now create your C file and start coding!

```
$ vim cipher.c
```

# Assignment

Write a program that accepts a 26-character string that represents a
[substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher).

For example, if the input is `qwertyuiopasdfghjklzxcvbnm`, then the letter `a`
will be replaced by `q`, `b` with `w`, `c` with `e`, etc.

Your program should then enter a loop to encipher/decipher text.

```
$ gcc cipher.c -o cipher
$ ./cipher
Enter substitution pad: qwertyuiopasdfghjklzxcvbnm
hello world! this is plaintext -- let's see it in ciphertext!
itssg vgksr! ziol ol hsqofztbz -- stz'l ltt oz of eohitkztbz!
this is another test. The encipher/decipher does not need to USE CAPITAL LETTERS
or punctuation...they can be ignored.
ziol ol qfgzitk ztlz. Tit tfeohitk/rteohitk rgtl fgz fttr zg USE CAPITAL LETTERS
gk hxfezxqzogf...zitn eqf wt oufgktr.
^C
```

## Tips

* `char` is an integer type, and characters are represented as numeric values
  internally. A common encoding of basic characters used in English is
  [ASCII](https://en.wikipedia.org/wiki/ASCII).
* You can use this by performing arithmetic and comparison between characters in
  strings and letters. (e.g., `str[i] >= 'a'` evaluates to true if the character
  at position `i` is a letter "greater than" `a`).
* You can also perform arithmetic with characters: `'d' - 2` evaulates to `b`,
  for example. Likewise `'d' - 'a'` evaluates to 4.

# Turning it in

When you are complete, commit your code and create a pull request with your
exercise. 

Change to the root directory of your repository:

```
$ cd ..                 
```

Add a line to the `.gitignore` file to exclude your binary.

```
$ echo exercise02/cipher >> .gitignore
```

Add the new directory (and file) to your staged commit and verify your files 
are staged.

```
$ git add exercise02
$ git status
```

Commit your code and push it to GitHub!

```
$ git commit -m "<your commit message>"
$ git push -u origin <your-branch>
```

There will be a link to create a pull request in the upload message. Click the
link and create a PR. Add one of the TAs as a reviewer!
