import os
from zerotk.easyfs import FindFiles, GetFileContents, CreateFile
import yaml


def create_project(project_name, config_filename):

    config = yaml.load(open(config_filename))

    template_dir = os.path.dirname(__file__) + '/template'
    for i_template_filename in FindFiles(template_dir, '*.*'):
        target_filename = project_name + '/' + os.path.basename(i_template_filename)
        create_project_file(
            target_filename,
            i_template_filename,
            config
        )
        yield target_filename


def create_project_file(target_filename, template_filename, config):
    from jinja2 import Template
    template = Template(GetFileContents(template_filename))
    CreateFile(
        target_filename,
        template.render(**config)
    )
