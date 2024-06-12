# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
from uw_itbill.tests import fdao_itbill_override
from uw_itbill.subscription import Subscription


@fdao_itbill_override
class ITBillTestSubscriptionData(TestCase):
    def test_get_by_sis_id(self):
        sys_id = '0123456789abcdef0123456789abcdef'
        subscription = Subscription().get_subscription_by_sys_id(sys_id)

        self.assertEqual(subscription.sys_id, sys_id)
