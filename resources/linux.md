---
layout: default
title: Linux tools and shell
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

## Transferring files with SCP

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
$ cp my_prog.c langm@iris.rhodes.edu:./my_prog.c
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

# `git` and GitHub

Make sure that you [sign up](https://github.com/signup) for a GitHub account and
activate your [benefits for
students](https://education.github.com/discount_requests/pack_application).

You'll be writing Markdown files for lab writeups. GitHub has provided a nice
[cheat
sheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
for formatting a document using Markdown.

# Setting up `git`

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

# Vim

{: .warning }
You will probably hate using Vim at first.

Using a command-line text editor is a vital process skill and Vim is both
ubiquitous and well-supported, with a rich collection of plugins that [can make
your life easier](https://youtu.be/9n1dtmzqnCU).

There are several tutorials and cheet sheets online. One is even built into Vim
itself!

* Run `vimtutor` for an interactive tutorial inside of Vim.
* [This](https://devhints.io/vim) is a decent basics cheat sheet.
* [This](https://vim.rtorr.com/) is a more detailed cheat sheet.
* [Vim Adventures](https://vim-adventures.com) is a cute game that helps you
  learn the basic movement commands (these will come in useful!). The full game
  is not free, but the free preview has good coverage of basic movement.

# `tmux`

ssh attempts to make connections persistent. However, like any other application
running on the network, you will drop an ssh connection when you disconnect from
the internet. This can be frustrating when you're in the middle of working!

One way to prevent this frustration is to create a persistent terminal session
on the remote machine--think of this like a set of windows that you can
disconnect from and reconnect to.  `tmux` is a program that allows you to do
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

