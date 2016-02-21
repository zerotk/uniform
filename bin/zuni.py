import click
import os
from zerotk.easyfs import FindFiles
from zerotk.uniform import create_project


@click.command()
@click.argument('project_name')
def mkproject(project_name):
    assert os.path.isdir(project_name)
    for i_filename in create_project(project_name, project_name + '/.zerotk.uniform.yml'):
        click.echo(i_filename)


if __name__ == '__main__':
    mkproject()