---
layout: default
title: Vim and Tmux
parent: Course Resources
description: Vim and Tmux
nav_order: 5
---

# {{ page.description }}
{: .no_toc }

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

