# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

"""
Contains ITBill API DAO implementations.
"""
import os
from os.path import abspath, dirname

from restclients_core.dao import DAO


class ITBill_DAO(DAO):
    def service_name(self):
        return "itbill"

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]

    def _custom_headers(self, method, url, headers, body):
        basic_auth = self.get_service_setting('BASIC_AUTH')
        if basic_auth is not None:
            return {"Authorization": f"Basic {basic_auth}"}

    def _edit_mock_response(self, method, url, headers, body, response):
        if method in ["POST", "PUT"] and response.status != 400:
            for base_path in self.get_implementation()._get_mock_paths():
                path = f"{base_path}/itbill/file{url}.{method}"
                try:
                    with open(path, 'r') as handle:
                        response.data = handle.read()
                        response.status = 200
                    return
                except OSError:
                    response.status = 404
