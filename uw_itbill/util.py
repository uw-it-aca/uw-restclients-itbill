# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime, timedelta
from dateutil.parser import parse
from restclients_core.util.decorators import use_mock
from uw_itbill.dao import ITBill_DAO

fdao_itbill_override = use_mock(ITBill_DAO())


def str_to_datetime(s):
    return parse(s) if (s is not None and len(s)) else None


def str_to_date(s):
    dt = str_to_datetime(s)
    return dt.date() if dt is not None else None


def date_to_str(dt):
    # datetime.datetime.isoformat
    return dt.isoformat() if dt is not None else None


def date_to_month(dt):
    return dt.strftime("%Y-%m") if dt is not None else None
