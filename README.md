<a name="toc"></a>
<!--ts-->
* [Introduction](#introduction)
* [Logging in](#logging-in)
   * [Off-campus access](#off-campus-access)
* [Getting started](#getting-started)
* [Working with branches](#working-with-branches)
* [Editing your program](#editing-your-program)
* [Compiling and running your program](#compiling-and-running-your-program)
* [Committing your code and pushing your commits](#committing-your-code-and-pushing-your-commits)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: langm, at: Fri Dec 16 19:41:33 UTC 2022 -->

<!--te-->

# Introduction

We will be using a command line shell interface for development in this course.
We will also be using version control tools (git) to track changes in our work
as well as to "release" code (to turn it in).

After this lab, you should:
* be able to ssh into a remote server.
* clone a git repository from GitHub and manage it using the git command-line
  interface.
* edit files using a text mode editor.
* compile a program using a command-line C compiler.
* use common commands like `cd`, `pwd`, `ls`, `less`, and `cat` as well as run
  user-compiled programs.

🔝 [back to top](#toc)

# Logging in

Both MacOS and Windows computers come with an ssh client installed. Depending on
your system, use `ssh <username>@lily.rhodes.edu` to ssh into the server where
you'll be doing your work. You should have received an email or slack message
from me containing your initial password.

When you first log in, run the following command to change your password (note
that the `$` indicates the command prompt and that you don't need to actually
type it):

```
$ passwd
Changing password for ...
```

Once you've logged in, you can view the files and folders in your home directory
by using the `ls` command (think "list"):

```
$ ls
```

The `ls` command, like many other commands and programs, accepts program
arguments via flags and options.

For example, `ls -a` supplies the `-a` argument to the program, which indicates
that it should list _all_ files. In Unix-like systems (like Linux), some files
(those starting with a period--called dot-files) are hidden.

Try a few arguments:
```
$ ls -l
$ ls -a -l
$ ls .vim
```

What do you think the last one did? Before continuing, make a note answering the
question (question 1).

Try running the following to see if you were right:

```
$ pwd
$ cd .vim
$ pwd
$ ls
$ cd ..
$ pwd
```

`cd` is the change directory command. `..` is a special shortcut that refers to
the directory above the current one. What do you think `pwd` stands for? Make a
note of your answer (question 2).

## Off-campus access

Follow [the instructions](https://tinyr.us/rhodes-vpn) provided by ITS to get
access to VPN.  After connecting to the Rhodes VPN, you can use `ssh` like
normal.

🔝 [back to top](#toc)

# Getting started

First, clone this repository to your account.

```
$ cd
$ pwd # note what running cd with no arguments does...
$ git clone <your URL>
```

You can verify that the repository has been cloned by looking at the project's
files.

```
$ cd <your project directory>
$ ls
```

You should see this file (`README.md`) and a C source file (`hello.c`). 

🔝 [back to top](#toc)

# Working with branches

Before we edit anything, we'll first create a __branch__ of our source code.
This allows us to work on our code and make changes without affecting the
original files in the main branch. If we were working on a team, this would
allows us to work on the same sets of files at the same time. It would also
allow us to make a bunch of incremental changes that are part of one single
feature, or keep track of different features without intermingling our code
changes.


In this class, we'll mostly be using one branch at a time. Using branches with
git is good practice (for the reasons listed above--and more).

To create a new branch, run the following command (from within your project
directory!).

```
$ git checkout -b namefix
$ git status
```

The `-b` option tells git to create the branch.

If you want to check out the main branch again, run:

```
$ git checkout main
$ git status
```

Before you continue, make sure that you are using the `namefix` branch: `git
checkout namefix`.

🔝 [back to top](#toc)

# Editing your program

Now that we're working on our new branch (confirm this using `git status`), we
can start editing files. I recommend using `vim`, which I have preconfigured
have many features that you are probably used to in an IDE. `vim` is a __very__
powerful tool and infinitely configurable.

At its base, Vim is a text editor: a program designed for editing text files.
However, it has a robust plugin and scripting capabilities that enable to it to
almost anything. Yours has been configured with syntax highlighting, semantic
completion, and code analysis that runs while you're editing.

Vim is very different from other text editing programs that you may have used
before. It has different modes. The two major modes are _insert_ and _normal_.
Insert mode is editing mode: things that you type affect the contents of the
text file. Normal mode is navigation mode: things that you type move you around
the file.

Vim starts in normal (navigation) mode. You can enter editing mode by typing the
command to enter insert mode `i`. Now you can edit normally. When you are done,
you can go back to normal mode by hitting the escape key. 

A third mode is the command mode. This allows you to enter commands to the
editor. Two important ones are writing the file (saving) and quitting the editor.

To enter command mode, make sure you are in normal mode and then type `:`. This
brings up the Vim command prompt. Type `w` to save (write), or `q` to quit. To
quit without saving changes, use `q!`.

Before getting continuing, run `vimtutor` for the built-in introduction to Vim's
commands. [This](https://devhints.io/vim) is a decent cheat sheet.
[This](https://vim.rtorr.com/) is a more detailed cheat sheet, but may be too
complex at first. [Vim Adventures](https://vim-adventures.com) is a cute game
that demonstrates and practices commands through playing a game (though it is
unfortunately not free for the full experience).

Now that you've walked through Vim a little bit, let's edit our source file.

```
$ vim hello.c
```

First, take a minute to read through the file. Make note of things that look
like variables, expressions, code blocks, etc.

Then, change my name to yours.

When you're done, answer the following questions:

1. Question 1 for above (skip this until you get to instructions after question 8).

2. Question 2 from above (skip this until you get to instructions after question 8).

3. List any elements that look familiar to you.

4. What do you think the `//` characters mean?

5. What do you think the `{` and `}` braces mean?

6. What functions does the program have?

7. What do you think the program does? Don't worry about what it means to
   "compute MD5" -- just know that it is an operation that turns a string of
   any length into a deterministic 16 byte value.

8. Pick out some lines or fragments of code that you think are similar to 
   constructs in other languages you know (Java or Python). Describe at least
   three.

After you're done making your changes and exploring the file, close the file and
open this one to add your answers! `vim README.md` will open the file. As you
can see, the file is formatted using a markup language called markdown. Here's a
[cheat
sheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
for GitHub-specific markdown.  Format your answers as block quotes under the
questions. 

If you want to read about what MD5 actually is, skim the [Wikipedia
page](https://en.wikipedia.org/wiki/MD5).

🔝 [back to top](#toc)

# Compiling and running your program

Cool! Now lets compile and run our first program! We'll use the GCC C compiler
to compile:

```
$ gcc hello.c -lssl -lcrypto -o my_hello
```

Here, this command runs the compiler with the input file `hello.c` and links in
the `ssl` and `crypto` libraries (for MD5). The compiled output program will be
named `my_hello`. If the program compiles successfully, you should see the
output program when you list the directory:

```
$ ls
```

Now, run your program! Was your guess from question 7 correct?

```
$ ./my_hello
```

To view a file's contents, you can use the `less` command to view it, and use
the up/down arrow/page keys to move through it. Hit `q` to quit.

```
$ less hello.c
```

For short files (like our program's output), it may be more efficient to just
output their contents. The `cat` command does this.

```
$ cat output.txt
```

C is a fundamental part of most Unix-like systems. Unix-like systems have
built-in manuals, and the manuals includes documentation on the C library. Run
the following to open the `malloc` entry in the manual:

```
$ man 3 malloc
```

The manual page will open in `less`. Use the arrow keys to navigate and `q` to
quit. Use the manual to answer the following:

9. One difference between C and other languages you have used is that C requires
   you to explicitly manage dynamically-allocated memory. What do you think line
   9 of `hello.c` is doing?

10. What do you think line 35 is doing?

11. Try moving line 35 to above line 25. What do you think will happen when you
    compile and run the program again? 

12. Compile and run the program. Try moving it different places and see if there
    is any different behavior. What happened? Why do you think this happened?

13. Try adding `free(name);` somewhere. What do you think will happen? What
    happened?

We will talk a lot more about memory management in the coming weeks.

🔝 [back to top](#toc)

# Committing your code and pushing your commits

First, undo the changes that you made above in steps 11--13. Compile and run
your program again.

Now that we've finished editing, it's time to commit our changes and push our
feature! 

Use `git status` to see what has changed in the current branch. Use `git add <filename>`
to add a file to be staged for commit. 

```
$ git status
$ git add hello.c
$ git add output.txt
$ git status
```

Finally, use `git commit` to commit your change, alongside a description of the
changes that you made.

```
$ git commit -m 'fix name, add output file'
```

You can commit as many changes as you want within a branch. Commits are
typically self-contained, small, incremental changes that build up to a big
change (e.g., implementing a feature). When it's time to merge that feature into
the main code base, we create a pull request on GitHub. To do so, run the
following to push your branch to GitHub.

```
$ git push
```

__It will error the first time you do this and tell you what you need to do to
fix it.__ Run the command that git specifies to set the remote repository.

Once you've set the upstream for the branch, you can continue to commit and
push as much as you'd like. Keeping GitHub in sync with your changes on your
computer by pushing your commits has a great side effect of backing up your
work!

Before you continue on, make sure that you have edited this file and updated it
with your answers. __Make sure you commit your changes to this file and push
them as well.__

Note that in the output of the first successful push there was a link to create
a pull request. You can also do this from your repository's web UI.

Pull requests are ways for your code to be reviewed by a peer (or, in this case,
by me) before it is made final by merging it into the main branch. Follow the
URL to create a pull request. When you want to submit this, create a pull
request for me to review. In the GitHub UI, set me (`@ml8`) as a reviewer.
Do not merge the pull request! This is how I will grade your work.

Later, __after__ I have graded your lab, you can merge the pull request. Come
back to your repository, and update your local with the changes made to your
main branch!

```
$ git checkout main
$ git pull
```

🔝 [back to top](#toc)

