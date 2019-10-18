import json
import logging
import os
import pycos
import uuid

from datetime import datetime

# Set up logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s.%(msecs)03d %(levelname)-6s %(name)s :: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


LOGGER = logging.getLogger('cos_example')
LOGGER.setLevel(logging.DEBUG)


def main():
    try:
        with open('config.json') as jsn_file:
            config = json.load(jsn_file)

        bucket = str(uuid.uuid4())
        filename = 'upload.json'

        from datetime import datetime
        msg = f'{{"message":"inmem", "time":"{str(datetime.now())}"}}'

        adm = pycos.COSAdmin(config)
        adm.bucket_create(bucket)

        wtr = pycos.COSWriter(config, bucket)
        wtr.store('inmem', msg)

        key1 = 'inmem'
        with pycos.COSReader(config, bucket, key1) as cos_reader:
            contents = cos_reader.readlines()
            print(f'{contents}')


        msg = f'{{"message":"file", "time":"{str(datetime.now())}"}}'
        with open(filename, 'w') as fout:
            fout.write(msg)

        wtr.upload('upload', filename)

        key2 = 'upload'
        with pycos.COSReader(config, bucket, key2) as cos_reader:
            contents = cos_reader.readlines()
            print(f'{contents}')

        bkts = adm.bucket_list()
        print(f'{bkts}')

        cnts = adm.bucket_contents(bucket)
        print(f'{cnts}')

        adm.bucket_content_delete(bucket, key1)
        adm.bucket_content_delete(bucket, key2)

        adm.bucket_delete(bucket)

        os.remove(filename)

    except pycos.COSClientError as client_err:
        LOGGER.error(client_err)


if __name__ == '__main__':
    main()
