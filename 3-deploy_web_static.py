#!/usr/bin/python3
""" Fabric script that generates a .tgz
archive from the contents of the web_static """

import os
import datetime
from fabric.api import *
from fabric.network import ssh_config
from fabric.api import local, run, env, put

env.user = 'ubuntu'
env.hosts = ['54.210.88.105', '100.26.233.248']
env.key_filename = "/root/.ssh/school"
env.use_ssh_config = True


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
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        zip_name = archive_path.split('/')[-1]
        archive_split = archive_path.split('.')
        filename = archive_split[0].split('/')
        run("mkdir -p /data/web_static/releases/{}".format(filename[1]))
        unzip_tar = "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                     zip_name, filename[1])
        run(unzip_tar)
        rm_zipfile = "rm -rf /tmp/{}".format(zip_name)
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

    def deploy():
        """function used to full deployment an archive"""
        archive_file = do_pack()
        if archive_file is None:
            return False
        deployed_file = do_deploy(archive_file)
        return deployed_file
