from distutils.core import setup, Extension
import subprocess
subprocess.run(["pandoc","--from=markdown","--to=rst","--output=README","README.md"])

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'SnykVulndb',
  packages = ['SnykVulndb'],
  version = '0.1',
  license='MIT',
  description = 'This library used for searching cve by package name and version using SNYK database. Basically it parse HTML from SNYK page',
  long_description=long_description,
  author = 'Aryya Widigdha',
  author_email = 'aryya.widigdha@yahoo.com',
  url = 'https://github.com/adwisatya/SnykVulndb',
  download_url = 'https://github.com/adwisatya/SnykVulndb/archive/refs/tags/v0.1.tar.gz',
  keywords = ['cve','snyk','snyk api'],
  install_requires=[
          'requests',
          'lxml.html',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
