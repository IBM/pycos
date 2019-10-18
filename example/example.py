"""
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""

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
            LOGGER.info(f'{contents}')

        msg = f'{{"message":"file", "time":"{str(datetime.now())}"}}'
        with open(filename, 'w') as fout:
            fout.write(msg)

        wtr.upload('upload', filename)

        key2 = 'upload'
        with pycos.COSReader(config, bucket, key2) as cos_reader:
            contents = cos_reader.readlines()
            LOGGER.info(f'{contents}')

        bkts = adm.bucket_list()
        LOGGER.info('Bucket Listing...')
        LOGGER.info(f'{bkts}')

        cnts = adm.bucket_contents(bucket)
        LOGGER.info('Bucket Contents...')
        LOGGER.info(f'{cnts}')

        adm.bucket_content_delete(bucket, key1)
        adm.bucket_content_delete(bucket, key2)

        adm.bucket_delete(bucket)

        os.remove(filename)

    except pycos.COSClientError as client_err:
        LOGGER.error(client_err)


if __name__ == '__main__':
    main()
