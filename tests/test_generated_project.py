import os

from cookiecutter.main import cookiecutter
from plumbum import local
from plumbum.cmd import pylama


def generate_project(**kwargs):
    cookiecutter(template='./', checkout=None, no_input=True, **kwargs)


def test_code_style(tmpdir):
    output_dir = str(tmpdir)
    print(output_dir)
    generate_project(output_dir=output_dir)
    with local.cwd(os.path.join(output_dir, 'project_name')):
        pylama()
