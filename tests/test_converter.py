#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File name: test_converter.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg and avconv.
#   Copyright 2015-2016 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module provides tests for converter.py module."""

import nose

from PyQt5.QtCore import QProcess

from videomorph.converter import converter
from videomorph.converter import media
from videomorph.converter import XMLProfile

conv = None


# Set of test for Converter class
def setup():
    """Function to setup the test."""
    xml_profile = XMLProfile()
    xml_profile.create_profiles_xml_file()
    xml_profile.set_xml_root()

    media_list = media.MediaList()

    media_file = media.MediaFile(
        file_path='Dad.mpg',
        conversion_profile=xml_profile.get_conversion_profile(
            profile_name='DVD',
            target_quality='DVD Fullscreen (4:3)'))

    media_list.add_file(media_file)
    global conv
    conv = converter.Converter()
    conv.start_encoding(cmd=media_file.get_conversion_cmd(output_dir='.'))


def teardown():
    """Function to clean after tests are done."""
    conv.process.close()
    conv.process.kill()


def test_is_running():
    """Test is_running."""
    assert conv.process.state() == QProcess.Starting


if __name__ == '__main__':
    nose.run()
