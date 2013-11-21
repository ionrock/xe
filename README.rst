====
 Xe
====

`xe` stands for eXecutable Environment.

There are a ton of "best practices" for python projects. We can all
agree that you should use a virtualenv_ and a test runner such as
pytest_ or nose_. Pip_ is another good tool to use. Sphinx_ is great
for documentation. The list goes on.

The problem is that while we agree on the tools, we seldom agree on
how we should use the tools. Some people use virtualenvwrapper_ and
prefer to hide all their virtualenv's in a hidden directory. Others
prefer to create a directory within the project root. Others like to
do a `virtualenv .` to create a virtualenv for a project so activation
does the "Right Thing" with the prompt and uses the project name. Not
to mention tools like tox_ that help create virtualenvs for different
versions of Python and make sure your dev environment doesn't mix with
your test environment.

While I'm positive that I can't bring the Python world together in
harmony, I can write a tool to make this sort of environment
management and automate my own standard practices. I'm calling this
tool `xe`.


Project Opinions
================

`xe` is opinionated in decisions it makes regarding a project's dev
environment. These opinions are never meant to be controversial! In
fact the goal is to be as benign as possible in hopes that `xe` will
easily support any developer's workflow.

With that in mind, there are some ideals that `xe` tries to maintain
in order to be general and easy to work with.

 1. all commands should be runnable without a required "activation"
    step
 2. a project should have its own environment

While it is handy to be able to "activate" your environment, it
creates a fragile environment. It makes it really easy to do a `pip
install somepackage` where you fail to realize you never added it to
your `setup.py` or a `dev_requirements.txt`. Therefore, `xe` doesn't
force you to activate your environment.

Another benefit of avoiding an activation step is that other tools can
reliably call a single command without having to configure an
environment haphazardly. For example, in an IDE it is nice to
configure a build step to test the current test file you are working
on. Using `xe` you can easily configure that step as `xe test
$fn`. There is not a list of environment variables you have to setup
and configure. You don't have to specify a virtualenv directory or
testing tool. `xe` takes care of it.

A project should have its own environment because you should be
testing and using that project in isolation. That doesn't mean you
shouldn't have subrepos or install other packages as editable. It
simply means that if you are working in a project directory, you
should be using that project's environment.


Standard Project Files and Directories
======================================

Here are the standard project files and directories that `xe`
utilizes.


  1. setup.py
  2. requirements.txt
  3. dev_requirements.txt
  4. .bumpversion.cfg
  5. a version control . directory
  6. docs/
  7. tests/
  8. build file (Makefile, pavement.py, tasks.py, etc.)
  9. venv/ (virtualenv directory)

Most of these can be configured to point to other non-root
directories, but if you use these files, `xe` will try to work out of
the box without extra configuration.


Getting Started
===============

Typically you'd read this first, but as this is our code we're talking
about we needed to get the prereq's out of the way and make sure that
your project isn't going to get borked by `xe`. Assuming things look
reaonable, you can get started by doing:

  $ xe bootstrap

`xe` will create a virtualenv if one hasn't been created yet. It will
then look for a `dev_requirements.txt` and run that in the newly
create environment. From there you can use xe to run tasks. A good
default is simply running python:

  $ xe python

That will start up the python in the `xe` virtualenv. If you are using
a django project you can use the following shortcut to have access to
your `manage.py` commands:

  $ xe manage runserver

If you use pytest, you can run your tests too:

  $ xe test -x

Say you build your docs with make, you can use `xe` to run make and be
confident your environment will be in place.

  $ xe make html

That is it!
