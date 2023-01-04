---
layout: default
title: Code Conventions 
parent: Course Resources
description: Code Style and Conventions
nav_order: 5
---

# {{ page.description }}

{: .note }
Programming with a consistent and readable style is an important process skill.
It makes it easier for others to read and understand your code and for you to
work with other engineers/researchers on projects. All projects have a
[programming style](https://en.wikipedia.org/wiki/Programming_style) convention.
For example, [here](https://google.github.io/styleguide/) is Google's collection
of style guides for various languages.

One of the process skills that I want you to learn in this class is for you to
write code that is readable.  A portion of each lab grade will be reserved for
good style and conventions for code. 

We will follow the LLVM style convention. You can read the style guide
[here](https://llvm.org/docs/CodingStandards.html#style-issues).  Though some of
it is not applicable to the code that we will write in this class, the
high-level advice and low-level rules are a good read and might help you think
about how to better structure the code that you write.

## `clang-format`

Vim has been set up so that the `clang-format` tool is run each time you save a
C file. This tool automatically formats your files so that they meet the LLVM
[coding standards](https://llvm.org/docs/CodingStandards.html#style-issues).

The files that you turn in must meet this style. If you absolutely need to
disable `clang-format`, you can surround code in blocks that turn off the
formatter:

```
// clang-format off
... // unformatted code
// clang-format on
```
