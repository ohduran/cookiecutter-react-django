.. Cookiecutter React Django documentation master file, created by
   sphinx-quickstart on Fri Mar  6 21:16:51 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cookiecutter React Django
=========================

.. image:: https://travis-ci.com/ohduran/cookiecutter-react-django.svg?branch=master
    :target: https://travis-ci.com/ohduran/cookiecutter-react-django.svg?branch=master

**Cookiecutter React Django** [1]_ is a framework for jumpstarting production-ready projects quickly.

-------------------

Powered by `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`_, Cookiecutter React Django combines the capabilities of Django as a backend service with the flexibility and ease of use of React into an opinionated framework that allows you to jumpstart a production-ready web application.

Features
--------

* **Latest versions of Python, Django and React**: With the latest security updates and the newest features available.
* **Docker**: Your app becomes a lightweight, standalone, executable package of software.
* **WhiteNoise**: Radically simplify static file serving for your web app.
* **Heroku ready**: Create an app, set up the configuration and deploy.

Local setup
-----------

Let's assume that you want to create a project called "hello_world", one that makes a separation between a React-based front end and a Django-based backend, all set up locally using Docker and production ready in Heroku.

Most tutorials will give you a partial solution, so the only way is painstakingly piecing together a solution from multiple guides/tutorials that did some aspect of what you want without covering the whole.

  *Side projects don't exactly require optimal productivity, but, unlike jobs, if they become a pain to work on, it's pretty easy to just quit.*

Instead, we can do as follows. First, get Cookiecutter. Trust me, it's awesome:

``$ pip install "cookiecutter>=1.7.0"``

Now run it against this repo:

``$ cookiecutter https://github.com/ohduran/cookiecutter-react-django``

You'll be prompted for some values. Provide them, then the project will be created for you.

Now, on your terminal, simply do docker-compose up --build, and wait for the containers to build. Eventually, you'll be able to see the index page by going to http://127.0.0.1/

You will be able to see the following:

.. image:: _static/index-demo.png
    :target: _static/index-demo.png

Write something on that box over there, it will get you the number of characters via your Django API!

.. image:: _static/api-demo.png
    :target: _static/api-demo.png



Deployment
---------------

If you're new to Heroku, their `getting started guide <https://devcenter.heroku.com/articles/getting-started-with-python>`_ will walk you through the basics of creating a generic, non-dockerized Python app. If you don’t have it yet, install the `Heroku CLI <https://devcenter.heroku.com/articles/getting-started-with-python#set-up>`_.

1. We can create a Heroku app by running ``heroku create`` within our project. Once you've done it, Heroku will provide you with the following message:

    ``
    Creating app... done, ⬢ one-example-12345
    https://one-example-12345.herokuapp.com/ | https://git.heroku.com/one-example-12345.git
    ``

    In this case, ``one-example-12345`` is the name of the app; yours is likely to be different.

2. Make sure you link the Heroku app with your repository by running ``heroku git:remote -a [app_name]``.

3. For environment variables in production, you can set the config variables by running the following command:

  ``heroku config:set PRODUCTION_HOST=[app_name].herokuapp.com SECRET_KEY=[your secret key] DJANGO_SETTINGS_MODULE=backend.settings.production``

  You can generate a valid Django Secret Key via `this link <https://miniwebtool.com/django-secret-key-generator/>`_. REMEMBER to put the key between apostrophes ('), or you will likely get a ``-bash: ****: event not found`` error.

4. Now run ``heroku stack:set container`` to tell our Heroku app to use Docker.

5. At this point, you're ready to deploy: run ``git push heroku master``.

6. Checkout https://[app_name].herokuapp.com. You should be able to see your web app ready!

Contributing
------------

To learn more about contributing, please read `our contributing docs <https://github.com/ohduran/cookiecutter-react-django/blob/master/CONTRIBUTING.md>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

-------------------

.. [1] This project is based on a series of tutorials written by `Craig Franklin <https://github.com/cfranklin11>`_ called `Creating an app with Docker Compose, Django, and Create React App <https://dev.to/englishcraig/creating-an-app-with-docker-compose-django-and-create-react-app-31lf>`_
