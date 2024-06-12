# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core.util.decorators import use_mock
from uw_itbill.dao import ITBill_DAO


fdao_itbill_override = use_mock(ITBill_DAO())
