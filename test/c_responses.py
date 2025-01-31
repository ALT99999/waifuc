import pytest

from .responses import mock_responses_from_hf


@pytest.fixture(scope='session')
def anime_pictures_2girls():
    with mock_responses_from_hf('anime_pictures_2girls'):
        yield


@pytest.fixture(scope='session')
def anime_pictures_surtr():
    with mock_responses_from_hf('anime_pictures_surtr'):
        yield


@pytest.fixture(scope='session')
def atfbooru():
    with mock_responses_from_hf('atfbooru'):
        yield


@pytest.fixture(scope='session')
def danbooru():
    with mock_responses_from_hf('danbooru'):
        yield


@pytest.fixture(scope='session')
def duitang_nian():
    with mock_responses_from_hf('duitang_nian'):
        yield


@pytest.fixture(scope='session')
def duitang_nian_non_strict():
    with mock_responses_from_hf('duitang_nian_non_strict'):
        yield


@pytest.fixture(scope='session')
def e621_amiya():
    with mock_responses_from_hf('e621_amiya'):
        yield


@pytest.fixture(scope='session')
def e621_surtr():
    with mock_responses_from_hf('e621_surtr'):
        yield


@pytest.fixture(scope='session')
def e926_amiya():
    with mock_responses_from_hf('e926_amiya'):
        yield


@pytest.fixture(scope='session')
def e926_surtr():
    with mock_responses_from_hf('e926_surtr'):
        yield


@pytest.fixture(scope='session')
def gelbooru_2dogs():
    with mock_responses_from_hf('gelbooru_2dogs'):
        yield


@pytest.fixture(scope='session')
def gelbooru_surtr():
    with mock_responses_from_hf('gelbooru_surtr'):
        yield


@pytest.fixture(scope='session')
def huashi6_nian():
    with mock_responses_from_hf('huashi6_nian'):
        yield


@pytest.fixture(scope='session')
def hypnohub_2dogs():
    with mock_responses_from_hf('hypnohub_2dogs'):
        yield


@pytest.fixture(scope='session')
def hypnohub_surtr():
    with mock_responses_from_hf('hypnohub_surtr'):
        yield


@pytest.fixture(scope='session')
def konachan_2dogs():
    with mock_responses_from_hf('konachan_2dogs'):
        yield


@pytest.fixture(scope='session')
def konachan_net_2dogs():
    with mock_responses_from_hf('konachan_net_2dogs'):
        yield


@pytest.fixture(scope='session')
def konachan_net_surtr():
    with mock_responses_from_hf('konachan_net_surtr'):
        yield


@pytest.fixture(scope='session')
def konachan_surtr():
    with mock_responses_from_hf('konachan_surtr'):
        yield


@pytest.fixture(scope='session')
def lolibooru_2dogs():
    with mock_responses_from_hf('lolibooru_2dogs'):
        yield


@pytest.fixture(scope='session')
def lolibooru_surtr():
    with mock_responses_from_hf('lolibooru_surtr'):
        yield


@pytest.fixture(scope='session')
def paheal_surtr():
    with mock_responses_from_hf('paheal_surtr'):
        yield


@pytest.fixture(scope='session')
def pixiv_ranking_day():
    with mock_responses_from_hf('pixiv_ranking_day'):
        yield


@pytest.fixture(scope='session')
def pixiv_ranking_week_r18():
    with mock_responses_from_hf('pixiv_ranking_week_r18'):
        yield


@pytest.fixture(scope='session')
def pixiv_search_surtr():
    with mock_responses_from_hf('pixiv_search_surtr'):
        yield


@pytest.fixture(scope='session')
def pixiv_search_surtr_original():
    with mock_responses_from_hf('pixiv_search_surtr_original'):
        yield


@pytest.fixture(scope='session')
def pixiv_user_2864095():
    with mock_responses_from_hf('pixiv_user_2864095'):
        yield


@pytest.fixture(scope='session')
def pixiv_user_2864095_original():
    with mock_responses_from_hf('pixiv_user_2864095_original'):
        yield


@pytest.fixture(scope='session')
def rule34_2dogs():
    with mock_responses_from_hf('rule34_2dogs'):
        yield


@pytest.fixture(scope='session')
def rule34_surtr():
    with mock_responses_from_hf('rule34_surtr'):
        yield


@pytest.fixture(scope='session')
def safebooru():
    with mock_responses_from_hf('safebooru'):
        yield


@pytest.fixture(scope='session')
def safebooru_org_2dogs():
    with mock_responses_from_hf('safebooru_org_2dogs'):
        yield


@pytest.fixture(scope='session')
def safebooru_org_surtr():
    with mock_responses_from_hf('safebooru_org_surtr'):
        yield


@pytest.fixture(scope='session')
def sankaku_2dogs():
    with mock_responses_from_hf('sankaku_2dogs'):
        yield


@pytest.fixture(scope='session')
def sankaku_surtr():
    with mock_responses_from_hf('sankaku_surtr'):
        yield


@pytest.fixture(scope='session')
def sankaku_texas_yuri():
    with mock_responses_from_hf('sankaku_texas_yuri'):
        yield


@pytest.fixture(scope='session')
def tbib_2dogs():
    with mock_responses_from_hf('tbib_2dogs'):
        yield


@pytest.fixture(scope='session')
def tbib_surtr():
    with mock_responses_from_hf('tbib_surtr'):
        yield


@pytest.fixture(scope='session')
def wallhaven_id_105577():
    with mock_responses_from_hf('wallhaven_id_105577'):
        yield


@pytest.fixture(scope='session')
def wallhaven_surtr():
    with mock_responses_from_hf('wallhaven_surtr'):
        yield


@pytest.fixture(scope='session')
def xbooru_2dogs():
    with mock_responses_from_hf('xbooru_2dogs'):
        yield


@pytest.fixture(scope='session')
def xbooru_surtr():
    with mock_responses_from_hf('xbooru_surtr'):
        yield


@pytest.fixture(scope='session')
def yande_2dogs():
    with mock_responses_from_hf('yande_2dogs'):
        yield


@pytest.fixture(scope='session')
def yande_surtr():
    with mock_responses_from_hf('yande_surtr'):
        yield


@pytest.fixture(scope='session')
def zerochan_amiya_login():
    with mock_responses_from_hf('zerochan_amiya_login'):
        yield


@pytest.fixture(scope='session')
def zerochan_amiya_login_strict():
    with mock_responses_from_hf('zerochan_amiya_login_strict'):
        yield


@pytest.fixture(scope='session')
def zerochan_camilla_strict():
    with mock_responses_from_hf('zerochan_camilla_strict'):
        yield


@pytest.fixture(scope='session')
def zerochan_surtr():
    with mock_responses_from_hf('zerochan_surtr'):
        yield


@pytest.fixture(scope='session')
def zerochan_surtr_full():
    with mock_responses_from_hf('zerochan_surtr_full'):
        yield


@pytest.fixture(scope='session')
def zerochan_surtr_strict():
    with mock_responses_from_hf('zerochan_surtr_strict'):
        yield
