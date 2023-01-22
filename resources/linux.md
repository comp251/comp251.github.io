---
layout: default
title: Linux shell and tools
parent: Course Resources
description: Bash, Vim, Tmux, and Linux Tips
nav_order: 3
---

# {{ page.description }}
{: .no_toc }

1. TOC
{:toc}

# SSH and remote access

You'll be using SSH to log in to lily/iris to do your work in this class.
SSH (Secure SHell) is a way to open a shell/terminal on a remote computer.
This allows you to interact with the remote computer and run programs, edit
files, write code, etc. SSH is a _secure_ shell because it uses an encrypted
channel for communication between your local computer and the remote computer.

The program `ssh` is used to connect to a remote machine. Use `ssh username@host` to
connect to the computer named `host` (e.g., `lily.rhodes.edu`) with the given
username (e.g., `langm`). For example, my account on `lily` is named `langm`. To
connect, I run `ssh langm@lily.rhodes.edu`.

## Access from off-campus

Within the first week, you should have access to the Rhodes VPN. Follow the
instructions on the [software resources page](/resources/software) to install the
FortiClient software.

---

# Shell cheat sheet and basic commands

{: .note }
This section summarizes some basic command shell usage. It is not a substitute
for [The Linux Command Line](/resources/books) book, though! Skimming chapters 1-4 in that
book will give a good overview of using the command line.

## What is a shell?

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
### First commands

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


## File organization

The files on a computer are stored in _directories_ (aka folders). Directories
can contain other directories (folders within folders) as well as files.
Directories are organized in a tree-like structure, where there is a
distinguished _root directory_ at the top level.

A directory is uniquely identified by its _path_ from the root. 

The root directory is named `/`. If it contains a directory named `home`, the path
of `home` is `/home`. My home directory's path is `/home/langm`, and it may contain
other directories (e.g., `/home/langm/Documents`,
`/home/langm/Pictures/my_summer_vacation`, etc.).

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


## Command list

<div class="code-example" markdown="1">
### Navigating directories

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

<div class="code-example" markdown="1">
### Viewing directories

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

<div class="code-example" markdown="1">
### Making and removing directories

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

<div class="code-example" markdown="1">
### Viewing files

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
$ vim file_to_edit.txt          # read section on vim below!
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

