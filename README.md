# [[![GJMS](http://hostagamejam.com/media/gjms-logo.png)](http://hostagamejam.com)](http://hostagamejam.com)
> v0.7.1-alpha - Bringing game jam hosting to everyone!

![alt text](https://api.travis-ci.org/Folis/gjms.png "TravisCI build status")

## The vision

Today more and more game jams are being hosted. But hosting game jams is *hard*.<br>
You have to write your own submission forms, backend code and all other management.<br>
After having hosted 3 game jams myself, I know how tedious this is.

The **Game Jam Management System** tries to change the status quo, by doing the heavy lifting for you.
It aims to provide a fully-featured backend for managing game jams, while allowing you to retain full control over what happens at the front.

The ultimate version of GJMS is easy to setup, easy to use, yet very powerful.<br>
In short: **Game jam hosting for everyone!**


## Getting started

GJMS is implemented in Python. Thus, you need access to Python and pip to run it.<br>
The ideal setup for GJMS is an Apache server with mod_rewrite activated.<br>
Linux preferred. I won't stop you from running it on Windows, though.<br>
<br>
These are the things you need to do:

* Clone the repository to your web server: `git clone git://github.com/Folis/gjms.git`
* Go to the path of the repo: `cd path/to/gjms`
* Resolve dependencies: `pip install -r project/requirements.txt`
* Setup a proxy to localhost on port 8196 via .htaccess:<br>
<code>RewriteEngine On<br>
RewriteRule ^(.*)$ http://127.0.0.1:8196/path/to/gjms/$1 [P]</code><br>
* Start GJMS with the included shell script: `./start`

You should be greeted by a little intro text and some server output telling you that it created an instance of itself.
After you set up your proxy, go to [your-website.com/gjms-config/](#), which will guide you through a setup process to get all necessary data. After finishing the setup process you are ready to go!

## Contributing

Contributions to GJMS are always welcome, however there are a few guidelines to the<br>process to keep the project organised. These are:

#### Formatting
* Code close to PEP-8 standards. ([PyLint](http://www.pylint.org/) is very helpful here.)
* Only use spaces for indentation
* Semi-colons are discouraged

#### Branching and git management
* Updates/commits before version 1.0 go to master. After we will go by the git flow model:
    - The master branch should be production ready at all times.
    - develop is for all features included in the next release.
    - Adding a new feature? Start a branch: **feature/gjms-[module]-[submodule]**<br>(for gjms.core.users this would be feature/gjms-core-users.)<br>
Also be sure to write unit tests and check against existing tests (see test/test.py).

#### General
* Set up a [virtualenv](https://pypi.python.org/pypi/virtualenv) to avoid unwanted dependencies.
* Pull requests should get reviewed within 12/24 hours. (Usually at 1 p.m. or 10 p.m. CET.)
* Issues will be ultimately closed by **Folis (Richard Blechinger).**

## License
The **Game Jam Management System** is licensed under a BSD 3-clause license.<br>
Refer to the LICENSE file for detailed information.
