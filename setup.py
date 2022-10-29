from setuptools import setup


install_requires = [
    'starlette==0.14.2',
    'meliodas==1.1.8',
    'rocketchat==1.0.1',
    'hawk==1.2.8'
]


test_require = [
    'ipython==7.26.0',
    'pytest==6.2.4',
    'pytest-asyncio==0.15.1',
    'pytest-cov==2.12.1',
]

setup(
    name='security',
    version='1.1.5',
    packages=['security'],
    install_requires=install_requires,
    author='Danilo Vargas',
    dependency_links=[
        'https://github.com/dasouch/meliodas.git@v1.1.8#egg=meliodas',
        'https://github.com/dasouch/rocketchat-singleton.git@v1.0.1#egg=rocketchat',
        'https://github.com/dasouch/hawk.git@v1.2.8#egg=hawk'
    ]
)