<div class="code-example" markdown="1">
### Copying and moving files/directories

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
$ mkdir cool_tunes
$ mv naruto_ska_cover.mp3 cool_tunes/naruto_ska_cover.mp3
$ mv mr\ brightside.flac cool_tunes/mr_brightside.flac
$ ls
best-friends.xls                limewire.zip                    rats - nonverbal.xls
cool_tunes                      potential-enemies.xls           small_horse_(not_too_small).jpg
$ ls cool_tunes
mr_brightside.flac   naruto_ska_cover.mp3
$ mv cool_tunes new_music
$ ls
best-friends.xls                new_music                       rats - nonverbal.xls
limewire.zip                    potential-enemies.xls           small_horse_(not_too_small).jpg
```

<div class="code-example" markdown="1">
### User/session management

You will probably only use two commands to manage your user: `passwd` and `exit`.

It is convenient to use tmux to have long-lived sessions, but not necessary for the course. See section on [tmux](#tmux) below.
</div>
```shell-session
$ passwd                       # change your password
Changing password for langm.
Current password: 
New password: 
Retype new password: 
passwd: password updated successfully
$ exit                         # log out
$ tmux ls                      # list tmux sessions (see below)
$ tmux new -s 251              # new tmux session (see below)
$ tmx 251                      # same as above -- tmx shortcut
$ tmux attach-session -t 251   # attach to tmux session (see below)
$ tmx 251                      # same as above -- tmx shortcut
```

<div class="code-example" markdown="1">
### Compiling and debugging code

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

# `git` and GitHub

Make sure that you [sign up](https://github.com/signup) for a GitHub account and
activate your [benefits for
students](https://education.github.com/discount_requests/pack_application).

You'll be writing Markdown files for lab writeups. GitHub has provided a nice
[cheat
sheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
for formatting a document using Markdown.

## Setting up `git`

When you log in to lily, you should configure git with your identity:

```
$ git config --global user.name "Marion Lang"
$ git config --global user.email "langm@rhodes.edu"
```

{: .important}
As of late 2021, GitHub disabled using your password for
accessing repositories and instead recommends using tokens when using HTTPS or
ssh keys when using ssh. __We will use ssh.__

* To set this up, follow the general directions
  [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
  and
  [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

* Speficially, for our environment:

  1. Log into lily.
  2. Use the email you used to sign up for GitHub in the following: 

     ```
     $ ssh-keygen -t ed25519 -C "your_email@example.com"
     ```

  3. When it prompts you for file name, just hit enter.
  4. When it prompts for a passphrase, hit enter for none.
  5. `$ exec ssh-agent bash`
  6. `$ ssh-add ~/.ssh/id_ed25519`
  7. `$ cat ~/.ssh/id_ed25519.pub`
  8. Copy the output of the last command.
  9. Go to
     [github.com/settings/keys](https://github.com/settings/keys).
  10. Click "New SSH key."
  11. Give it a name (e.g., "lily").
  12. Paste the output from the `cat` command into the "key" box.
  13. Click "Add SSH key."

---

# Vim

{: .warning }
You will probably hate using Vim at first.

Using a command-line text editor is a vital process skill and Vim is both
ubiquitous and well-supported, with a rich collection of plugins that can make
your life easier. 

There are several tutorials and cheet sheets online. One is even built into Vim
itself!

* Run `vimtutor` for an interactive tutorial inside of Vim.
* [This](https://devhints.io/vim) is a decent basics cheat sheet.
* [This](https://vim.rtorr.com/) is a more detailed cheat sheet.
* [Vim Adventures](https://vim-adventures.com) is a cute game that helps you
  learn the basic movement commands (these will come in useful!). The full game
  is not free, but the free preview has good coverage of basic movement.

This [parody](https://youtu.be/9n1dtmzqnCU) of Vim users is spot-on.

---

# tmux

ssh attempts to make connections persistent. However, like any other application
running on the network, you will drop an ssh connection when you disconnect from
the internet. This can be frustrating when you're in the middle of working!

One way to prevent this frustration is to create a persistent terminal session
on the remote machine--think of this like a set of windows that you can
disconnect from and reconnect to.  tmux is a program that allows you to do
this.

I highly recommend that you invest a little time in learning how to use tmux to
have multiple windows open in one ssh window __and to be able to quit and
reconnect to an existing session__. Here’s a couple of tutorials:

* [How to use
  tmux on Linux](https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/)
* [Getting Started with Tmux](https://linuxhandbook.com/tmux/)
* [How to Use Tmux + Cheat
  Sheet](https://www.hostinger.com/tutorials/tmux-beginners-guide-and-cheat-sheet/)

Note that these tutorials may ask you install software. You can't install
software on Lily--you don't have the proper permissions. But, you shouldn't need
to; I have installed all the software necessary for success in this class.

---

# Transferring files with SCP

If you want to transfer files back and forth between a remote computer, you can
use the program SCP (Secure CoPy). This is a SSH version of the `cp` command.

Recall that using `cp` copies a _source_ file/directory to a _dest_
file/directory:

```
$ cp source dest
```

`scp` is similar, except it allows you to specify a different
host machine before the source or dest:

```
# copy remote to local
$ scp user@host:/path/to/souce dest
# copy local to remote
$ scp source user@host:/path/to/dest
```

Practically, if I want to copy a file from my laptop to my home directory on
`iris`, this would look like the following:

```
$ scp my_prog.c langm@iris.rhodes.edu:./my_prog.c
```

If I wanted to copy a directory name `notes/` from my home directory on `iris`
to my local computer, it would look like this (note the `-r` flag for
_recursive_ copy of a directory):

```
$ scp -r langm@iris.rhodes.edu:./notes ./notes
```

{: .note }
You can use a graphical program if you prefer. The [recommended
software](/resources/software) page lists some.


