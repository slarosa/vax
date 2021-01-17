# Vax data
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
 | | |-vax_total.csv
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
```

# Dataset
Format of CSV file (separator is comma)
| FIELD              | Format                         | Example                        |
|--------------------|--------------------------------|--------------------------------|
| TML_DTA_SOMM       | date (YYYY-MM-DD)              | 2020-12-27                     |
| TML_VAX_FORNITORE  | string                         | PF/BT                          |
| TML_DES_STRUTTURA  | string                         | "P.O. ""G. Mazzini"" - Teramo" |
| TML_AREA           | string                         | ABR                            |
| TML_FASCIA_ETA     | string                         | 20-29                          |
| TML_SESSO_M        | integer                        | 1                              |
| TML_SESSO_F        | integer                        | 4                              |
| TML_CAT_OSS        | integer                        | 5                              |
| TML_CAT_PERSONALE  | integer                        | 0                              |
| TML_CAT_RSA_OSPITI | integer                        | 0                              |
| TML_CAT_ALTRO      | integer                        | 0                              |
| TML_DOSE_1         | integer                        | 5                              |
| TML_DOSE_2         | integer                        | 0                              |
| TML_REGIONE        | string                         | Abruzzo                        |
| TML_NUTS           | string                         | ITF1                           |


# Note
The official open-data are available to this [repository](https://github.com/italia/covid19-opendata-vaccini).