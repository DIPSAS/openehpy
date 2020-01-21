import requests

class PyOpenEHR:
    def __init__(self, EHRStoreURL, responseEncoding = "utf-8-sig", verifySSLConnection = True):
        self.EHRStoreURL = EHRStoreURL
        self.responseEncoding = responseEncoding
        self.verifySSLConnection = verifySSLConnection

    def query(self, query, includeTags = []):
        response = requests.get(self.EHRStoreURL + "/openehr/v1/query/aql/?q=" + query, verify = self.verifySSLConnection)
        response.encoding = self.responseEncoding
        return response.json() if response.ok else raise_for_status()

if __name__ == '__main__':