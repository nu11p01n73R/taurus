from configparser import ConfigParser
import os


def parse_file(file_name):
    config = ConfigParser()
    config.read(file_name)

    output = {}
    if 'MONGO' in config:
        mongo = config['MONGO']
        output['mongo'] = {
                'url': mongo['url'],
                'db': mongo['db']}

    return output


def parse_environ():
    return {
            'mongo': {
                'url': os.environ['MONGO_URL'],
                'db': os.environ['MONGO_DB']}}


config = parse_file('config.ini')
if not config:
    config = parse_environ()
