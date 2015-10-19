import os

import pytest

from cookiecutter.main import cookiecutter
from plumbum import local
from plumbum.cmd import pip, python


def generate_project(**kwargs):
    cookiecutter(template='./', checkout=None, no_input=True, **kwargs)


def test_code_style(tmpdir):
    output_dir = str(tmpdir)
    project_name = 'test_project'
    generate_project(output_dir=output_dir, extra_context={
        'project_name': project_name,
    })
    with local.cwd(os.path.join(output_dir, project_name)):
        pip['install', '-r', 'requirements/test.txt']()
        local['pylama']()


@pytest.mark.parametrize('use_django_cms', ['y', 'n'])
def test_django_test(tmpdir, use_django_cms):
    output_dir = str(tmpdir)
    project_name = 'test_project'
    generate_project(output_dir=output_dir, extra_context={
        'project_name': project_name,
        'use_django_cms': use_django_cms,
    })
    with local.cwd(os.path.join(output_dir, project_name)), local.env(
        DJANGO_SETTINGS_MODULE='{}.settings.test'.format(project_name)
    ):
        pip['install', '-r', 'requirements/test.txt']()
        python['manage.py', 'test']()
