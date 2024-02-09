# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
Contains ITBill API DAO implementations.
"""
from restclients_core.dao import DAO
from os.path import abspath, dirname
import os


class  ITBill_DAO(DAO):
    def service_name(self):
        return "itbill"

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def _custom_headers(self, method, url, headers, body):
        basic_auth = self.get_service_setting('BASIC_AUTH')
        if basic_auth is not None:
            return {"Authorization": "Basic {}".format(basic_auth)}

    def _edit_mock_response(self, method, url, headers, body, response):
        if "POST" == method or "PUT" == method:
            if response.status != 400:
                path = "{path}/resources/itbill/file{url}.{method}".format(
                    path=abspath(dirname(__file__)), url=url, method=method)

                try:
                    handle = open(path)
                    response.data = handle.read()
                    response.status = 200
                except IOError:
                    response.status = 404
