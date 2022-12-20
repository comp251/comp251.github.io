---
layout: default
title: "Programming Portfolio (kata N)"
nav_order: 99
nav_exclude: true
---

# Programming Kata N

Change your working directory to your portfolio and create a new branch
for this assignment.

```
$ cd <your-portfolio-directory>
$ git checkout -b <your-branch-name>
```

Now, create a subdirectory for this exercise and change your working directory
to inside it.

```
$ mkdir exerciseNN
$ cd exerciseNN
```

Now create your C file and start coding!

```
$ vim XXX.c
```

# Assignment

Write a program that repeatedly reads stings from standard input and then uses a
function to reverse a string. You can have a termination condition and check it
using `strcmp`, or you can just use CTRL-C to quit.

```
$ gcc 
$ ./
```

# Turning it in

When you are complete, commit your code and create a pull request with your
exercise. 

Change to the root directory of your repository:

```
$ cd ..                 
```

Add a line to the `.gitignore` file to exclude your binary.

```
$ echo exerciseNN/XXX >> .gitignore
```

Add the new directory (and file) to your staged commit and verify your files 
are staged.

```
$ git add exerciseNN
$ git status
```

Commit your code and push it to GitHub!

```
$ git commit -m "<your commit message>"
$ git push -u origin <your-branch>
```

There will be a link to create a pull request in the upload message. Click the
link and create a PR. Add one of the TAs as a reviewer!
