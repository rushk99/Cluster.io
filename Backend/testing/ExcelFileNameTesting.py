file_names_list = ["data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx",
                   "data/04SEP2019_600F-30min_BCS-RCS-1301.xlsx",
                   "data/05SEP2019_600F-02min_BCS-1152.xlsx",
                   "start/weird/structure/data/06NOV2019_Austemper-600defF-5min_BCS-1027",
                   "data/15JAN2020_Aust5min_BCS.xlsx",
                   "15JAN2020_Aust30Min_BCS.xlsx",
                   "data/19AUG2020_0515-2017-10601_Unprocessed_BCS-2118 MAP.xlsx",
                   "data/A365 CuCS T6 11-30-2018 1217.xlsx",
                   "data/Bulk WAAM of Puck 1.xlsx",
                   "data/UMass Ta As-Sprayed #1 Map.xlsx",
                   "data/UMass Ta As-Sprayed #2 Map"
                   ]

NUM_CHARACTER_TO_INCLUDE = 30

for file_name in file_names_list:
    start_index = file_name.rfind("/") + 1
    end_index = file_name.rfind(".")
    if end_index == -1:
        end_index = len(file_name)
    assert start_index < end_index
    new_string = file_name[start_index:end_index]
    if len(new_string) > NUM_CHARACTER_TO_INCLUDE:
        new_string = new_string[0:NUM_CHARACTER_TO_INCLUDE]
    print(new_string)

exit(0)
