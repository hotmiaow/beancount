"""Read a beancount input file and a directory name, and attempt to identify
and convert the files in the directory. There is also an option to automatically
file succesfully detected and converted input files.
"""
from beancount.imports import scripts


def main():
    """This function uses the same import mechanism as beancount.imports.script
    does. We put our main program there so that users are able to create their
    own embedded import script instead of calling this with a filename. This is
    because the process of specifying imports is very much customized to the
    user and should not change very often. We provide evertyhing so that the
    user can create their own Python script, which specifies the import
    configuration as a simple Python object.
    """

    # Create a parser and parse the arguments. We add the configuration file
    # from which we'll extract the Python object that drives the importer
    # matching process.
    parser = scripts.create_parser(None, None)

    parser.add_argument('-c', '--config', action='store', metavar='FILENAME',
                        help=('Importer configuration file. '
                              'This is a Python file with a data structure that '
                              'is specific to your accounts'))

    opts = parser.parse_args()

    # Load the importer config from its Python file.
    importer_config = scripts.load_module_attribute(opts.config, 'CONFIG')

    # Run the importer.
    scripts.import_with_options(importer_config, opts)


if __name__ == '__main__':
    main()