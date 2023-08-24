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


class OBS:
    obj_list = []

    def __init__(self, params):
        # Unique ID generated by the system.
        self.obs_id = int(params.get('obs_id').strip()) if params.get('obs_id') else None
        # The parent OBS value in the OBS hierarchy.
        self.parent_obs_id = int(params.get('parent_obs_id').strip()) if params.get('parent_obs_id') else None
        # Global Unique Identifier generated by the system.
        self.guid = params.get('guid').strip() if params.get('guid') else None
        # Sequence number used for sorting.
        self.seq_num = int(params.get('seq_num').strip()) if params.get('seq_num') else None
        # The name of the person/role in the organization.
        self.obs_name = params.get('obs_name').strip() if params.get('obs_name') else None
        # The description of the person/role in the organization.
        self.obs_descr = params.get('obs_descr').strip() if params.get('obs_descr') else None

        OBS.obj_list.append(self)

    def get_tsv(self):
        tsv = ['%R', self.obs_id, self.parent_obs_id, self.guid, self.seq_num,
               self.obs_name, self.obs_descr]
        return tsv
    @classmethod
    def get_json(cls):
        root_nodes = list(filter(lambda x: x.parent_obs_id is None, cls.obj_list))
        # print(root_nodes)
        json = dict()
        for node in root_nodes:
            json["node"] = node
            json["level"] = 0
            json["childs"] = cls.get_childs(node, 0)
        print(json)

    @classmethod
    def get_childs(cls, node, level):
        nodes_lst = list(filter(lambda x: x.parent_obs_id == node.obs_id, cls.obj_list))
        nod = dict()
        for node in nodes_lst:
            nod["node"] = node
            nod["level"] = level + 1
            children = cls.get_childs(node, level+1)
            nod["childs"] = children if children else []
        return nod

    def get_id(self):
        return self.obs_id

    @classmethod
    def find_by_id(cls, id):
        obj = list(filter(lambda x: x.obs_id == id, cls.obj_list))
        if obj:
            return obj[0]
        return obj

    def __repr__(self):
        return self.obs_name
