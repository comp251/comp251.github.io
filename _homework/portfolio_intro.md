---
layout: default
title: "Programming Portfolio (intro)"
nav_order: 1
---

# Building a Portfolio

One goal that I have for this class is for you to get more experience
programming. You should leave this class feeling comfortable writing short
programs in C.

A secondary goal that I have is for you to be prepared to apply for internships
and jobs post-graduation. When applying for these positions, having a portfolio
of work that you can share will be important, as it gives evidence for the
claims that you make on your resume.

To achieve this goal, you will be writing __at least one small program per
week__, starting after [lab 0](labs/lab0) (due date TBD).

# The practice of programming

Have you ever played a competitive sport? Learned a musical instrument? If so,
you are familiar with the importance of __practice__. When you practice, you
take the theory and abstract principles that you have learned and you apply
them, over and over.

By design, practice is an instantiation of [the learning
cycle](https://www.simplypsychology.org/learning-kolb.html). When you practice,
you expect to struggle, fail, and learn from your mistakes. Eventually, you
perfect some skill through repetition of this process. And, even when you have
perfected the skill, you continue to practice it in order to maintain the level
of skill that you achieved..

If you aim to be skilled at any sport or art, you expect that extensive practice
will be part of the process. __Programming is no different.__ 

So if our goal is to prepare you to be able to program, practice is necessarily
a part of this preparation.

# Code katas 

We will practice programming through a series of programming problems, similar
to what you might expect to see in an interview. None of them will be
particularly algorithmically challenging. The act of solving these types of
problems is commonly called "code
[katas](https://en.wikipedia.org/wiki/Kata)"--borrowing the idea of small
exercises to practice and perfect movements in martial arts. 

The concept was introduced in a classic software engineering book "[The
Pragmatic Programmer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)"
and is a common way of learning a programming language. Here's a few examples:

* [codekata.com](http://codekata.com/) site
* [Awesome Katas](https://github.com/gamontal/awesome-katas) repo
* [Coding Dojo](https://codingdojo.org/kata/) katas
* A [curated
  list](https://hackmd.io/@pierodibello/A-curated-list-of-programming-kata) of
  katas

# The assignment

I will assign one programming exercise per week, starting after the first lab.

You will use these assignments to build a portfolio in the form of a GitHub
repository.

__When the first exercise is assigned__, you will follow this process to set up
and initialize your repository.

1. Create a __private__ [GitHub repository](https://github.com/new). 

   * Name your repository "c-exercises".
   * Use the `.gitignore` template for C.
   * Check the button to add a README file.

2. From the repository page, click on Settings, then Collaborators (see image
   screenshot below).

   * Add me ([@ml8](https://github.com/ml8)) and the course TAs (TBD) as
     collaborators. We should be given the "Maintain" role.

   ![](/assets/repo-collaborators.png)
   
3. Clone the repository on lily.
   
   * `git clone <your repo url>`

4. When an exercise is assigned, create a new branch for the exercise.

5. Turn the exercise in by creating a pull request.

# Code reviews

Given the size of this class and the number of exercises, it is infeasible to
give a detailed code review for each exercise.

Though each assignment will be graded, you will do __at least__ two face-to-face
code reviews with me this semester: once before the midterm and once afterward.

You can choose the assignment that we review one-on-one and you will create an
office hours appointment for us to go through your code. You must do this twice.

# Rubric

* Each assignment will be graded on a scale of 1-5:

  | Score | Meaning |
  |---|---|
  | 1 | You turned in the assignment |
  | 2 | You turned in code that compiles but has several major flaws |
  | 3 | Your code is mostly correct but has a major flaw |
  | 4 | Your code is mostly correct and may have a minor flaw or is does not meet readability standards  |
  | 5 | Your code is correct and meets readability standards |

* At the end of the semester, each missing one-on-one session deducts 50% from
  the total grade for all exercises.

# After the semester

After the semester, you can (and should!) make your repository public. Spend
some time cleaning up your code and the aesthetics of the repository. Work on
your README to describe the overall repository and link to each exercise. Make a
[GitHub pages](https://pages.github.com/) site for your work. __Congratulations!
You have a portfolio!__

Note that you __may not__ make your lab assignment repositories public. You can,
however, add a note in your portfolio that you have other examples of your work
from this course available to recruiters _upon request_. This strategy has been
successful for students in my COMP385: Distributed Systems course in the past.
