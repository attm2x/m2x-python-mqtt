from setuptools import setup


version = __import__('m2x_mqtt').version

LONG_DESCRIPTION = """
AT&T's M2X is a cloud-based fully managed data storage service for network
connected machine-to-machine (M2M) devices. python-m2x-mqtt is python client to
M2X MQTT API. API documentation at https://m2x.att.com/developer/documentation
"""

setup(
    name='m2x-mqtt',
    version=version,
    author='Citrusbyte',
    author_email='matia.saguirre@citrusbyte.com',
    description='M2X Python API client',
    license='BSD',
    keywords='m2x, mqtt, api',
    url='https://github.com/attm2x/m2x-python-mqtt',
    packages=[
        'm2x_mqtt',
        'm2x_mqtt.v2'
    ],
    long_description=LONG_DESCRIPTION,
    install_requires=[
        'iso8601==0.1.8',
        'paho-mqtt==1.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3'
    ],
    zip_safe=False
)
