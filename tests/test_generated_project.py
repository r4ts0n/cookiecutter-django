import os

from cookiecutter.main import cookiecutter
from plumbum import local
from plumbum.cmd import pylama, python


def generate_project(**kwargs):
    cookiecutter(template='./', checkout=None, no_input=True, **kwargs)


def test_code_style(tmpdir):
    output_dir = str(tmpdir)
    project_name = 'test_project'
    generate_project(output_dir=output_dir, extra_context={
        'project_name': project_name,
    })
    with local.cwd(os.path.join(output_dir, project_name)):
        pylama()


def test_django_project(tmpdir):
    output_dir = str(tmpdir)
    project_name = 'test_project'
    generate_project(output_dir=output_dir, extra_context={
        'project_name': project_name,
    })
    with local.cwd(os.path.join(output_dir, project_name)):
        with local.env(
            DATABASE_URL='sqlite://localhost/:memory:',
        ):
            python['manage.py', 'migrate']()
        with local.env(
            DJANGO_SETTINGS_MODULE='{}.settings.test'.format(project_name),
        ):
            python['manage.py', 'test']()
