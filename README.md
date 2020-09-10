# openehpy
`openehpy` (pronounced: open-e-h-py) is a simple package for retrieving data
from an *openEHR* server through its openEHR REST API and AQL queries.
Results are transformed to a `pandas.DataFrame` for further analysis.


# Usage
To use openehpy, simply import it and use it from a script or similar like so

```python
from openehpy import client

openehr_server = client.server_connection("https://openehr-server","utf-8-sig")
aql = """
select
    o/data[at0001]/events[at0006]/time/value as datetime,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value/magnitude AS systolic,
    o/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value/magnitude AS diastolic
from
    composition c
        contains observation o[openEHR-EHR-OBSERVATION.blood_pressure.v1]
limit 5"""

response = openehr_server.query(aql)

print(response)

#                         datetime  systolic  diastolic
# 0  2017-02-07T18:18:33.932+01:00     130.0       85.0
# 1  2017-02-08T13:39:51.382+01:00     120.0       80.0
# 2  2017-02-10T02:02:11.825+01:00     100.0       55.0
# 3  2017-02-08T01:32:46.904+01:00     130.0       80.0
# 4  2016-06-02T15:28:25.247+02:00     140.0       80.0
```

If you want to disable SSL connection verification you can pass in `verifySSLConnection = False`

```
openehr_server = client.server_connection("https://openehr-server","utf-8-sig", verifySSLConnection = False)
```

when you create the openEHR server object for querying. 

If you want to add headers you can pass in `headers = {"key":"value"}`

```
openehr_server = client.server_connection("https://openehr-server", headers = {"key":"value"})
```
If you want to add auth you can pass in ` auth=('user','pass')`

```
openehr_server = client.server_connection("https://openehr-server", auth=('user','pass'))
```

# Build and install 

To build and install this package simply run 

```
    python3 -m pip install .
```

in the root folder of this repository.
