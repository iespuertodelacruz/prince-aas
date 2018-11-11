from fabric.api import env, local, cd, run

env.hosts = ['iespuertodelacruz.es']


def deploy():
    local('git push')
    with cd('~/web'):
        run('git pull')
        run('pipenv install')
        run('supervisorctl restart prince-aas')
