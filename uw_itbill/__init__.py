# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.exceptions import DataFailureException
from uw_itbill.dao import  ITBill_DAO
import json


class ITBill(object):
    """
    The ITBill object has methods for getting information
    about accounts, courses, enrollments and users within
    Canvas
    """

    _url_base = '/api/x_unowr_subscriptn/provision/'

    def base_url(self, service):
        return f"{self._url_base}{service}"

    def get_resource(url):
        response = DAO.getURL(url, {'Accept': 'application/json'})

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        return json.loads(response.data)


    def post_resource(url, body):
        response = DAO.postURL(url, {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }, body)

        if response.status != 200:
            raise DataFailureException(url, response.status, response.data)

        return json.loads(response.data)
