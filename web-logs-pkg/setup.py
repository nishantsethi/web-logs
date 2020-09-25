from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = 'A python package to views live logs of any application(s) \
    on browser. Uses Flask to put pages on the web.' 
  
setup( 
        name ='weblogs', 
        version ='1.0.2', 
        author ='Nishant Sethi', 
        author_email ='sethi.nishant43@gmail.com', 
        url ='https://github.com/nishantsethi/web-logs', 
        description ='A Python Package to view stream of logs', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(),
        package_data={'web-logs': ['data/index.html']},
        entry_points ={ 
            'console_scripts': [ 
                'web-logs = web_logs.web_logs:main'
            ] 
        }, 
        classifiers =[
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ], 
        keywords ='python web-logs logs browser logs-stream', 
        install_requires = requirements, 
        zip_safe = False
) 