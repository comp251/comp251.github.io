---
layout: default
title: "Programming Portfolio (kata 3)"
nav_order: 6
nav_exclude: true
---

# Programming Kata 3

Change your working directory to your portfolio and __create a new branch
for this assignment__.

```
$ cd <your-portfolio-directory>
$ git checkout -b <your-branch-name>
```

Now, create a subdirectory for this exercise and change your working directory
to inside it.

```
$ mkdir exercise03
$ cd exercise03
```

Now create your C file and start coding!

```
$ vim 7seg.c
```

# Assignment

Write a program that repeatedly reads integers from standard input and displays
them as digits in a 7 segment display (pretend that the following is not
double-spaced 😒).

```
$ gcc 7seg.c -o 7seg
$ ./7seg
Enter a number: 1234567890
     _   _       _   _   _   _   _   _
  |  _|  _| |_| |_  |_    | |_| |_| | |
  | |_   _|   |  _| |_|   | |_|   | |_|

Enter a number: 222222
 _   _   _   _   _   _
 _|  _|  _|  _|  _|  _|
|_  |_  |_  |_  |_  |_

Enter a number: 781981
 _   _       _   _
  | |_|   | |_| |_|   |
  | |_|   |   | |_|   |

Enter a number: ^C
```

## Tips

* Declaring a multidimensional array of 3-character long (4, with null
  terminator) strings representing the digits is an easy approach to this
  problem.

  For example, the following declares a 2-d array where each element in a
  string:

  ```
  char dims[2][4][5] = { { "abcd", "efgh", "ijkl", "mnop" },
                         { "qrst", "uvwx", "yz12", "3456" } };
  ```

  This results in a 2-D array with 2 rows, 4 columns, and each element is 5
  characters (so it can include a 4 char string with a null-terminator).

  | `abcd` | `efgh` | `ijkl` | `mnop` |
  | `qrst` | `uvwx` | `yz12` | `3456` |

* Note that `int` type will be less than 10 digits; if you use an array to store
  the digits of the number that was entered, you can assume that 10 digits is
  enough.



# Turning it in

When you are complete, commit your code and create a pull request with your
exercise. 

Change to the root directory of your repository:

```
$ cd ..                 
```

Add a line to the `.gitignore` file to exclude your binary.

```
$ echo exercise03/7seg >> .gitignore
```

Add the new directory (and file) to your staged commit and verify your files 
are staged.

```
$ git add exercise03
$ git status
```

Commit your code and push it to GitHub!

```
$ git commit -m "<your commit message>"
$ git push -u origin <your-branch>
```

There will be a link to create a pull request in the upload message. Click the
link and create a PR. Add one of the TAs as a reviewer!
