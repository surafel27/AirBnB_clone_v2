#!/usr/bin/python3
""" Fabric script that generates a .tgz
archive from the contents of the web_static """

import os
import datetime
from fabric.api import local, run, env


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


def do_deploy(archive_path):
    """lets deploye the one we have just archived"""
    env.user = 'ubuntu'
    env.hosts = ['ubuntu@54.210.88.105', '100.26.233.248']
    env.key_filename = "/root/.ssh/id_rsa"
    env.use_ssh_config = True
    if not os.path.exists(archive_path):
        return False
    try:
        if not os.path.exists('/tmp/'):
            os.makedirs('/tmp')
        put(archive_paht, '/tmp/')
        archive_split = archive_path.split('.')
        filename = archive_split.split('/')
        unzip_tar = "tar -xzvf /tmp/{}.tgz".format(filename[1])
        run(unzip_tar)
        rm_zipfile = "rm -rf /tmp/{}.tgz".format(filename[1])
        run(rm_zipfile)
        mv_file = "mv /data/web_static/releases/{}/web_static/* \
                   /data/web_static/releases/{}".format(
                           filename[1], filename[1])
        run(mv_file)
        run("rm -rf /data/web_static/releases/{}/web_static".format(
             filename[1]))
        run("rm -rf /data/web_static/current")
        new_link = "ln -sf /data/web_static/releases/{} \
                    /data/web_static/current".format(filename[1])
        run(new_link)
        return True
    except:
        return False
