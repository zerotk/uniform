import click
import os
from zerotk.easyfs import FindFiles


@click.command()
@click.argument('project_name')
def mkproject(project_name):
    template_dir = os.path.dirname(__file__) + '/../template'
    click.echo('template files: ' + template_dir)
    for i_filename in FindFiles(template_dir, '*.*'):
        click.echo(i_filename)


if __name__ == '__main__':
    mkproject()