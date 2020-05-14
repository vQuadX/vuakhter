import pytest
from elasticsearch.client import IndicesClient, Elasticsearch


@pytest.fixture
def mocked_scan(mocker):
    def get_mocked_scan(response=None):
        mocked_scan = mocker.patch('elasticsearch_dsl.search.scan')
        return_value = None
        if response and response['hits'] and response['hits']['hits']:
            return_value = iter(response['hits']['hits'])
        mocked_scan.return_value = return_value
        return mocked_scan
    return get_mocked_scan


@pytest.fixture
def mocked_indices_get(mocker):
    mocked_indicies_get = mocker.patch.object(IndicesClient, 'get')
    mocked_indicies_get.return_value = {}
    return mocked_indicies_get


@pytest.fixture
def mocked_count(mocker):
    def get_mocked_count(count=0):
        mocked_count = mocker.patch.object(Elasticsearch, 'count')
        mocked_count.return_value = {'count': count}
        return mocked_count
    return get_mocked_count
