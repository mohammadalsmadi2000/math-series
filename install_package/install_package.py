import subprocess

def install_package(package_name):
    # Install package
    subprocess.run(['pip', 'install', package_name])

    # Update requirements.txt file
    with open('requirements.txt', 'a') as f:
        subprocess.run(['pip', 'freeze'], stdout=f)


install_package('pytest')