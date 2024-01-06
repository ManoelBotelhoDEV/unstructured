# unstructured

Installing the Python SDK: You can install the core SDK using pip:

pip install unstructured
Plain text files, HTML, XML, JSON, and Emails are immediately supported without any additional dependencies.

If you need to process other document types, you can install the extras required by following the Full Installation

System Dependencies: Ensure the subsequent system dependencies are installed. Your requirements might vary based on the document types you’re handling:

libmagic-dev : Essential for filetype detection.

poppler-utils : Needed for images and PDFs.

tesseract-ocr : Essential for images and PDFs.

libreoffice : For MS Office documents.

pandoc : For EPUBs, RTFs, and Open Office documents.

Validating Installation
After installation, confirm the setup by executing the below Python code:

from unstructured.partition.auto import partition
elements = partition(filename="example-docs/eml/fake-email.eml")
If you’ve opted for the “local-inference” installation, you should also be able to execute:

from unstructured.partition.auto import partition
elements = partition("example-docs/layout-parser-paper.pdf")
If these code snippets run without errors, congratulations! Your unstructured installation is successful and ready for use.

The following section will cover basic concepts and usage patterns in unstructured. After reading this section, you should be able to:

Partitioning a document with the partition function.

Understand how documents are structured in unstructured.

Convert a document to a dictionary and/or save it as a JSON.
