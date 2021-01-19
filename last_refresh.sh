#!/bin/bash

url="https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9"

last_refresh=$(curl 'https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata?synchronous=true' \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0' \
    -H 'Accept: application/json, text/plain, */*' \
    -H 'Accept-Language: it,en-US;q=0.7,en;q=0.3' --compressed \
    -H 'X-PowerBI-ResourceKey: 388bb944-d39d-4e22-817c-90d1c8152a84' \
    -H 'Content-Type: application/json;charset=UTF-8' \
    -H 'Origin: https://app.powerbi.com' \
    -H 'DNT: 1' \
    -H 'Connection: keep-alive' \
    -H 'Referer: '"$url"'' \
    -H 'Pragma: no-cache' \
    -H 'Cache-Control: no-cache' --data-raw '{ "version": "1.0.0", "queries": [ { "Query": { "Commands": [ { "SemanticQueryDataShapeCommand": { "Query": { "Version": 2, "From": [ { "Name": "l", "Entity": "LastRefresh", "Type": 0 } ], "Select": [ { "Column": { "Expression": { "SourceRef": { "Source": "l" } }, "Property": "Datetime_UTC+1" }, "Name": "LastRefresh.Datetime_UTC+1" } ], "OrderBy": [ { "Direction": 1, "Expression": { "Column": { "Expression": { "SourceRef": { "Source": "l" } }, "Property": "Datetime_UTC+1" } } } ] }, "Binding": { "Primary": { "Groupings": [ { "Projections": [ 0 ] } ] }, "DataReduction": { "DataVolume": 3, "Primary": { "Window": {} } }, "Version": 1 } } } ] }, "QueryId": "", "ApplicationContext": { "DatasetId": "5bff6260-1025-49e0-8e9b-169ade7c07f9", "Sources": [ { "ReportId": "b548a77c-ab0a-4d7c-a457-2e38c2914fc6" } ] } } ], "cancelQueries": [], "modelId": 4280811 }' | jq -c '.results[0].result.data.dsr.DS[0].PH[0].DM0[].G0')

NEWDATETIME=date -r `expr $last_refresh / 1000` +"%Y-%m-%d %H:%M:%S"
# sed -i -E 's/[0-9]{4}-[0-9]{2}-[0-9]{2}.[0-9]{2}:[0-9]{2}:[0-9]{2}/$NEWDATETIME/g' README.md
perl -pi -e "s/[0-9]{4}-[0-9]{2}-[0-9]{2}.[0-9]{2}:[0-9]{2}:[0-9]{2}/$NEWDATETIME/" README.md