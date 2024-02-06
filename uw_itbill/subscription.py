# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from uw_itbill import ITBill
from uw_itbill.models import Subscription


class Subscription(ITBill):

    _path_prefix = 'subscription/'

    def subscription_url(self, path=""):
        return self.base_url(f"{self._path_prefix}{path}")

    def get_subscription_by_worktag(self, worktag):
        url = self.url(f"worktag/{worktag}")

        json_data = self.get_resource(url)

        return Subscription.from_json(json_data)

    def get_subscriptions_by_worktags(self, worktags):
        url = self.url(f"worktags?worktags={','.join(worktags)}")

        subscriptions = []
        for sub in self.get_resource(url):
            json_data = Subscription.from_json(sub)
            subscriptions.append(json_data)

        return subscriptions

    def create_subscription(self, subscription):
        url = self.url()

        json_data = self.post_resource(url, subscription)

        return Subscription.from_json(json_data)
