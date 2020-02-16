# {{cookiecutter.project_name}}

[![Built with Cookiecutter ReactDjango](https://img.shields.io/badge/built%20with-Cookiecutter%20ReactDjango-blue)](https://img.shields.io/badge/built%20with-Cookiecutter%20ReactDjango-blue)

## Local setup
On your terminal, simply do `docker-compose up --build`, and wait for the containers to build. Eventually, you'll be able to see the index page by going to `[http://127.0.0.1/](http://127.0.0.1/)`.

## Test coverage
To run the tests, check your test coverage, and generate a coverage report:

```
docker-compose run --rm django pytest
```

## Deployment
You can check how to deploy your app to Heroku [here](https://github.com/ohduran/cookiecutter-react-django#deploy-to-heroku)
