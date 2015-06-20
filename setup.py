from setuptools import setup

setup(
    name='slack_log_handler',
    version='0.2.2',
    author='Daniel Perez',
    author_email='daniel@claudetech.com',
    packages=['slack_log_handler'],
    url='https://github.com/claudetech/python-slack-log',
    license='LICENSE',
    description='Python Slack log handler using webhook',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ],
)
