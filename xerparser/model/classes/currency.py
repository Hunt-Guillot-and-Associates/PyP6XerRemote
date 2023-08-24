# PyP6XER
# Copyright (C) 2020, 2021 Hassan Emam <hassan@constology.com>
#
# This file is part of PyP6XER.
#
# PyP6XER library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License v2.1 as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyP6XER is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyP6XER.  If not, see <https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html>.


class Currency:
    obj_list = []

    def __init__(self, params):
        # Unique ID generated by the system.
        self.curr_id = int(params.get('curr_id')) if params.get('curr_id') else None
        # The number of decimal places displayed.
        self.decimal_digit_cnt = int(params.get('decimal_digit_cnt')) if params.get('decimal_digit_cnt') else None
        # The symbol used to identify each defined currency.
        self.curr_symbol = params.get('curr_symbol') if params.get('curr_symbol') else None
        # The decimal symbol displayed.
        self.decimal_symbol = params.get('decimal_symbol').strip() if params.get('decimal_symbol') else None
        # The symbol used to group the numbers.
        self.digit_group_symbol = params.get('digit_group_symbol').strip() if params.get('digit_group_symbol') else None
        # The symbol used to display a positive currency.
        self.pos_curr_fmt_type = params.get('pos_curr_fmt_type').strip() if params.get('pos_curr_fmt_type') else None
        # The symbol used to display a negative currency.
        self.neg_curr_fmt_type = params.get('neg_curr_fmt_type').strip() if params.get('neg_curr_fmt_type') else None
        # The names of all defined currencies.
        self.curr_type = params.get('curr_type').strip()
        # The identifiers for all currencies defined in Project Management.
        self.curr_short_name = params.get('curr_short_name').strip() if params.get('curr_short_name') else None
        # Currency Group Digit Count
        self.group_digit_cnt = params.get('group_digit_cnt').strip()
        # The current exchange rate between the selected currency and the base currency.
        self.base_exch_rate = params.get('base_exch_rate').strip() if params.get('base_exch_rate') else None

        Currency.obj_list.append(self)

    def get_id(self):
        return self.curr_id

    def get_tsv(self):
        tsv = ['%R', self.curr_id, self.decimal_digit_cnt, self.curr_symbol, self.decimal_symbol,
               self.digit_group_symbol, self.pos_curr_fmt_type, self.neg_curr_fmt_type,
               self.curr_type, self.curr_short_name, self.group_digit_cnt, self.base_exch_rate]
        return tsv
    @classmethod
    def find_by_id(cls, id):
        obj = list(filter(lambda x: x.curr_id == id, cls.obj_list))
        if obj:
            return obj[0]
        return obj

    def __repr__(self):
        return self.curr_short_name + ' ' + str(self.curr_type)