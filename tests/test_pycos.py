"""Tests for pycos
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

import os
import pytest
import pycos


def config_fetch():
    import json

    cfg = os.environ.get('PYCOSCONFIG')
    if cfg is not None:
        jsn = json.loads(cfg)
        return jsn

    if cfg is None:
        try:
            with open('config.json') as jsn_file:
                jsn = json.load(jsn_file)
                return jsn
        except:
            return None

@pytest.fixture
def yield_config_bucket_objectname():
    config = config_fetch()

    import uuid
    bucket = str(uuid.uuid4())
    objectname = str(uuid.uuid4())

    adm = pycos.COSAdmin(config)
    adm.bucket_create(bucket)

    yield (config, bucket, objectname)

    adm.bucket_content_delete(bucket, objectname)
    adm.bucket_delete(bucket)


def test_store_inmem_and_fetch(yield_config_bucket_objectname):
    config, bucket, objectname = yield_config_bucket_objectname

    from datetime import datetime
    msg = f'{{"message":"inmem", "time":"{str(datetime.now())}"}}'

    wtr = pycos.COSWriter(config, bucket)
    wtr.store(objectname, msg)

    key1 = objectname
    with pycos.COSReader(config, bucket, key1) as cos_reader:
        contents = cos_reader.readlines()
        print(f'{contents}')

    assert contents[0] == msg


@pytest.fixture
def yield_config_bucket_filename_msg_objectname():
    config = config_fetch()

    import uuid
    bucket = str(uuid.uuid4())
    filename = str(uuid.uuid4())
    objectname = str(uuid.uuid4())

    from datetime import datetime
    msg = f'{{"message":"file", "time":"{str(datetime.now())}"}}'

    with open(filename, 'w') as fout:
        fout.write(msg)

    adm = pycos.COSAdmin(config)
    adm.bucket_create(bucket)

    yield (config, bucket, filename, msg, objectname)

    os.remove(filename)
    adm.bucket_content_delete(bucket, objectname)
    adm.bucket_delete(bucket)


def test_upload_file_and_fetch(yield_config_bucket_filename_msg_objectname):
    config, bucket, filename, msg, objectname = yield_config_bucket_filename_msg_objectname

    wtr = pycos.COSWriter(config, bucket)
    wtr.upload(objectname, filename)

    key2 = objectname
    with pycos.COSReader(config, bucket, key2) as cos_reader:
        contents = cos_reader.readlines()
        print(f'{contents}')

    assert contents[0] == msg
