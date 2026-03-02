# REST client for UW IT Bill API

[![Build Status](https://github.com/uw-it-aca/uw-restclients-itbill/workflows/tests/badge.svg)](https://github.com/uw-it-aca/uw-restclients-itbill/actions)
[![Coverage Status](https://coveralls.io/repos/github/uw-it-aca/uw-restclients-itbill/badge.svg?branch=main)](https://coveralls.io/github/uw-it-aca/uw-restclients-itbill?branch=main)
[![PyPi Version](https://img.shields.io/pypi/v/uw-restclients-itbill.svg)](https://pypi.python.org/pypi/uw-restclients-itbill)
![Python versions](https://img.shields.io/badge/python-3.12-blue.svg)

To use this client, you'll need these settings in your application or script:

    # Specifies whether requests should use live or mocked resources,
    # acceptable values are 'Live' or 'Mock' (default)
    RESTCLIENTS_ITBILL_DAO_CLASS='Live'

    # Values for authentication credentials
    RESTCLIENTS_ITBILL_BASIC_AUTH=<base64-encoded-credentials>

    # ITBill API hostname (test or production)
    RESTCLIENTS_ITBILL_HOST='https://server.washington.edu'
