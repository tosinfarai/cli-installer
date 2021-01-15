import argparse
import platform
import os

class Installer(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super (Installer, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if (values == 'nodejs'):
            if (platform.system() == 'Linux'):
                os.system('sudo apt-get install nodejs')
            elif (platform.system() == 'Windows'):
                os.system('scoop install nodejs')
            elif (platform.system() == 'Darwin'):
                os.system('brew install node')
            else:
                print('unrecognized OS')

        elif (values == 'wget'):
            if (platform.system() == 'Linux'):
                os.system('sudo apt-get install wget')
            elif (platform.system() == 'Windows'):
                os.system('scoop install wget')
            elif (platform.system() == 'Darwin'):
                os.system('brew install wget')
            else:
                print('unrecognized OS')

        elif (values == 'curl'):
            if (platform.system() == 'Linux'):
                os.system('sudo apt-get install curl')
            elif (platform.system() == 'Windows'):
                os.system('scoop install curl')
            elif (platform.system() == 'Darwin'):
                os.system('brew install curl')
            else:
                print('unrecognized OS')

        else:
            print("Error: Argument Unknown. Try 'nodejs', 'wget' or 'curl'")


parser = argparse.ArgumentParser()
parser.add_argument('--install', action=Installer, type=str)

args = parser.parse_args()
