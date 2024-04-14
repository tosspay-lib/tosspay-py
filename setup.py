import setuptools

setuptools.setup(
    name="tosspay",
    version="0.0.1",
    license='APACHE-2.0',
    author="5-23",
    author_email="rustacean@5-23.dev",
    description="사업자 등록증 없이 결제 시스템을 만들수있는 파이썬 라이브러리",
    long_description=open('README.md').read(),
    url="https://github.com/tosspay-lib/tosspay-py",
    package_dir="tospay",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE-2.0 License",
    ],
)