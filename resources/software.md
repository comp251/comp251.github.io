---
layout: default
title: Software
parent: Course Resources
description: Recommended Software
nav_order: 2
---

# {{ page.description }}

* Off campus access to Rhodes via the [Rhodes VPN](https://tinyr.us/rhodes-vpn).
  You should be given access to the Rhodes VPN, so you should not need to file a
  ticket. You will, however, need to download the Fortinet client and
  install/configure it.

* A terminal emulator or SSH client for your OS of choice. Most operating
  systems ship with `ssh` already installed.

  To connect to a remote host using ssh, open the terminal/command prompt
  application on your computer and then type `ssh username@hostname` to connect
  to `hostname` as the user named `username`.

  As an example, I connect to `lily` using `ssh langm@lily.rhodes.edu`.


## Other recommended software

* OSX:
  * [Cyberduck](https://cyberduck.io) is a graphical SCP (and FTP, etc.)
    client.
  * You can use the built in Terminal.app, but it is a terrible program.
  * [iTerm2](https://iterm2.com/) replaces the super-crappy built-in terminal application.
* Windows: 
  * Use the built-in command prompt (enter `cmd` or "Command Prompt" in the
    Windows search box), and then you can use `ssh` as outlined above.
  * [WinSCP](https://winscp.net/eng/index.php) is a Windows SCP program.
  * ~[PuTTY](https://www.putty.org/) is a commonly-used SSH client.~ Note: I
    used to recommend PuTTY, but modern versions of Windows ship with `ssh`).
  * Do you have a terminal emulator or ssh client that you prefer? Let me know!

