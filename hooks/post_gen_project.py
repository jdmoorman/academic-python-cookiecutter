import subprocess


subprocess.call(['git', 'init'])
subprocess.call(['pre-commit', 'install'])

# Attempt to commit twice. First fails from commit hooks, second commits.
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# Push to github repository if it exists.
subprocess.call(['git', 'remote', 'add', 'origin', r'git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}.git'])
subprocess.call(['git', 'remote', '-v'])
subprocess.call(['git', 'push', '-u', 'origin', 'master'])