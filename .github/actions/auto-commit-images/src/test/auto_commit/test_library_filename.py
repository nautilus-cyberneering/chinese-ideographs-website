import pytest

from auto_commit.library_filename import LibraryFilename


def test_base_image_type_check():
    filename = LibraryFilename("000002-42.600.2.tif")
    assert filename.is_base_image() == True
