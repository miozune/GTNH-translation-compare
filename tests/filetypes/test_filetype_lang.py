from gtnh_translation_compare.filetypes.filetype_lang import FiletypeLang
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property
import pytest

EN_US_RELPATH = "test/x/en_US.lang"
EN_US_CONTENT = "\n".join(
    [
        "#test",
        "test=test",
        "",
        "test2=test2=test2",
        "test3",
    ]
)
JA_JP_RELPATH = "test/x/ja_JP.lang"
JA_JP_CONTENT = "\n".join(
    [
        "#test",
        "test=テスト",
        "",
        "test2=テスト2=テスト2",
        "test3",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_lang() -> FiletypeLang:
    return FiletypeLang(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def ja_jp_filetype_lang() -> FiletypeLang:
    return FiletypeLang(JA_JP_RELPATH, JA_JP_CONTENT, Language.ja_JP)


def test__get_relpath(en_us_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.relpath == EN_US_RELPATH
    assert ja_jp_filetype_lang.relpath == JA_JP_RELPATH


def test__get_content(en_us_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.content == EN_US_CONTENT
    assert ja_jp_filetype_lang.content == JA_JP_CONTENT


def test__get_properties(en_us_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.properties == {
        "lang|test": Property("lang|test", "test", "test=test", 11, 15),
        "lang|test2": Property("lang|test2", "test2=test2", "test2=test2=test2", 23, 34),
    }
    assert ja_jp_filetype_lang.properties == {
        "lang|test": Property("lang|test", "テスト", "test=テスト", 11, 14),
        "lang|test2": Property("lang|test2", "テスト2=テスト2", "test2=テスト2=テスト2", 22, 31),
    }


def test_get_en_us_relpath(en_us_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.get_en_us_relpath() == EN_US_RELPATH
    assert ja_jp_filetype_lang.get_en_us_relpath() == EN_US_RELPATH


def test_get_ja_jp_relpath(en_us_filetype_lang: FiletypeLang, ja_jp_filetype_lang: FiletypeLang) -> None:
    assert en_us_filetype_lang.get_ja_jp_relpath() == JA_JP_RELPATH
    assert ja_jp_filetype_lang.get_ja_jp_relpath() == JA_JP_RELPATH
