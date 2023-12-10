from gtnh_translation_compare.filetypes.filetype_gt_lang import FiletypeGTLang
from gtnh_translation_compare.filetypes.language import Language
from gtnh_translation_compare.filetypes.property import Property
import pytest

EN_US_RELPATH = "GregTech_US.lang"
EN_US_CONTENT = "\n".join(
    [
        "# Configuration file",
        "",
        "enablelangfile {",
        "    B:UseThisFileAsLanguageFile=false",
        "}",
        "",
        "",
        "languagefile {",
        "    S:test=test",
        "}",
        "",
    ]
)
JA_JP_RELPATH = "GregTech.lang"
JA_JP_CONTENT = "\n".join(
    [
        "# Configuration file",
        "",
        "enablelangfile {",
        "    S:Language=en_US",
        "    B:UseThisFileAsLanguageFile=true",
        "}",
        "",
        "",
        "languagefile {",
        "    S:test=テスト",
        "}",
        "",
    ]
)


@pytest.fixture(scope="module")
def en_us_filetype_gt_lang() -> FiletypeGTLang:
    return FiletypeGTLang(EN_US_RELPATH, EN_US_CONTENT)


@pytest.fixture(scope="module")
def ja_jp_filetype_gt_lang() -> FiletypeGTLang:
    return FiletypeGTLang(JA_JP_RELPATH, JA_JP_CONTENT, Language.ja_JP)


def test__get_relpath(en_us_filetype_gt_lang: FiletypeGTLang, ja_jp_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.relpath == EN_US_RELPATH
    assert ja_jp_filetype_gt_lang.relpath == JA_JP_RELPATH


def test__get_content(en_us_filetype_gt_lang: FiletypeGTLang, ja_jp_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.content == EN_US_CONTENT
    assert ja_jp_filetype_gt_lang.content == JA_JP_CONTENT


def test__get_properties(en_us_filetype_gt_lang: FiletypeGTLang, ja_jp_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.properties == {
        "gt-lang|    S:test": Property("gt-lang|    S:test", "test", "    S:test=test", 107, 111),
    }
    assert ja_jp_filetype_gt_lang.properties == {
        "gt-lang|    S:test": Property("gt-lang|    S:test", "テスト", "    S:test=テスト", 127, 130),
    }


def test_get_en_us_relpath(en_us_filetype_gt_lang: FiletypeGTLang, ja_jp_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.get_en_us_relpath() == EN_US_RELPATH
    assert ja_jp_filetype_gt_lang.get_en_us_relpath() == EN_US_RELPATH


def test_get_ja_jp_relpath(en_us_filetype_gt_lang: FiletypeGTLang, ja_jp_filetype_gt_lang: FiletypeGTLang) -> None:
    assert en_us_filetype_gt_lang.get_ja_jp_relpath() == JA_JP_RELPATH
    assert ja_jp_filetype_gt_lang.get_ja_jp_relpath() == JA_JP_RELPATH
