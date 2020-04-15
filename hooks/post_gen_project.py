import subprocess
import os
import shutil
import yaml

MANIFEST = "manifest.yml"

def get_manifest():
    with open(MANIFEST) as manifest_file:
        manifest = yaml.safe_load(manifest_file)
    return manifest

def delete_resources_for_disabled_features(manifest):
    for feature in manifest['features']:
        if not feature['enabled']:
            print("removing resources for disabled feature {}...".format(feature['name']))
            for resource in feature['resources']:
                delete_resource(resource)
    print("cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

def create_git_repo(manifest):
    precommit_feature = next(d for d in manifest['features'] if d["name"] == "precommit")
    precommit_enabled = precommit_feature["enabled"]

    subprocess.call(['git', 'init'])

    if precommit_enabled:
        subprocess.call(['pre-commit', 'install'])

    if precommit_enabled:
        # Hooks will fail the first time around, so we try twice.
        subprocess.run(['git', 'add', '.'], capture_output=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], capture_output=True)

    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])

#     # Push to github repository if it exists.
#     subprocess.call(['git', 'remote', 'add', 'origin', r'git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_project_name }}.git'])
#     subprocess.call(['git', 'remote', '-v'])
#     subprocess.call(['git', 'push', '--set-upstream', 'origin', 'master'])

if __name__ == "__main__":
    manifest = get_manifest()
    delete_resources_for_disabled_features(manifest)
    create_git_repo(manifest)
