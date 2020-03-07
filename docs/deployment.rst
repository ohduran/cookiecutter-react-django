.. _deployment:

Deployment
==========

Deployment with Heroku
----------------------

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
