import click
import pickle

from membli.storage import Storage


STORAGE_FILE = 'membli.bin'

@click.group()
def cli():
    pass


@cli.command('init', help='initiate key-value storage')
@click.option('-l', '--lock', 'lock')
def init(lock):
    """
    TODO:
    """
    import os
    myhost = os.uname()[1]
    
    with open(STORAGE_FILE, 'wb') as f:
        storage = Storage(myhost)
        pickle.dump(storage, f)
    

@cli.command('get', help='Get value from key-value set')
@click.argument('key')
def get(key):
    """
    TODO:
    """

    try:
        with open(STORAGE_FILE, 'rb') as pk_storage:
            storage = pickle.load(pk_storage)
            val = storage.get(key)
            print(val)
    except FileNotFoundError:
        print('No storage, create with `init` option')


@cli.command('put', help='Put key-value set')
@click.argument('key')
@click.argument('value')
def put(key, value):
    """
    TODO:
    """

    try:
        rf = open(STORAGE_FILE, 'rb')
        update_storage = pickle.load(rf)
        rf.close()

        wf = open(STORAGE_FILE, 'wb')
        update_storage.update(key, value)
        pickle.dump(update_storage, wf)
    except FileNotFoundError:
        print('No storage, create with `init` option')
        

@cli.command('delete', help='Delete key-value set from storage')
@click.argument('key')
def delete(key):
    """
    TODO:
    """

    try:
        rf = open(STORAGE_FILE, 'rb')
        update_storage = pickle.load(rf)
        rf.close()

        wf = open(STORAGE_FILE, 'wb')
        update_storage.delete(key)
        pickle.dump(update_storage, wf)
        wf.close()
        
    except FileNotFoundError:
        print('No storage, create with `init` option')


@cli.command('list', help='Display list of key-value sets in storage')
def list():
    """
    TODO:
    """

    with open(STORAGE_FILE, 'rb') as buf_read:
        try:
            data = pickle.load(buf_read)
            data.list()
        except EOFError:
            raise Exception('Cannot load file')
