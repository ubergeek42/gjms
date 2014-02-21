# [GJMS 0.2.1](http://hostagamejam.com)
> Bringing game jam hosting to everyone!

## The vision

Today more and more game jams are being hosted. But hosting game jams is *hard*.<br>
You have to write your own submission forms, backend code and all other management.<br>
After having hosted 3 game jams myself, I know how tedious this is.

The **Game Jam Management System** tries to change the status quo, by doing the heavy lifting for you.
It aims to provide a fully-featured backend for managing game jams, while allowing you to retain full control over what happens at the front.  

The ultimate version of GJMS is easy to setup, easy to use, yet very powerful.<br>
In short: **Game jam hosting for everyone!**


## Getting started

<h3 style="color: #B11;">This section is not yet implemented!</h3>
GJMS is implemented in Python. Thus, you need access to Python and pip to run it.<br>
You can run GJMS either via CGI or proxy. It is recommended to run via proxy and<br>this is the method explained here:

* Clone the repository to your web server: `git clone git://github.com/Folis/gjms.git`
* Setup a proxy on port 5000 via .htaccess:<br>
<code>RewriteEngine On
RewriteRule ^(.*)$ http://127.0.0.1:5000/path/to/repo/$1 [P]</code>
This'll proxy all requests to GJMS. You may also proxy only requests from a subfolder.

After you set up your proxy, go to [your-website.com/gjms-config/](#), which will guide you through a setup process to get all necessary data. After finishing the setup process you<br>
are ready to go!

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
Also be sure to write unit tests and check against exisiting (<span style="color: #B11;">pending</span>) tests.

#### General
* Set up a [virtualenv](https://pypi.python.org/pypi/virtualenv) to avoid unwanted dependencies.
* Pull requests should get reviewed within 12/24 hours. (Usuall at 1 p.m. or 10 p.m. CET.)
* Issues will be ultimately closed by **Folis (Richard Blechinger).**

## License
The **Game Jam Management System** is licensed under a BSD 3-clause license.<br>
Refer to the LICENSE file for detailed information.
