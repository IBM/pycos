|travis-badge|_

.. |travis-badge| image:: https://travis-ci.com/IBM/pycos.svg?branch=master
.. _travis-badge: https://travis-ci.com/IBM/pycos/

=====
pycos
=====

Wrapper package around ``ibm_boto3`` to provide basic read/write capability
into cloud object store.

Prerequisites
---------------------------------

- Credentials to your instance of IBM Cloud Object Store. These are available from the IBM Cloud Object Store dashboard, *service credentials -> new credentials*. It takes the form:

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

- Region specifer (which region you are using) eg ``us-south``, ``eu-de`` ...
- This pycos package available locally, which can be installed either by:

  - ``python3 -m pip install --user git+https://github.com/IBM/pycos``
  - clone this repo,

    - ``python3 setup.py sdist`` followed by
    - ``python3 -m pip install --user dist/pycos-0.0.1.tar.gz``


Running the sample code`
-----------------------------

Copy the credentials (as described above) into ``example/config.json`` and add the following line, ``"endpoint" : "https://s3.eu-de.cloud-object-storage.appdomain.cloud"``
(assuming the region is eu-de).

.. code-block::

  cd example
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
  python3 example.py


Running the unit tests
-----------------------------

Copy the ``example/config.json`` file to the ``tests`` directory and run:

.. code-block::

  cd tests
  pytest test_pycos.py
