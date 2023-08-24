import codecs
from pprint import pprint
from xerparser.reader import Reader
from xerparser import *
import urllib.request
from urllib.request import urlopen
import io
from xerparser.reader import Reader





file = open('example.xer', "r", errors='ignore')


xer = Reader(file)


# BUILD ACT REFERENCE
act_ref = {}
for act in xer.activities:
    act_ref[act.id] = act

for prj in xer.projects:
    for wbs in prj.wbss:
        print(f"WBS: {wbs}")

        # order by start date
        act_list = wbs.activities
        act_list.sort(key=lambda x: x.start_date)

        print('')

        for act in act_list:
            dict_ref = act.get_tsv_dict()
            print("    Activity ID ", act.id ,"| ", act.task_code, " | driving_path_flag | ", dict_ref['driving_path_flag'], " | Pred | ", f"Start Date: {act.start_date} | End Date: {act.end_date} ", " | Activity Name | ", act.task_name, )

            print('')
            for pred in xer.relations.get_predecessors(act.id):
                pred_vals = pred.get_tsv()
                sub_act = act_ref[pred_vals[3]]

                print(f'        PRED | ACTIVITY ID {sub_act.task_code} | ACTIVITY NAME {sub_act.task_name} | RELATION TYPE {pred_vals[6]} | LAG {pred_vals[7]}')
                print('')


            for succ in xer.relations.get_successors(act.id):
                succ_vals = succ.get_tsv()
                sub_act = act_ref[succ_vals[3]]

                print(f'        SUCC | ACTIVITY ID {sub_act.task_code} | ACTIVITY NAME {sub_act.task_name} | RELATION TYPE {pred_vals[6]} | LAG {pred_vals[7]}')
                print('')


