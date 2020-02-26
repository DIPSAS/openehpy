# PyOpenEHR
PyOpenEHR is a simple *openEHR* endpoint interface intended to make results of AQL queries against a chosen openEHR-endpont available as pandas.DataFrames.

### Usage
To use PyOpenEHR, simply create an instance the class `PyOpenEHR`.

**Example of makeing a connection instance:**
```
connection = PyOpenEHR("http*://openehr-endpoint-url", "utf-8-sig", False)
```
Please note that in this example SSL connection verification is disabled by the setting of the last constructor parameter to `False`.

**Example of useage of a connection instance:**
```
response = connection.query(aql);
```
The response from each query will be availabe as a `pandas.DataFrame` if the query is successful, otherwise the response will be the response object returned by the provided endpoint.