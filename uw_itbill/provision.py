# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from uw_itbill import ITBill
from uw_itbill.models import Provision


class Provision(ITBill):

    _path_prefix = 'provision/'

    def url(self, path=""):
        return self.base_url(f"{self._path_prefix}{path}")

    def get_provision_by_remote_key(self, key_remote):
        url = self.url("key_remote/{key_remote}")

        json_data = self.get_resource(url)

        return Provision.from_json(json_data)

    def put_provision_by_remote_key(self, key_remote, provision):
        url = self.url("key_remote/{key_remote}")

        json_data = self.put_resource(url, data)

        return Provision.from_json(json_data)
