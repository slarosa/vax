# -*- coding: utf-8 -*-

"""
***************************************************************************
    get_vax_data.py
    ---------------------
    Date                 : Juanary 2021
    Copyright            : (C) 2021
    Email                : lrssvtml at gmail dot com
    Note                 : Originally developed from Sergio Vavassori
                           (https://github.com/svavassori)
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Salvatore Larosa'
__date__ = 'Juanary 2021'
__copyright__ = '(C) 2021'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import sys
import os
import csv
import json
import requests
import glob
import pandas as pd
from datetime import date, timedelta


AREA_MAP = {
  "ABR": ["Abruzzo", "ITF1"],
  "BAS": ["Basilicata", "ITF5"],
  "CAL": ["Calabria", "ITF6"],
  "CAM": ["Campania", "ITF3"],
  "EMR": ["Emilia-Romagna", "ITH5"],
  "FVG": ["Friuli Venezia Giulia", "ITH4"],
  "LAZ": ["Lazio", "ITI4"],
  "LIG": ["Liguria", "ITC3"],
  "LOM": ["Lombardia", "ITC4"],
  "MAR": ["Marche", "ITI3"],
  "MOL": ["Molise", "ITF2"],
  "PAB": ["P.A. Bolzano", "ITH1"],
  "PAT": ["P.A. Trento", "ITH2"],
  "PIE": ["Piemonte", "ITC1"],
  "PUG": ["Puglia", "ITF4"],
  "SAR": ["Sardegna", "ITG2"],
  "SIC": ["Sicilia", "ITG1"],
  "TOS": ["Toscana", "ITI1"],
  "UMB": ["Umbria", "ITI2"],
  "VDA": ["Valle d'Aosta", "ITC2"],
  "VEN": ["Veneto", "ITH3"],
}

# Converts the JSON output of a PowerBI query to a CSV file
def extract(area, output_dir):
    # input_json = read_json(input_file)
    input_json = get_raw_json(area=area)
    data = input_json["results"][0]["result"]["data"]
    dm0 = data["dsr"]["DS"][0]["PH"][0]["DM0"]
    columns_types = dm0[0]["S"]
    columns = map(
        lambda item: item["GroupKeys"][0]["Source"]["Property"]
        if item["Kind"] == 1 else item["Value"], data["descriptor"]["Select"])
    value_dicts = data["dsr"]["DS"][0].get("ValueDicts", {})

    reconstruct_arrays(columns_types, dm0)
    expand_values(columns_types, dm0, value_dicts)

    replace_newlines_with(dm0, "")
    output_file = '{}.csv'.format(os.path.join(output_dir, area))
    write_csv(output_file, columns, dm0)
    df = pd.read_csv(output_file)
    df = df.rename(columns={
        'M0': 'TML_SESSO_M',
        'M1': 'TML_SESSO_F',
        'M2': 'TML_GRAVIDANZA',
        'M3': 'TML_CAT_OSS',
        'M4': 'TML_CAT_PERSONALE',
        'M5': 'TML_CAT_RSA_OSPITI',
        'M6': 'TML_CAT_ALTRO',
        'M7': 'TML_DOSE_1',
        'M8': 'TML_DOSE_2',
        'M9': 'TML_TOT_SOMM',
    }, inplace=False)
    df['TML_DTA_SOMM'] = pd.to_datetime(df['TML_DTA_SOMM'], unit='ms')
    df['TML_REGIONE'] = AREA_MAP[area][0]
    df['TML_NUTS'] = AREA_MAP[area][1]
    df.to_csv(output_file, index=False)
    # df.to_json(output_file, orient="table", indent=4, index=False)


def get_raw_json(query=None, area="CAL"):
    url = 'https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata?synchronous=true'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-us',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'wabi-europe-north-b-api.analysis.windows.net',
        'Origin': 'https://app.powerbi.com',
        'Referer': 'https://app.powerbi.com/',
        'Content-Length': '2380',
        'Connection': 'keep-alive',
        'X-PowerBI-ResourceKey': '388bb944-d39d-4e22-817c-90d1c8152a84',
        'RequestId': '2fe09f8c-ba6e-0461-0d01-9d427028aba7',
        'ActivityId': '6bf4dd37-d0cb-a91b-5d29-4ccbb557a95d'
    }

    post_fields = { "version": "1.0.0", "queries": [ { "Query": { "Commands": [ { "SemanticQueryDataShapeCommand": { "Query": { "Version": 2, "From": [ { "Name": "t", "Entity": "TAB_MASTER", "Type": 0 } ], "Select": [ { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_DTA_SOMM" }, "Name": "TAB_MASTER.TML_DTA_SOMM" }, { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_VAX_FORNITORE" }, "Name": "TAB_MASTER.TML_VAX_FORNITORE" }, { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_COD_STRUTTURA" }, "Name": "TAB_MASTER.TML_COD_STRUTTURA" }, { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_DES_STRUTTURA" }, "Name": "TAB_MASTER.TML_DES_STRUTTURA" }, { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_AREA" }, "Name": "TAB_MASTER.TML_AREA" }, { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_FASCIA_ETA" }, "Name": "TAB_MASTER.TML_FASCIA_ETA" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_SESSO_M" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_SESSO_M)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_SESSO_F" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_SESSO_F)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_GRAVIDANZA" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_GRAVIDANZA)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_CAT_OSS" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_CAT_OSS)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_CAT_PERSONALE" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_CAT_PERSONALE)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_CAT_RSA_OSPITI" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_CAT_RSA_OSPITI)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_CAT_ALTRO" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_CAT_ALTRO)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_DOSE_1" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_DOSE_1)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_DOSE_2" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TML_DOSE_2)" }, { "Aggregation": { "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TOT_SOMM" } }, "Function": 0 }, "Name": "Sum(TAB_MASTER.TOT_SOMM)" } ], "Where": [ { "Condition": { "Comparison": { "ComparisonKind": 1, "Left": { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_DOSE_1" } }, "Right": { "Literal": { "Value": "0L" } } } } }, { "Condition": { "In": { "Expressions": [ { "Column": { "Expression": { "SourceRef": { "Source": "t" } }, "Property": "TML_AREA" } } ], "Values": [ [ { "Literal": { "Value":"\'" + area + "\'" } } ] ] } } } ] }, "Binding": { "Primary": { "Groupings": [ { "Projections": [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ] } ] }, "DataReduction": { "Primary": { "Top": { "Count": 30000 } } }, "Version": 1 } } } ] }, "QueryId": "", "ApplicationContext": { "DatasetId": "5bff6260-1025-49e0-8e9b-169ade7c07f9", "Sources": [ { "ReportId": "b548a77c-ab0a-4d7c-a457-2e38c2914fc6" } ] } } ], "cancelQueries": [], "modelId": 4280811 }

    r = requests.post(url, data=json.dumps(post_fields), headers=headers)
    print(r.status_code, r.reason)
    if r.status_code != 200:
        sys.exit()
        return dict()
    raw = json.loads(r.content)

    return raw


def read_json(file_name):
    with open(file_name) as json_config_file:
        return json.load(json_config_file)


def write_csv(output_file, columns, dm0):
    with open(output_file, "w") as csvfile:
        wrt = csv.writer(csvfile)
        wrt.writerow(columns)
        for item in dm0:
            wrt.writerow(item["C"])


def reconstruct_arrays(columns_types, dm0):
    # fixes array index by applying
    # "R" bitset to copy previous values
    # "Ø" bitset to null values
    lenght = len(columns_types)
    for item in dm0:
        currentItem = item["C"]
        if "R" in item:
            copyBitset = item["R"]
            deleteBitSet = item.get("Ø", 0)
            for i in range(lenght):
                if is_bit_set_for_index(i, copyBitset):
                    currentItem.insert(i, prevItem[i])
                elif is_bit_set_for_index(i, deleteBitSet):
                    currentItem.insert(i, None)
        prevItem = currentItem


def is_bit_set_for_index(index, bitset):
    return (bitset >> index) & 1 == 1


# substitute indexes with actual values
def expand_values(columns_types, dm0, value_dicts):
    for (idx, col) in enumerate(columns_types):
        if "DN" in col:
            for item in dm0:
                dataItem = item["C"]
                if isinstance(dataItem[idx], int):
                    valDict = value_dicts[col["DN"]]
                    dataItem[idx] = valDict[dataItem[idx]]


def replace_newlines_with(dm0, replacement):
    for item in dm0:
        elem = item["C"]
        for i in range(len(elem)):
            if isinstance(elem[i], str):
                elem[i] = elem[i].replace("\n", replacement)


def main():
    if len(sys.argv) == 2:
        for k in AREA_MAP.keys():
            extract(k, sys.argv[1])

        all_files = glob.glob(sys.argv[1] + "/*.csv")
        dfs = []
        for filename in all_files:
            if not os.path.basename(filename).startswith(("vax_", "summary_")):
                df_area = pd.read_csv(filename, index_col=None, header=0)
                dfs.append(df_area)
        df_total = pd.concat(dfs, axis=0, ignore_index=True)
        df_total.to_csv(os.path.join(sys.argv[1], 'vax_total.csv'), index=False)
        group_fields = ['TML_DTA_SOMM', 'TML_REGIONE', 'TML_NUTS']
        df_total.groupby(group_fields).sum().to_csv(os.path.join(sys.argv[1], 'summary_vax_total.csv'))
        df_total[df_total.TML_DTA_SOMM == (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")].groupby(
            group_fields).sum().to_csv(os.path.join(sys.argv[1], 'summary_vax_total_latest.csv'))
        df_total[df_total.TML_DTA_SOMM == date.today().strftime("%Y-%m-%d")].groupby(
            group_fields).sum().to_csv(os.path.join(sys.argv[1], 'summary_vax_total_today.csv'))
    else:
        sys.exit("Usage: python3 " + sys.argv[0] + " area output_dir", file=sys.stderr)


if __name__ == "__main__":
    main()
