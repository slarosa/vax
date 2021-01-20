[![license](https://img.shields.io/github/license/slarosa/vax.svg)](https://github.com/slarosa/vax/blob/main/LICENSE.md)
![vax](https://github.com/slarosa/vax/workflows/vax-github-actions/badge.svg)
[![Made With Love](https://img.shields.io/badge/Made%20With-Love-orange.svg)](https://github.com/chetanraj/awesome-github-badges)
<!--![visitor badge](https://visitor-badge.glitch.me/badge?page_id=slarosa.vax)-->


## News
:warning: Starting from 19 January 2021 the data is no longer updated as the dashboard has been turned off.

:o: New dashboard is available [here](https://www.governo.it/it/cscovid19/report-vaccini/).

# Vax data (Last update: 2021-01-18 22:12:06)

This repository contains the unofficial data scraped from the dashboard of the [government
page](https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9&fbclid=IwAR0xF1jrq3kDmC0Emy3bDC5sikCEQxdMYbGr0ZfqYxNuQC7jKaGVHmHD5nk). 


# Tree directories
```
 |-vax
 | |-LICENSE
 | |-requirements.txt
 | |-query.json
 | |-get_vax_data.py
 | |-README.md
 | |-.github
 | | |-workflows
 | | | |-vax.yml
 | |-data
 | | |-LAZ.csv
 | | |-VDA.csv
 | | |-PIE.csv
 | | |-BAS.csv
 | | |-TOS.csv
 | | |-SIC.csv
 | | |-LIG.csv
 | | |-EMR.csv
 | | |-PUG.csv
 | | |-PAB.csv
 | | |-ABR.csv
 | | |-MAR.csv
 | | |-PAT.csv
 | | |-MOL.csv
 | | |-CAM.csv
 | | |-CAL.csv
 | | |-VEN.csv
 | | |-LOM.csv
 | | |-FVG.csv
 | | |-SAR.csv
 | | |-UMB.csv
 | | |-vax_total.csv
 | | |-summary_vax_total.csv
 | | |-summary_vax_total_latest.csv
 | | |-summary_vax_total_today.csv
```

# Dataset
Format of CSV file (separator is comma and encoding is UTF-8)
| Field              | Description                    | Format                         | Example                        |
|--------------------|--------------------------------|--------------------------------|--------------------------------|
| TML_DTA_SOMM       | Somministration date           | date (YYYY-MM-DD)              | 2020-12-27                     |
| TML_VAX_FORNITORE  | Vaccine supplier               | string                         | PF/BT                          |
| TML_DES_STRUTTURA  | Medical facility               | string                         | "P.O. ""G. Mazzini"" - Teramo" |
| TML_AREA           | Name area                      | string                         | ABR                            |
| TML_FASCIA_ETA     | Age range                      | string                         | 20-29                          |
| TML_SESSO_M        | Male sex                       | integer                        | 1                              |
| TML_SESSO_F        | Female sex                     | integer                        | 4                              |
| TML_GRAVIDANZA     | Pregnant women                 | integer                        | 0                              |
| TML_CAT_OSS        | Social health worker category  | integer                        | 5                              |
| TML_CAT_PERSONALE  | Medical personnel category     | integer                        | 0                              |
| TML_CAT_RSA_OSPITI | Nursing homes category         | integer                        | 0                              |
| TML_CAT_ALTRO      | Other categories               | integer                        | 0                              |
| TML_DOSE_1         | First dose of vaccine          | integer                        | 5                              |
| TML_DOSE_2         | Booster dose of vaccine        | integer                        | 0                              |
| TML_TOT_SOMM       | Total somministrations         | integer                        | 5                              |
| TML_REGIONE        | Name of Region                 | string                         | Abruzzo                        |
| TML_NUTS           | NUTS code level 2              | string                         | ITF1                           |


There are others CSV files which conatin the aggregate data from [```vax_total.csv```](data/vax_total.csv):
* [```summary_vax_total.csv```](data/summary_vax_total.csv) (grouping by date)
* [```summary_vax_total_latest.csv```](data/summary_vax_total_latest.csv) (grouping by yesterday date)
* [```summary_vax_total_today.csv```](data/summary_vax_total_today.csv) (grouping by today date)

The aggregate CSV files have the following structure.

| Field              | Description                    | Format                         | Example                        |
|--------------------|--------------------------------|--------------------------------|--------------------------------|
| TML_DTA_SOMM       | Somministration date           | date (YYYY-MM-DD)              | 2020-12-27                     |
| TML_REGIONE        | Name of Region                 | string                         | Abruzzo                        |
| TML_NUTS           | NUTS code level 2              | string                         | ITF1                           |
| TML_SESSO_M        | Male sex                       | integer                        | 1                              |
| TML_SESSO_F        | Female sex                     | integer                        | 4                              |
| TML_GRAVIDANZA     | Pregnant women                 | integer                        | 0                              |
| TML_CAT_OSS        | Social health worker category  | integer                        | 5                              |
| TML_CAT_PERSONALE  | Medical personnel category     | integer                        | 0                              |
| TML_CAT_RSA_OSPITI | Nursing homes category         | integer                        | 0                              |
| TML_CAT_ALTRO      | Other categories               | integer                        | 0                              |
| TML_DOSE_1         | First dose of vaccine          | integer                        | 5                              |
| TML_DOSE_2         | Booster dose of vaccine        | integer                        | 0                              |
| TML_TOT_SOMM       | Total somministrations         | integer                        | 5                              |


# Note
The official open-data are available to this [repository](https://github.com/italia/covid19-opendata-vaccini).
