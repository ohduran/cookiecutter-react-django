#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import json
import os
import shutil
import webbrowser

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "cookiecutter.json"), "r") as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of project_slug from cookiecutter.json
COOKIECUTTER_SETTINGS["project_name"] = "Project Name"
COOKIECUTTER_SETTINGS["project_slug"] = "project_name"
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS["project_slug"])
REQUIREMENTS = os.path.join(COOKIE, "backend", "requirements", "development.txt")


@task
def build(ctx):
    """Build the cookiecutter."""
    print('Making sure running cookiecutter with this folder works')
    ctx.run(f"cookiecutter {HERE} --no-input")


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)

def _run_docker_compose(ctx, command, *args):
    docker_compose_command = f"docker-compose {command}"
    ctx.run(docker_compose_command, echo=True)

def _build_production_image(ctx):
    ctx.run("docker build -t production:latest .")

@task(pre=[clean, build])
def test(ctx):
    """Run lint commands and tests."""
    os.chdir(COOKIE)
    _run_docker_compose(ctx, "build")
    _run_docker_compose(ctx, "run --rm django pytest")
    _build_production_image(ctx)
