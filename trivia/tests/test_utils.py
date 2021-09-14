import os
import time

from django.conf import settings
from django.test import TestCase, override_settings
from factory.django import ImageField
from shutil import rmtree

from tablib import Dataset

from neptune.factories import SharedImageFactory
from neptune.settings.base import FIXTURE_DIR
from neptune.utils import make_imagefield_filepath


class MakeImageFieldFilePath(TestCase):
    def setUp(self):
        self.instance = SharedImageFactory(name='url')

    def test_uploading_filepath_not_existing(self):
        uploading_filename = make_imagefield_filepath('shared', self.instance, 'test_image.png')
        self.assertEqual(uploading_filename, 'shared/test_image.png')

    @override_settings(DEFAULT_FILE_STORAGE='django.core.files.storage.FileSystemStorage')
    def test_uploading_filepath_exists(self):
        SharedImageFactory(name='shock',
                           image=ImageField(filename='test_image.png'))
        uploading_filename = make_imagefield_filepath('shared', self.instance, 'test_image.png')
        self.assertRegex(uploading_filename, r'shared\/test_image-\d+\.png')

        rmtree(settings.MEDIA_ROOT)


def import_xls_data(resource, headers, data):
    xls_file_path = os.path.join(FIXTURE_DIR, 'data.xls')
    dataset = Dataset(*data, headers=headers)

    with open(xls_file_path, 'wb') as f:
        f.write(dataset.export('xls'))

    with open(xls_file_path, 'rb') as f:
        dataset = Dataset().load(f.read())
    os.remove(xls_file_path)

    try:
        return resource.import_data(dataset)
    except AttributeError:
        return resource.bulk_import_data(dataset)


def load_export_file(path, check_exist=None):
    if check_exist:
        while not os.path.exists(path):
            time.sleep(1)
    return Dataset().load(open(path, 'rb').read())
