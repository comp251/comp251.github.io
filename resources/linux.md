---
layout: default
title: Linux tools and shell
parent: Course Resources
description: Bash, Vim, Tmux, and Linux Tips
nav_order: 3
---

# {{ page.description }}

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

# Vim

# `tmux`

You may want to invest a little time in learning how to use tmux to have
multiple windows open in one ssh window __and to be able to quit and reconnect
to an existing session__. Here’s a couple of tutorials:

* [Getting Started with Tmux](https://linuxhandbook.com/tmux/)
* [How to Use Tmux + Cheat
  Sheet](https://www.hostinger.com/tutorials/tmux-beginners-guide-and-cheat-sheet/)

-
