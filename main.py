from unstructured.ingest.interfaces import (
    FsspecConfig,
    PartitionConfig,
    ProcessorConfig,
    ReadConfig,
)
from unstructured.ingest.runner import S3Runner

from unstructured.chunking.title import chunk_by_title
from unstructured.staging.base import dict_to_elements

import os

diretorio_script = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = "fake-html.html"
caminhocompleto= os.path.join(diretorio_script, nome_arquivo)

from unstructured.partition.auto import partition
elements = partition(filename=caminhocompleto)

for element in elements:
    print(element)