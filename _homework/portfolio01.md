---
layout: default
title: "Programming Portfolio (kata 1)"
nav_order: 4
nav_exclude: true
---

# Programming Kata 1

If you have not done so yet already, clone your portfolio on lily. 

```
$ git clone <your-portfolio-url>
```

Change your working directory to inside the portfolio and create a new branch
for this assignment.

```
$ cd <your-portfolio-directory>
$ git checkout -b <your-branch-name>
```

{: .warning }
You __must__ work within branches! Do not commit code to the `main` branch -- if
you do this, you will be penalized points. We are trying to model best practices
in this class and develop some process skills that you will use in __all__
future classes.

Now, create a subdirectory for this exercise and change your working directory
to inside it.

```
$ mkdir exercise01
$ cd exercise01
```

Now create your C file and start coding!

```
$ vim read_and_reverse.c
```

# Assignment

Write a program that repeatedly reads stings from standard input and then uses a
function to reverse a string. You can have a termination condition and check it
using `strcmp`, or you can just use CTRL-C to quit.

```
$ gcc read_and_reverse.c -o read_and_reverse
$ ./read_and_reverse
Enter a word (ctrl-C to quit): hello
hello -> olleh
Enter a word (ctrl-C to quit): world
world -> dlrow
Enter a word (ctrl-C to quit): racecar
racecar -> racecar
Enter a word (ctrl-C to quit): mom
mom -> mom
Enter a word (ctrl-C to quit): wow
wow -> wow
Enter a word (ctrl-C to quit): COMP251
COMP251 -> 152PMOC
Enter a word (ctrl-C to quit): ^C
$
```

## Tips

* You can assume that the string that the user enters is less than 50
  characters.
* Use `strlen` to determine the length of the word the user input (you will need
  to `#include <string.h>`.
* In a shell, type `$ man strlen` for info about the function.

# Turning it in

When you are complete, commit your code and create a pull request with your
exercise. 

Change to the root directory of your repository:

```
$ cd ..                 
```

Add a line to the `.gitignore` file to exclude your binary.

```
$ echo exercise01/read_and_reverse >> .gitignore
```

Add the new directory (and file) to your staged commit and verify your files 
are staged.

```
$ git add exercise01   
$ git status
```

Commit your code and push it to GitHub!

```
$ git commit -m "<your commit message>"
$ git push -u origin <your-branch>
```

There will be a link to create a pull request in the upload message. Click the
link and create a PR. Add one of the TAs as a reviewer!
