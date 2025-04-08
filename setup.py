#!/usr/bin/env python3

from setuptools import setup
import os
from glob import glob

package_name = 'rqt_embed_window'

setup(
    name=package_name,
    version='0.9.0',
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/ros2/*.launch.py')),
        # Include test files
        (os.path.join('share', package_name, 'test'), glob('test/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Sammy Pfeiffer',
    author_email='sammypfeiffer@gmail.com',
    maintainer='Sammy Pfeiffer',
    maintainer_email='sammypfeiffer@gmail.com',
    description='rqt_embed_window provides a GUI plugin to embed other windows',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rqt_embed_window = rqt_embed_window.RqtEmbedWindow:main',
        ],
    },
)
