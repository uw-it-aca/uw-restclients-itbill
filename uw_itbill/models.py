# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from restclients_core import models


class Budget(models.Model):
    ACTIVITY = "activity"
    COST_CENTER = "cost_center"
    GIFT = "gift"
    GRANT = "grant"
    PROGRAM = "program"
    PROJECT = "project"

    DRIVER_CHOICES = (
        (ACTIVITY, " Activity"),
        (COST_CENTER, "Cost Center"),
        (GIFT, "Gift"),
        (GRANT, "Grant"),
        (PROGRAM, "Program"),
        (PROJECT, "Project"),
    )

    budget_change = models.CharField(max_length=255)
    ab_percent = models.SmallIntegerField(default=0)
    ab_start_month = models.DateField()
    ab_end_month = models.DateField(null=True)
    driver_worktag_type = models.CharField(
        max_length=16m choices=DRIVER_CHOICES)
    company = models.CharField(max_length=32)
    cost_center_driver = models.CharField(max_length=255, null=True)
    resource_driver = models.CharField(max_length=255, null=True)
    activity_driver = models.CharField(max_length=255, null=True)
    gift_driver = models.CharField(max_length=255, null=True)
    grant_driver = models.CharField(max_length=255, null=True)
    program_driver = models.CharField(max_length=255, null=True)
    project_driver = models.CharField(max_length=255, null=True)
    cost_center_toggle = models.CharField(max_length=255, null=True)
    resource_toggle = models.CharField(max_length=255, null=True)
    activity = models.CharField(max_length=255, null=True)
    assignee = models.CharField(max_length=255, null=True)
    program_adhoc = models.CharField(max_length=255, null=True)
    grant_adhoc = models.CharField(max_length=255, null=True)
    other_worktags = models.CharField(max_length=255, null=True)

    def from_json(self, data):
        pass

    def to_json(self):
        pass


class Subscription(models.Model):
        DRAFT = "draft",
        PROVISIONING = "provisioning",
        DEPLOYED = "deployed",
        DEPROVISION = "deprovision",
        CLOSED = "closed",
        CANCELLED = "cancelled",

    LIFECYCLE_CHOICES = (
        (DRAFT, "Draft"),
        (PROVISIONING, "Provisioning"),
        (DEPLOYED, "Deployed"),
        (DEPROVISION, "Deprovision"),
        (CLOSED, "Closed"),
        (CANCELLED, "Cancelled"),
    )

    name = models.CharField(max_length=255)
    key_prefix = models.CharField(max_length=127)
    start_date = models.DateField()
    end_date = models.DateField()
    contact = models.CharField(max_length=127)
    contacts_additional = models.CharField(max_length=255)
    lifecycle_state = models.CharField(
        max_length=32, choices=LIFECYCLE_CHOICES)
    work_notes = models.CharField(max_length=255)
    updated_line_items = models.BooleanField(null=True)

    def from_json(self, data):
        """
        Deserialze Subscription model
        """
        pass

    def to_json(self):
        """
        Serialze Subscription model
        """
        pass


class Provision(models.Model):
    ANNUAL = "annual"
    ANNUAL_FIXED = "annual-fixed"
    MONTHLY = "monthly"
    MONTHLY_METERED = "monthly-metered"
    ONETIME = "onetime"
    QUARTER_FISCAL = "quarter-fiscal"

    BILL_SCHEDULE_CHOICES = (
        (ANNUAL, "Annual"),
        (ANNUAL_FIXED, "Annual-Fixed"),
        (MONTHLY, "Monthly"),
        (MONTHLY_METERED, "Monthly-Metered"),
        (ONETIME, "Onetime"),
        (QUARTER_FISCAL, "Quarter-Fiscal"),
    )

    sys_id = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    subscription = models.CharField(max_length=255)
    bill_schedule = models.CharField(
        max_length=16, choices=BILL_SCHEDULE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.CharField(max_length=255)

    def from_json(self, data):
        """
        Deserialze Subscription model
        """
        pass

    def to_json(self):
        """
        Serialze Subscription model
        """
        pass


class Quantity(model.Models):
     bill_comment = models.CharField(max_length=255)
     start_date = models.DateField()
     end_date = models.DateField()
     quantity = models.FloatField()

    def from_json(self, data):
        """
        Deserialze Subscription model
        """
        pass

    def to_json(self):
        """
        Serialze Subscription model
        """
        pass


