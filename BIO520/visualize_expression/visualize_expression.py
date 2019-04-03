#!/usr/local/bin/python3
""" Parse results from a differential expression analysis and create graphs for visualization.

Usage:
    visualize_expression.py <config_filename>

Options:
    --help                                Display this super helpful help message.
"""
import docopt
import Expression
import json
import jsonpickle


def main(args):
    with open(args['<config_filename>'], 'r') as cfg_file:
        config = json.load(cfg_file)

    expression_analysis = Expression.from_rsem_ebseq(config['treatments'], config['ebseq_runs'], config['treatments_dir'], config['ebseq_dir'], config['calc_expr_extension'])


def load_pickle(file):
    """
    Decode json pickle file into object.
    :param file: json pickle file handle to load object from.
    :return: decoded object
    """
    return jsonpickle.decode(file.read())


def write_pickle(filename, obj, overwrite=True):
    """
    Encode object into json pickle, then open filename and write to file in sorted, human-readable json.
    :param filename: name of pickle file to be written.
    :param obj: object to pickle.
    :param overwrite: if true will overwrite an existing file, if false will append to existing file.
    :return: None
    """
    mode = 'w' if overwrite else 'a'
    with open(filename, mode) as file:
        pickled_object = jsonpickle.encode(obj)
        temp_json = json.loads(pickled_object)
        json_str = json.dumps(temp_json, sort_keys=True, indent=4)
        file.write(json_str)


if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    main(arguments)
