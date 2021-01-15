import argparse
import os
import sys
import platform

class Installer(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super (Installer, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if (platform.system() == 'Linux'):
            if (values == 'nodejs'):
                print('install nodejs')
            elif (values == 'wget'):
                print ('install wget')
            elif (values == 'curl'):
                print('install curl')
            else:
                raise ValueError("try again")


parser.add_argument('nodejs', action=Installer, type=str)
parser.add_argument('wget', action=Installer, type=str)
parser.add_argument('curl', action=Installer, type=str)


args = parser.parse_args()
