from fabric.api import env, local, cd, run

env.hosts = ['iespuertodelacruz.es']


def deploy():
    local('git push')
    with cd('~/prince-aas'):
        run('git pull')
        run('pipenv install')
        run('stop.sh')
        run('start.sh')
