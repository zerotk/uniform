from zerotk.uniform import create_project
import os


def test_uniform(embed_data):
    obtained_filenames = create_project(embed_data['TESTE'], embed_data['.zerotk.uniform.yml'])

    for i_obtained_filename in obtained_filenames:
        expected_filname = embed_data['expected'] + '/' + os.path.basename(i_obtained_filename)
        embed_data.assert_equal_files(
            i_obtained_filename,
            expected_filname
        )
