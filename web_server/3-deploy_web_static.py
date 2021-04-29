#!/usr/bin/python3
"""
This module uses fabric to
deploy files to a server
"""


from fabric.api import env, run, put, local
from datetime import datetime
import os


env.hosts = ['35.196.163.39', '35.185.33.80']


def do_pack():
    """ Create directory and compress file
        as a given name
    """
    time_test = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_" + time_test + ".tgz"
    command1 = "mkdir -p versions"
    command2 = "tar -czvf " + file_name + " web_static"
    local(command1)
    com = local(command2)
    if com.return_code == 0:
        return file_name
    else:
        return None


def do_deploy(archive_path):
    """ This function takes the path of the archive
        and uploads it to the servers
    """
    if not os.path.exists(archive_path):
        return False

    file_ext = archive_path[archive_path.find('/') + 1:]
    file_name = archive_path[archive_path.find('/') + 1: -4]

    result = put(archive_path, '/tmp/' + file_ext)
    if result.failed:
        return False

    result = run('mkdir -p /data/web_static/releases/' + file_name + '/')
    if result.failed:
        return False

    result = run('tar -xzf /tmp/' + file_ext +
                 ' -C /data/web_static/releases/' + file_name + '/')
    if result.failed:
        return False

    result = run('rm /tmp/' + file_ext)
    if result.failed:
        return False

    result = run('mv /data/web_static/releases/' + file_name +
                 '/web_static/* /data/web_static/releases/' + file_name + '/')
    if result.failed:
        return False

    result = run('rm -rf /data/web_static/releases/' + file_name +
                 '/web_static')
    if result.failed:
        return False

    result = run('rm -rf /data/web_static/current')
    if result.failed:
        return False

    result = run('ln -s /data/web_static/releases/' +
                 file_name + '/ /data/web_static/current')
    if result.failed:
        return False

    print('New version deployed!')
    return True


def deploy():
    """ This function deploys a web to a server
    """
    archive_path = do_pack()
    if archive_path is False:
        return false

    deploy_return = do_deploy(archive_path)
    return deploy_return
