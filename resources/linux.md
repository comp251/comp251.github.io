---
layout: default
title: Linux Shell
parent: Course Resources
description: Linux Shell
nav_order: 4
---

# {{ page.description }}
{: no_toc }

{: .note }
This page summarizes some basic command shell usage. It is not a substitute
for [The Linux Command Line](/resources/books) book, though! Skimming chapters 1-4 in that
book will give a good overview of using the command line.

1. TOC
{:toc}

# What is a shell?

A _shell_ or _command shell_ is a program that allows you to run other programs.
The Windows/OSX GUI is a visual shell; we will be using a text-based shell. When
you log into lily via ssh, a shell is started for you and it is what you will
interact with.

A shell runs in a _REPL_ (read, execute, print, loop) mode, where it prompts you
to enter a command and waits for your input (_read_), executes the command
(_execute_), shows you the output of the command (_print_), and repeats these
operations (_loop_).

Each of the commands that you enter will be a program to run and a list of
arguments for the program. The program name goes first and arguments follow.

The following is a list of commands/programs, grouped by their use. The
convention used is that `$` is the shell's input prompt. The output of the
command is shown on the next line. Comments are prefixed with `#` and are asides
to you, the reader.

<div class="code-example" markdown="1">
## Your first commands

First, log in to lily by using SSH. You'll see a prompt that looks something
like this:

```shell-session
langm@lily:~$
```

This is the input _prompt_.  Try typing a few commands. Here's a few useful
samples including some that retrieve some system information.

When you're ready to log out, run the `exit` command. 
</div>
```shell-session
$ date
$ cal
$ uptime
$ uname -a
$ lscpu
$ passwd 
$ exit
```


# File organization

The files on a computer are stored in _directories_ (aka folders). Directories
can contain other directories (folders within folders) as well as files.
Directories are organized in a tree-like structure, where there is a
distinguished _root directory_ at the top level.

A directory is uniquely identified by its _path_ from the root. 

The root directory is named `/`. If it contains a directory named `home`, the path
of `home` is `/home`. My home directory's path is `/home/langm`, and it may contain
other directories (e.g., `/home/langm/Documents`,
`/home/langm/Pictures/my_summer_vacation`, etc.). Here's a visual example.

![Filesystem Screenshot](/assets/filesystem_screenshot.png)

A shell always has a _working directory_ that is the directory that the shell is
currently working within. If a path for a file/directory is given that does not
start with `/`, it is assumed to be a _relative path_ and is assumed to start
with the working directory's path.

{: .warning }
{: id="fs-warning" }
One thing that you will notice is that it is awkward to deal with files that have special characters or spaces, since the shell interprets a space as separating arguments!
<br><br>
If you need to work with files with spaces or special characters, use `\` to "escape" the special character/space.

# General tips

* The shell provides both command and file completion. When you type the start
  of some command or file, use the tab key to have the shell attempt to complete
  it. If there are multiple options, hit tab twice quickly to see them all.
* There are some special signals that you can send to programs using the control
  key: 

  * `ctrl-c` will attempt to kill the currently-running program
  * `ctrl-d` will send the end-of-file character to the currently-running
    program
  * `ctrl-z` will send the running program to the background and pause it. Use
    `jobs` to list background programs, `fg` to resume the program in the
    foreground, and `bg` to resume the program in the background.


# Command list

The following is a sample of some useful shell commands to get you started. I
highly recommend reading the [Linux Command Line book](/resources/books)!

<div class="code-example" markdown="1">
## Navigating directories

The `pwd` ("print working directory") command prints the name of the
directory/folder that your shell is working within. This directory can be
changed using the `cd` command.
</div>
```shell-session
$ pwd
/home/langm
$ cd /home
$ pwd
/home
$ cd langm      # note this is a relative path -- a name that does start with /
$ pwd
/home/langm
$ cd ~          # ~ is a special alias for your home directory
$ cd ..         # .. is a special alias for the directory "above" the current
$ cd -          # - is a special alias for the last directory
```

---

<div class="code-example" markdown="1">
## Viewing directories

The `ls` command (read as "list") lists the files in a directory. By default, it
lists files in the _current directory_ (see `pwd`). If you want to see files in
another directory, you can give that as an argument.

`ls` also accepts _flags_. These are arguments that change the behavior of the
program, or are modifiers to other arguments. Flags usually start with a `-` and
can be combined together.
</div>
```shell-session
$ ls
birthdays.txt  Desktop  Documents  Downloads  large_file.txt  Pictures
$ ls -l            # the -l flag lists the files in "long" format
total 102424
-rw-rw-r-- 1 langm langm        31 Jan 21 21:15 birthdays.txt
drwxr-xr-x 2 langm langm      4096 Jan 21 21:05 Desktop
drwxr-xr-x 2 langm langm      4096 Jan 21 21:05 Documents
drwxr-xr-x 2 langm langm      4096 Jan 21 21:05 Downloads
-rw-rw-r-- 1 langm langm 104857600 Jan 21 21:11 large_file.txt
drwxr-xr-x 3 langm langm      4096 Jan 21 21:09 Pictures
$ ls -l -h         # use human-readable sizes
total 101M
-rw-rw-r-- 1 langm langm   31 Jan 21 21:15 birthdays.txt
drwxr-xr-x 2 langm langm 4.0K Jan 21 21:05 Desktop
drwxr-xr-x 2 langm langm 4.0K Jan 21 21:05 Documents
drwxr-xr-x 2 langm langm 4.0K Jan 21 21:05 Downloads
-rw-rw-r-- 1 langm langm 100M Jan 21 21:11 large_file.txt
drwxr-xr-x 3 langm langm 4.0K Jan 21 21:09 Pictures
$ ls Documents     # list a specific directory (relative path)
cat_stories  cowboy_names.txt  resume.tex
$ ls /home         # list a specific directory (absolute path)
brian elise langm
$ tree             # view current and sub-directories in a tree format
.
|-- birthdays.txt
|-- Desktop
|-- Documents
|   |-- cat_stories
|   |-- cowboy_names.txt
|   `-- resume.tex
|-- Downloads
|-- large_file.txt
`-- Pictures
    `-- my_summer_vacation

22 directories, 4 files
```

