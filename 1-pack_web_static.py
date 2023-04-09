#!/usr/bin/python3
""" Fabric script that generates a .tgz
archive from the contents of the web_static """

import os
import datetime
from fabric.api import local


def do_pack():
    """function makest tar file"""
    c_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "versions/web_static_{}.tgz".format(c_time)
    if not os.path.exists('versions'):
       os.makedirs("versions")
    print("Packing web_static to {}".format(archive_name))
    archive_file_tar = "tar -czvf {} web_static".format(archive_name)
    archive_file = local(archive_file_tar)
    if archive_file.failed:
        return None
    return archive_name
