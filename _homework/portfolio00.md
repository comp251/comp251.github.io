---
layout: default
title: "Kata 0 (Due 2/8)"
nav_order: 4
---

# Programming Kata 0

Welcome to your first programming exercise for your portfolio!

{: .warning }
If you have not already done so, follow the instructions in the [portfolio
intro](/homework/portfolio_intro). You **must** do this before starting this
assignment!

If you have not done so yet already, clone your portfolio on lily. 

```
$ git clone <your-portfolio-url>
```

Change your working directory to inside the portfolio and create a new branch
for this assignment.

```
$ cd <your-portfolio-directory>
$ git checkout -b exercise00
```

Validate that you are indeed **using a branch** (the output should start with
"On branch exercise00"):

```
$ git status
```

{: .warning }
You __must__ work within branches! Do not commit code to the `main` branch -- if
you do this, you will be penalized points. We are trying to model best practices
in this class and develop some process skills that you will use in __all__
future classes.

Now, create a subdirectory for this exercise and change your working directory
to inside it.

```
$ mkdir exercise00
$ cd exercise00
```

Now create your C file and start coding!

```
$ vim collatz.c
```

# Assignment

Write a program that computes the total number of iterations for (user-inputted)
numbers to complete their [Collatz
sequences](https://en.wikipedia.org/wiki/Collatz_conjecture).

{: .note }
The Collatz sequence for a number is the sequence of numbers that are output
when following the following algorithm for a given input `n` (`n` must be
greater than 1):<br/><br/>"as long as `n` is not 1: if `n` is even, `n` becomes `n/2`;
otherwise, `n` becomes `3n+1`."<br/><br/>For example, consider a starting value of
10: 10 is even, so the next number is 5. 5 is odd, so the next number is 16
(`3*5+1`). 16 is even, so the next number is 8 (then 4, then 2, then
1).<br/><br/>The
total length of this sequence (10, 5, 16, 8, 4, 2, 1) is 7.

You can have a termination condition that validates that the number is greater
than 0, or you can just use CTRL-C to quit.

```
$ gcc collatz.c -o collatz
$ ./collatz
Enter a number: 12
12 -> 10
Enter a number: 19
19 -> 21
Enter a number: 2
2 -> 2
Enter a number: 6
6 -> 9
Enter a number: 7
7 -> 17
Enter a number: 26
26 -> 11
Enter a number: 27
27 -> 112
Enter a number: ^C
$
``` 

## Tips

* You should write a function to compute the number of iterations for a given
  number.
* Use `scanf` and `printf` to perform input and output.
* You should add input validation; quitting when the number is not greater than
  or equal to 1 is a fine behavior.

# Turning it in

When you are complete, commit your code and create a pull request with your
exercise. 

Change to the root directory of your repository:

```
$ cd ..                 
```

Add a line to the `.gitignore` file to exclude your binary.

```
$ echo exercise00/collatz >> .gitignore
```

Add the new directory (and file) to your staged commit and verify your files 
are staged.

```
$ git add exercise00   
$ git add exercise00/collatz.c
$ git status
```

Commit your code and push it to GitHub!

```
$ git commit -m "<your commit message>"
$ git push -u origin exercise00
```

There will be a link to create a pull request in the upload message. Click the
link and create a PR. Assign me as reviewer.