---

<div class="code-example" markdown="1">
## Making and removing directories

`mkdir` creates a directory and `rmdir` deletes a directory.
</div>
```shell-session
$ ls
birthdays.txt  Desktop  Documents  Downloads  large_file.txt  Pictures
$ mkdir foo
$ ls
birthdays.txt  Desktop  Documents  Downloads  foo  large_file.txt  Pictures
$ rmdir foo
$ ls
birthdays.txt  Desktop  Documents  Downloads  large_file.txt  Pictures
```

---

<div class="code-example" markdown="1">
## Viewing files

* `cat` outputs a file's contents. 
* `less` can be used to view large files. 
* We'll use `vim` for editing files. 
* `tail` and `head` view the beginning and end of files, respectively.
</div>
```shell-session
$ ls
birthdays.txt  Desktop  Documents  Downloads  large_file.txt  Pictures
$ cat birthdays.txt
elise 9/5
marion 7/8
zelda 5/1
$ less large_file.txt           # use q to quit
$ vim file_to_edit.txt          # read section on vim!
$ cd Documents
$ ls
cat_stories     cowboy_names.txt     resume.tex
$ head cowboy_names.txt         # first 10 lines
Slim
Pete
Buck
Clint
Colt
Duke
Hank
Cody
Beau
Dan
$ head -n 15 cowboy_names.txt   # first 15 lines
Slim
Pete
Buck
Clint
Colt
Duke
Hank
Cody
Beau
Dan
Boone
Jasper
Harvey
Billy
Bart
$ tail -n 6 cowboy_names.txt    # last 6 lines
Shiloh
Mac
Rex
Orville
Owen
Hogan
```

---

<div class="code-example" markdown="1">
## Copying and moving files/directories

There are two main commands for moving and copying files and directories: `mv` (move) and `cp` (copy).

