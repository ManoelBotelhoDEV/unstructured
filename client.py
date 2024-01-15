from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError

s = UnstructuredClient(api_key_auth="jP7OGSZ5Gy8bEZzQYlUpMvNi1BkM50")

filename = "contrato.pdf"

with open(filename, "rb") as f:
    # Note that this currently only supports a single file
    files=shared.Files(
        content=f.read(),
        file_name=filename,
	)

req = shared.PartitionParameters(
    files=files,
    # Other partition params
    strategy='ocr_only',
    languages=["por"],
)

try:
    resp = s.general.partition(req)
    print(resp.elements[0])
except SDKError as e:
    print(e)


#Example for out
# {
# 'type': 'UncategorizedText', 
# 'element_id': 'fc550084fda1e008e07a0356894f5816', 
# 'metadata': {
#   'filename': 'contrato.pdf', 
#   'filetype': 'application/pdf', 
#   'languages': ['por'], 
#   'page_number': 1
#   }
# }