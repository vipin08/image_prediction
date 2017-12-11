from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='Predict Images',
      url='https://github.com/vipin08/image_prediction',
      author='vipin08',
      author_email='vpnkumar.kumar1@gmail.com',
      license='MIT',
      packages=['image_prediction'],
      zip_safe=False)



from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='image_prediction',
      version='0.1',
      description='Image Prediction',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/vipin08/image_prediction',
      author='vipin08',
      author_email='vpnkumar.kumar1@gmail.com',
      license='MIT',
      packages=['image_prediction'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['funniest-joke=image_prediction.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)