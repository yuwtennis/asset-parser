
import importlib
import os
import sys
import logging

def main():

    module = os.getenv('LOAD_MODULE')
    name   = os.getenv('NAME')

    if name == 'NomuraSec':
        c = importlib.import_module('apps.{}.{}'.format(module, name))
        c(os.getenv('BRANCH_CODE'),  \
          os.getenv('ACCOUNT_NAME'), \
          os.getenv('SECRET'))
    else:
        logging.warning(f'Wrong class name {name} .')
        sys.exit(1)

    c.run()

if __name__ == '__main__':

    logging.basicConfig(format='%(levelname)s %(asctime)s %(name)s %(message)s', level=logging.INFO)

    main()
