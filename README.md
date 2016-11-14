Light Movie Database
--------------------

We love watching movies, make lists for different emotions and times.

Current movie database sites became very complex and interaction between users are minimum. Our idea is to create social network on movies for movie lovers like us. Share ideas, follow professionals, reviewers and friends, review movies, make your playlists. Get notification when new movies added by your favorite director or in your lovely categories.

We are Movie Discussion Network.

Install
-------

 - Clone or download repository
 - Create environment: `virtualenv venv -p python3`
 - Migrate database: `python manage.py migrate`
 - Create custom settings in project root: `./local_settings.py`
 - Run test server: `python manage.py runserver`

Deployment
----------

- Install gunicorn: `pip install gunicorn`
- ...

LICENSE
-------

Copyright (C) 2016 Emin Mastizada
Copyright (C) 2016 Emre Eroglu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    
    See the LICENSE file for more details.
