
=====
pycos
=====

Wrapper package around ``ibm_botd3`` to provide basic read/write capibility
into cloud object store.

Prereq to run example/example.py,
---------------------------------

- json credentials file, (from the IBM Cloud Object Store dashboard, *service credentials -> new credentials*). It takes the form

.. code-block::

  {
    "apikey": "",
    "cos_hmac_keys": {
      "access_key_id": "",
      "secret_access_key": ""
    },
    "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
    "iam_apikey_description": "",
    "iam_apikey_name": "",
    "iam_role_crn": "",
    "iam_serviceid_crn": "",
    "resource_instance_id": ""
  }

- region specifer eg ``us-south``, ``eu-de`` ...
- pycos package installed. this can be installed either by

  - ``python3 -m pip install --user git+https://github.com/IBM/pycos``
  - clone this repo,

    - ``python3 setup.py sdist``
    - ``python3 -m pip install --user dist/pycos-0.0.1.tar.gz``


to run ``example/example.py``
-----------------------------

copy credentials into ``config.json`` and add the following line, ``"endpoint" : "https://s3.eu-de.cloud-object-storage.appdomain.cloud"``
giving,

.. code-block::

  cat config.json
  {
    "apikey": "xxx",
    "cos_hmac_keys": {
      "access_key_id": "xxx",
      "secret_access_key": "xxx"
    },
    "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
    "iam_apikey_description": "xxx",
    "iam_apikey_name": "xxx",
    "iam_role_crn": "xxx",
    "iam_serviceid_crn": "xxx",
    "resource_instance_id": "xxx",
    "endpoint" : "https://s3.eu-de.cloud-object-storage.appdomain.cloud"
  }
  cd example
  python3 example.py
