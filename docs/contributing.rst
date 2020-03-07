.. _contributing:

Contributing
============

  *The question, O me! so sad, recurring—What good amid these, O me, O life?*

  *Answer.*

  *That you are here—that life exists and identity,*
  *That the powerful play goes on, and you may contribute a verse.*

  —  `Walt Whitman <https://www.poetryfoundation.org/poems/51568/o-me-o-life>`_

Do you want to contribute to Cookiecutter React Django? Great. First of all, **thank you** for even considering it. By contributing to open source software, you're making a scalable impact on how our society reaps the benefit of the Internet revolution. If `software is eating the world <https://a16z.com/2011/08/20/why-software-is-eating-the-world/>`_, by donating even a small amount of time, you're in a position to dictate how that will happen.

That said, we need to come to terms on how we are going to do that. If we establish a set of guidelines that make contributing to open source software enjoyable, then more of us will join and more valuable the whole enterprise will be.

We hope that this document makes the experience of contributing clearer and easier.

Community
---------

The most important thing you can do to help push the Cookiecutter React Django project forward is to be actively involved in the manner that you see most adequate. Code contributions are often the most prominent way to get involved in an open source project, but that isn't the only one.

If you have ever used Cookiecutter React Django, or planned on doing so, we would love you to be vocal about it. A tiny blog post about your overall experience, a casual conversation with a friend about it, anything is potentially a window into the community that revolves around this particular project. The ultimate goal of this piece of software is *making developers' lives easier*. Even if you are a beginner, keep in mind that your experience may be particularly helpful because you are in the best position to assess which bits are harder to understand or work with.

Even the Contributing guidelines are in scope for changes. Feel free to give any feedback that you may have on it.

Code of Conduct
---------------

Please keep the tone polite & professional. For some, your post may be their very first engagement with this project, or even with open source in general. First impressions do count, so please let's make everyone feel welcome.

Issues
------

Feature requests, bug reports and other issues should be raised on the GitHub `issue tracker <https://github.com/ohduran/cookiecutter-react-django/issues?q=is%3Aopen>`_.

If you intend to make any non-trivial changes to the implementation of this project, we recommend creating an issue ticket. This lets us reach an agreement on your proposal before you put significant effort into it.

If you’re only fixing a bug, it’s fine to submit a pull request right away, but we still recommend to create an issue ticket detailing what you’re fixing. This is helpful in case we don’t accept that specific fix but want to keep track of the issue.

Some tips on good issue reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* When describing an issue, phrase your ticket in terms of the *behaviour* that needs changing, rather than the code.
* Before submitting a ticket, have you searched for similar ones? Has a conversation about a problem similar to yours already started?
* If reporting a bug, it would be great if you can include a *failing test case*. That will make the conversation revolve around code, and will allow for the ticket to have boundaries that make it solvable faster. Mozilla has `bug reporting guidelines <https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines>`_ that we believe hint adequately how bugs should be reported, but feel empowered to think critically about any of them if you think there's a way to do it better.
* Closing an issue doesn't necessarily mean the end of a discussion.  If you believe your issue has been closed incorrectly, explain why and we'll consider if it needs to be reopened.

Security Bugs
~~~~~~~~~~~~~

Please **do not file security issues publicly**; go through the process outlined on :ref:`security`.

Development
-----------

To start developing on Cookiecutter React Django, clone the repo:

.. code-block:: bash

    git clone https://github.com/ohduran/cookiecutter-react-django


Testing
~~~~~~~

  *Once I got a suite of tests to pass, I would make sure that those tests were convenient to run for anyone else who needed to work with the code. I would ensure that the tests and the code were checked in together into the same source package.*

  —  Robert 'Uncle Bob' Martin


Tests on this project are run with `Jest <https://jestjs.io/>`_, for the React front-end, and `pytest <https://docs.pytest.org/en/latest/>`_, for the Django back-end.

To run the back-end tests, simply `cd` into the `{{cookiecutter.project_slug}}` folder and do:

.. code-block:: bash

  docker-compose run --rm django bash
  root@98923d344e8a:/app/backend# pytest


Likewise, to run the front-end tests, you must do `npm test` from the `react` container:

.. code-block:: bash

  docker-compose run --rm react npm test

Be aware that Jest runs on watch mode, which means that each change that you make on the code will rerun the Jest tests.

Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~

No pull request can be merged without passing tests. `Travis CI <https://travis-ci.org/>`_, what this project uses for continuous integration, won't give the GO signal unless:

* Back-end tests pass on the `django` container
* Front-end tests pass on the `react` container
* Production image builds correctly

Pull requests
-------------

**Is it your first pull request?** Then you may want to have a look at `this video tutorial <https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github>`_. There may be some
`good first issues <https://github.com/ohduran/cookiecutter-react-django/issues?q=is:open+is:issue+label:%22good+first+issue%22>`_ to help you get your feet wet and get you familiar with our contribution process.

We recommend that you make PRs early on, because we believe that they are the conversation starter, not the final, finished submission. It's also best to make a new branch before starting to work on a PR, preferably named after the associated issue ticket, if there's any. Thus, you'll be able to switch back to work on another issue without interfering with an ongoing PR.

Keep in mind that if you have an outstanding PR, then pushing new commits to your GitHub repo will also automatically update the PR, which is very convenient in our opinion.

It's best for everyone involved if you run the tests before submitting PRs, given that the CI infrastructure won't allow for the PR to be merged unless all tests pass. Once you've made a pull request take a look at the Travis build status in the GitHub interface and make sure the tests are running as you'd expect.

Branch Organisation
~~~~~~~~~~~~~~~~~~~

Submit all changes directly to the master branch. It's just easier for everyone.

Dependency Upgrades
~~~~~~~~~~~~~~~~~~~

If you noticed that any library dependency is outdated, we encourage you to submit a PR with the necessary changes. It's one of team's priority to always run on the latest version possible of third party libraries. By naming the branch `DepYYYYMMDD`, maintainers will know in advance what the PR aims at doing, and will prioritise accordingly.

License
-------

By contributing to Cookiecutter React Django, you agree that your contributions will be licensed under its `License <https://github.com/ohduran/cookiecutter-react-django/blob/master/LICENSE>`_.
