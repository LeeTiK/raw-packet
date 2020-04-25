import raw_packet

import setuptools
import pkg_resources

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Environment :: MacOS X",
        "Intended Audience :: Education",
        "License :: Free For Educational Use",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Education",
        "Topic :: Security"
    ]


setuptools.setup(
    name="raw_packet", # Replace with your own username
    version=raw_packet.__version__,
    author=raw_packet.__author__,
    author_email=raw_packet.__email__,
    description="This project implements network protocols such as Ethernet ARP IPv4 UDP TCP DHCPv4 ICMPv4 IPv6 DHCPv6 ICMPv6 DNS MDNS on raw socket.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://raw-packet.github.io/",
    packages=setuptools.find_packages(),
    classifiers=classifiers,
    install_requires=[
        "netifaces", "ipaddress", "netaddr", "scapy", 
        "psutil", "prettytable", "distro", "xmltodict",
        "paramiko", "npyscreen", "pycryptodomex", "getmac", "colorama" 
    ],
    entry_points = {
        'console_scripts': [
            'apple_arp_dos=raw_packet.Scripts.Apple.apple_arp_dos:main',
            'apple_rogue_dhcp=raw_packet.Scripts.Apple.apple_rogue_dhcp:main'
        ],
    },
    python_requires='>=3.7',
    include_package_data=True,
)