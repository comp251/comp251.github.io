---
layout: default
title: SSH and Remote Access
parent: Course Resources
description: SSH and Remote Access
nav_order: 3
---

1. TOC
{:toc}

# {{ page.description }}

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

# Passwordless SSH

You can set up SSH so that you don't need to enter your password each time. To
do so, you'll need to generate a public/private key pair, and copy the public
key to the remote computer.

Do the following _on your local computer_:

```
$ ssh-keygen -t rsa -b 4096 -C "your_email@address.com"
```

Hit enter to accept the default file location. When it prompts you for a
password, __just hit enter__--do not enter a password!

Now, copy you newly-generated SSH id to the remote machine:

```
$ ssh-copy-id user@lily.rhodes.edu
```

Now you should be able to log in without using a password.

## Passwordless ssh between lily/iris

To SSH between lily and iris without using a password, follow the same step
running `ssh-keygen` __while you are logged in to lily__. Then, simply do the
following:

```
$ cat .ssh/id_rsa.pub > ~/.ssh/authorized_keys
```

Now you should be able to simply run `ssh iris` to connect to iris without a
password.

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


