====
 Xe
====

`xe` stands for eXecutable Environment.

There are a ton of "best practices" for python projects. We can all
agree that you should use a virtualenv_ and a test runner such as
pytest_ or nose_. Pip_ is another good tool to use. Sphinx_ is great
for documentation. The list goes on.

.. _virtualenv: http://virtualenv.org
.. _pytest: http://pytest.org
.. _nose: http://nose.readthedocs.org/en/latest/
.. _pip: http://pip-installer.org
.. _sphinx: http://sphinx-doc.org


The problem is that while we agree on the tools, we seldom agree on
how we should use the tools. Some people use virtualenvwrapper_ and
prefer to hide all their virtualenv's in a hidden directory. Others
prefer to create a directory within the project root. Others like to
do a `virtualenv .` to create a virtualenv for a project so activation
does the "Right Thing" with the prompt and uses the project name. Not
to mention tools like tox_ that help create virtualenvs for different
versions of Python and make sure your dev environment doesn't mix with
your test environment.

.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
.. _tox: http://tox.readthedocs.org/en/latest/

While I'm positive that I can't bring the Python world together in
harmony, I can write a tool to make this sort of environment
management and automate my own standard practices. I'm calling this
tool `xe`.


Project Opinions
================

`xe` is slightly opinionated in decisions it makes regarding a
project's dev environment. These opinions are never meant to be
controversial! In fact the goal is to be as benign as possible in
hopes that `xe` will easily support any developer's workflow.

With that in mind, there are some ideals that `xe` tries to maintain
in order to be general and easy to work with.

 1. all commands should be runnable without a required "activation"
    step
 2. a project should have its own environment


Avoiding Activation
-------------------

If you've ever deployed a project only to realize that you failed to
update a dependency, then there is a good chance you were bitten by a
fragile environment. While it is handy to be able to "activate" your
environment, it makes it really easy to miss things when you are
updating dependencies.

Xe explicitly avoids shell level activation and instead finds your
virtualenv on every command.


The Right Environment for Every Command
---------------------------------------

Another area `xe` helps is when you use an IDE type tool. Most editors
and IDEs have the idea of a project. In the project settings you can
configure builds that typically map to running tests or project
tasks. If you are using a non-virtualenv aware tool, you usually have
to configure environment variables in order to make sure the correct
virtualenv is used. Even if your tool does understand virtualenvs, you
still need to supply some configuration to the correct environment.

Using `xe` you can easily configure the default build as `xe test
$fn`. There is not a list of environment variables you have to setup
and configure. You don't have to specify a virtualenv directory or
testing tool. You can let `xe` takes care of it.


Isolating Your Environment
--------------------------

A project should have its own environment because you should be
testing and using that project in isolation. That doesn't mean you
shouldn't have subrepos or install other packages as editable. It
simply means that if you are working in a project directory, you
should be using that project's environment.

Along similar lines, a project environment should be easy to delete
and rebuild from scratch. Using `xe`, the default behavior is to
create a directory local virtualenv that can be removed and rebuilt
from scratch when necessary.


Standard Project Files and Directories
======================================

Here are the standard project files and directories that `xe`
utilizes.

  1. setup.py
  2. requirements.txt
  3. dev_requirements.txt
  4. venv/ (virtualenv directory)

Most of these can be configured to point to other non-root
directories, but if you use these files, `xe` will try to work out of
the box without extra configuration.

It would be nice to eventually support different build tools, but I
imagine that will be implemented via plugins. The idea being that an
organization could implement their own build entry points and use `xe`
to run them correctly.


Getting Started
===============

Typically you'd read this first, but as this is our code we're talking
about we needed to get the prereq's out of the way and make sure that
your project isn't going to get borked by `xe`. Assuming things look
reaonable, you can get started by doing:

  $ xe bootstrap

`xe` will create a virtualenv if one hasn't been created yet. It will
then look for a `dev_requirements.txt` and run that in the newly
create environment. From there you can use `xe` to run tasks. A good
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


Working with Virtual Machines
-----------------------------

Another concept of an environment is to work on a remote machine or
virtual machine such as `Vagrant <https://vagrantup.com>`_. `xe`
supports `rdo <https://rdo.readthedocs.org/en/latest/>`_ for running
commands on remote machines.

To use `rdo` for all commands, add to your `.xerc`:

.. code-block:: yaml

   USE_RDO: true

If you only want to use `rdo` for specific commands, specify them via
the `RDO_COMMANDS` field:

.. code-block:: yaml

   RDO_COMMANDS:
     - make
     - python
