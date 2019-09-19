from setuptools import setup, find_packages
import os

# Determine version
version_file = os.path.realpath(__file__)
version_file = os.path.join(version_file[:version_file.rfind("/")], "VERSION")
version = open(version_file).read().strip()

setup(name="openbase-rct",
      version=version,
      description="Robotics Coordinate Transform (python).",
      long_description="This library wraps the functionality of the tf2 library (originated from ROS) and supports communication over the RSB middleware. The ROS dependencies are minimised as good as possible.",
      author="Norman Koester",
      author_email="nkoester[at]techfak.uni-bielefeld.de",
      url="https://github.com/openbase/rct-python.git",
      download_url="TODO",
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      include_package_data=True,
      keywords=['transformation', 'coordinates', 'tf', 'tf2', 'rsb', 'openbase'],
      license="LGPLv3",
      classifiers=[
          'Development Status :: Beta',
          'Environment :: Console',
          'Environment :: Robotics/Cognitive Systems',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: Linux',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Markup :: XML'
      ],
      # 'Louie', 'suds', 'restlib',
      # non-standard requirements: openbase-rct, rsb-python
      install_requires=['pyrr', "openbase-type"])