> See [warning above](#fs-warning) regarding files with spaces/special characters.

</div>
```shell-session
$ pwd
/home/langm/Downloads
$ ls
Limewire (1).zip                mr brightside.flac              rats - nonverbal.xls
best-friends.xls                naruto_ska_cover.mp3            small_horse_(not_too_small).jpg
$ mv Limewire\ \(1\).zip limewire.zip
$ ls
best-friends.xls                mr brightside.flac              rats - nonverbal.xls
limewire.zip                    naruto_ska_cover.mp3            small_horse_(not_too_small).jpg
$ cp best-friends.xls potential-enemies.xls
$ ls
best-friends.xls                mr brightside.flac              potential-enemies.xls           small_horse_(not_too_small).jpg
limewire.zip                    naruto_ska_cover.mp3            rats - nonverbal.xls
$ mkdir new_music
$ mv naruto_ska_cover.mp3 new_music/naruto_ska_cover.mp3
$ mv mr\ brightside.flac new_music/mr_brightside.flac
$ ls
best-friends.xls                new_music                       rats - nonverbal.xls
limewire.zip                    potential-enemies.xls           small_horse_(not_too_small).jpg
$ ls new_music
mr_brightside.flac   naruto_ska_cover.mp3
$ mv new_music cool_tunes
$ ls
best-friends.xls                limewire.zip                    rats - nonverbal.xls
cool_tunes                      potential-enemies.xls           small_horse_(not_too_small).jpg
```
---

<div class="code-example" markdown="1">
## User/session management

You will probably only use two commands to manage your user: `passwd` and `exit`.

It is convenient to use tmux to have long-lived sessions, but not necessary for the course. See section on [tmux](/resources/vim#tmux).
</div>
```shell-session
$ passwd                       # change your password
Changing password for langm.
Current password: 
New password: 
Retype new password: 
passwd: password updated successfully
$ exit                         # log out
$ tmux ls                      # list tmux sessions (see tmux section)
$ tmux new -s 251              # new tmux session (see tmux section)
$ tmx 251                      # same as above -- tmx shortcut
$ tmux attach-session -t 251   # attach to tmux session (see tmux section)
$ tmx 251                      # same as above -- tmx shortcut
```

---

<div class="code-example" markdown="1">
## Compiling and debugging code

We will use the GNU C Compiler (`gcc`) for compiling code. 
</div>
```shell-session
$ ls              
Makefile   my_program.c
$ gcc my_program.c              # compile program
$ ls
Makefile   a.out   my_program.c
$ ./a.out                       # run program
$ gcc my_program -o my_prog     # compile without output binary name my_prog
$ ls
Makefile   my_prog   my_program.c
$ ./my_prog                     # run program
$ make                          # use make with default target
$ make target_name              # use make with a named target
```

---

<div class="code-example" markdown="1">
## Pipes and redirection

One useful feature of Linux systems is the ability to redirect a program's
output to another program's input. This allows one to chain simple commands
together to form a complex processing pipeline. The IO _pipe_ is used to send
the output of one program to the input of another. The syntax for a pipe is
`command1 | command2`; this sends the output of `command1` to the input of
`command2`.

Here are some simple tools that are part of all Linux systems. You've already
seen the first few:

* `cat` -- output a file or set of files
* `head`/`tail` -- output the beginning or end of files
* `grep` -- search through input for lines matching some pattern
* `sort` -- sort input
* `cut` -- extract fields from input
* `wc` -- count lines from input

This list isn't complete: __all commands__ that use standard input/output can be
chained together in this way.
</div>
```
$ cat cowboy_names.txt | grep ^B       # find all cowboy names that start with B
Buck
Beau
Boone
Billy
Bart
$ sort cowboy_names.txt | tail -n 1    # find the last name in alphabetical order
Zeke
$ ls /usr/bin | grep python            # find all python binaries in /usr/bin
python
python2
python2.7
python2.7-config
python2-config
python3
python3.6
python3.6-config
python3.6m
python3.6m-config
python3.7
python3.7m
python3.8
python3.8-config
python3-config
$ cat /etc/passwd | cut -f 1 -d ':'  | grep m$  # find all users whose name ends in m
langm
$ cat /etc/passwd | wc -l             # count users in the system
35
$ cat /etc/passwd | cut -f 1 -d ':' | grep m$ | wc -l  # how many users end with m?
1
```

---

<div class="code-example" markdown="1">
## Getting help

Linux systems ship with a _manual_ that contains a page for each command on the
system. When you want help with a command, look it up via its _man page_ (manual
page).

The manual is also divided into sections:

section | topics
---|---
1 | User commands
2 | OS System calls and functions
3 | Library functions
4 | Special files
5 | File formats and conventions
6 | Games
7 | Misc
8 | System administration commands

To narrow down an ambiguous page to a specific section, use the section number
(see below).

It is always helpful to read the manual page for a C function when you use it.
</div>
```
$ man ls              # get help with ls
$ man cat             # get help with cat
$ man printf          # get help with the program printf (section 1)
$ man 3 printf        # get help with the C library function printf (section 3)
$ man -f printf       # find printf pages in the manual
printf (1)           - format and print data
printf (3)           - formatted output conversion
$ man -k printf       # find pages matching printf in the manual
asprintf (3)         - print to allocated string
dprintf (3)          - formatted output conversion
fprintf (3)          - formatted output conversion
fwprintf (3)         - formatted wide-character output conversion
printf (1)           - format and print data
printf (3)           - formatted output conversion
snprintf (3)         - formatted output conversion
sprintf (3)          - formatted output conversion
swprintf (3)         - formatted wide-character output conversion
vasprintf (3)        - print to allocated string
vdprintf (3)         - formatted output conversion
vfprintf (3)         - formatted output conversion
vfwprintf (3)        - formatted wide-character output conversion
vprintf (3)          - formatted output conversion
vsnprintf (3)        - formatted output conversion
vsprintf (3)         - formatted output conversion
vswprintf (3)        - formatted wide-character output conversion
vwprintf (3)         - formatted wide-character output conversion
wprintf (3)          - formatted wide-character output conversion
XtAsprintf (3)       - memory management functions
$ man 3 strcat        # look up the strcat function in the C libraries
```

