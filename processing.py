from ncbi.datasets.openapi import VirusApi as DatasetsVirusApi
from ncbi.datasets.openapi import ApiException as DatasetsApiException
from ncbi.datasets.openapi import ApiClient as DatasetsApiClient
import ncbi.datasets
import json
import jsonlines
import os
import csv
import zipfile
import pandas as pd
from pyfaidx import Fasta
from google.protobuf.json_format import ParseDict
import ncbi.datasets.v1alpha1.reports.virus_pb2 as virus_report_pb2
from collections import Counter
from datetime import datetime, timezone, timedelta


def download_sars_cov2_protein_dataset(zipfile_name: str):
    with DatasetsApiClient() as api_client:
        virus_api = DatasetsVirusApi(api_client)
        try:
            print('Begin download of virus protein data package ...')
            virus_protein_ds_download = virus_api.sars2_protein_download(
                'SPIKE',
                complete_only=True,
                host='human',
                include_annotation_type=['PROT_FASTA', 'CDS_FASTA'],
                _preload_content=False)

            with open(zipfile_name, 'wb') as f:
                f.write(virus_protein_ds_download.data)
            print(f'Download completed -- see {zipfile_name}')
        except DatasetsApiException as e:
            print(f'Exception when calling sars2_protein_download: {e}\n')

virus_api = ncbi.datasets.VirusApi(ncbi.datasets.ApiClient())
download_sars_cov2_protein_dataset('protein.zip')