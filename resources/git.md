---
layout: default
title: Git and GitHub
parent: Course Resources
description: Git and GitHub
nav_order: 6
---

# {{ page.description }}
{: .no_toc }

Make sure that you [sign up](https://github.com/signup) for a GitHub account and
activate your [benefits for
students](https://education.github.com/discount_requests/pack_application).

You'll be writing Markdown files for lab writeups. GitHub has provided a nice
[cheat
sheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
for formatting a document using Markdown.

## git resources

* This [series of videos](https://git-scm.com/videos) does a good job of
  providing an overview of version control and git.
* The [git book](https://git-scm.com/book/en/v2) (especially chapters 1--3)
  provide a nice overview of git.
* GitHub has a
  [guide](https://docs.github.com/en/get-started/using-git/about-git) for git
  beginners.
* GitHub also has videos on YouTube, including [this
  playlist](https://www.youtube.com/playlist?list=PLg7s6cbtAD15Das5LK9mXt_g59DLWxKUe)
  that covers some basics.

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

