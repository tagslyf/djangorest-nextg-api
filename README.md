# Technology stack #

### Language: Python 2.7 ###

### Database: Postgres ###

Currently runs on an RDS instance

### Major Libraries: Django 1.10, Django REST Framework ###

### Continuous Integration: Bitbucket Pipelines ###

Currently supports running unit tests and flake8 checking for Pep 8.

TODO: add jmeter tests

TODO: add code coverage

### Authentication ###

Possible options:

-   Oauth2
-   jwt

### Push notifications ###

Text goes here

### Asynchonous jobs ###

Text goes here

### Caching: ###

Do we want a standalone server?

Pros:
-   If we horizontally scale application servers then we will want a standalone redis server to easily invalidate the cache

Cache backends:
-   Redis
    -   Pros:
        -   Development Team has most experience with this
            Persistence to disk, by default [Source](http://stackoverflow.com/questions/10558465/memcached-vs-redis)
    -   CONS:
        -   Limited to one core as it is based on an event loop [Source](http://stackoverflow.com/questions/10558465/memcached-vs-redis)
-   Memcache
    -   Pros:
        -   Multithreaded and fast [Source](<http://stackoverflow.com/questions/10558465/memcached-vs-redis>)
        
"Because Redis is newer and has more features than Memcached, Redis is almost always the better choice. However, Memcached could be preferable when caching relatively small and static data, such as HTML code fragments." 
"Redis focuses on adding more features"
"Memache focuses on stability"
"memcache is easier to scale because it is multi threaded. Redis has to be scaled horizontally"
"Last but not least, in terms of operational visibility, Redis provides a slew of metrics and a wealth of introspective commands with which to monitor and track usage and abnormal behavior." 
[source](http://www.infoworld.com/article/3063161/application-development/why-redis-beats-memcached-for-caching.html)
        
Reverse Proxy Cache: 
-   Varnish
-   Nginx
-   Apache

### Load Balancer: ###

Possible Options:

-   AWS
-   nginx


### Real Time ###

Possible Options: 

-   Django-channels
-   Socket.io

### Web Accelerator: ###

Possible Options:

-   Apache
-   Nginx

### WSGI Interface: ###

Possible options:

-   uWSGI
-   gunicorn

### Searching ###

Possible Options:

-   Elastic Search
-   Cloud Search
-   Django ORM

### DNS ###

AWS

TODO: Add DNS details

### SSL Implementation ###

ACM (Amazon Certificate Manager)

### Monitoring ###

Text goes here

##### Logging #####

Text goes here

##### Alerts #####

Text goes here

### Email ###

Text goes here

### Front End Admin ###

Possible Options:

-   Django Admin
    -   Pros:
        -   Rapid development, easy to maintain
    -   Cons:
        -   Possible flexibility issues

-   AngularJS
    -   Pros:
        -   More customizable
    -   Cons:
        -   Have to write and maintain client and server validation separately
        possibilities:
        somehow get angular to infer validation constraints from the APIs metadata
        possibly this? http://glynjackson.org/weblog/tutorial-using-angularjs-django/
        somehow get django admin to send back the form templates which are then compiled by angularjs

-   Pure Django
    -   Pros:
        -   Sync form validation with model via modelforms
        -   We have to create an API anyway for mobile front ends, may as well make admin use an API also
    -   Cons:
        -   not as powerful frontend logic as angular

do we want to put it on a separpate server? S3? cloudfront?

# Backups #

Text goes here

# Coding Standards #

### Python ###

[PEP 8](https://www.python.org/dev/peps/pep-0008/)

[Django 1.10 Coding Style](https://docs.djangoproject.com/el/1.10/internals/contributing/writing-code/coding-style/)

[PEP 20](https://www.python.org/dev/peps/pep-0020/)

What max line length do we want to use? I think 79 is too small. How about we relax the hard limit to 99 characters and keep comments and docstrings to 72? (recommended by PEP 8)

avoid wildcard importsto avoid import conflicts and improve code introspection tools functionality

use explicity relative imports instead of absolute imports to keep apps easily movable

    

### Patterns ###

Test Driven Development

Write / update a test for every change you make to the application *before* you make the change. Only write code when there is a test failing for it. No cheating!

1. Write the test
2. Run the test (there is no implementation code, test does not pass)
3. Write just enough implementation code to make the test pass
4. Run all tests (tests pass)
5. Refactor
6. Make sure tests still pass
7. Repeat

Generally there should be at least one test for each function, plus one for each if statement inside the function.

Avoid fixtures for they are hard to maintain as the project evolves and data structures change. Use factory boy instead.

Use descriptive names for test methods for they help document the codebase.

Each test should only test one thing. Don't be afraid to break a test into multiple tests. DRY (Do not Repeat Yourself) principle does not apply for unit tests.


Fat models [source](http://django-best-practices.readthedocs.io/en/latest/applications.html)

A common pattern in MVC-style programming is to build thick/fat models and thin controllers. For Django this translates to building models with lots of small methods attached to them and views which use those methods to keep their logic as minimal as possible. There are lots of benefits to this approach.

Reasons:

-   DRY: Rather than repeating the same logic in multiple views, it is defined once on the model.
-   Testable: Breaking up logic into small methods on the model makes your code easier to unit test.
-   Readable: By giving your methods friendly names, you can abstract ugly logic into something that is easily readable and understandable.

[Example](https://github.com/django/django/blob/ff6ee5f06c2850f098863d4a747069e10727293e/django/contrib/auth/models.py#L225-404)

### Directory Structure ###

Each app should be named the same as it is in the url e.g. an app called users maps to http://nextg.com.au/users

### URL conventions ###

Router from Django Rest Framework [source](http://www.django-rest-framework.org/api-guide/routers/)

### Admin Frontend ###

Do we want JS / CS / HTML style guide?


### To Keep In Mind ###

-   ALWAYS be concern of scalability, performance, availability, and security of the application

-   COMPLICATED or UNFAMILIAR codes must be commented

-   PRAGMATICALLY segregate anything for easier scanning of codes and don't over segregate

### Database ###

How do we want to handle transactions? Do we want to user ATOMIC_REQUESTS so database tranactions contain the entire HTTP request?

-   PROS:
    -   safer and easier to develop
-   CONS:
    -   slower performance

### Database Migrations ###

Always manually review migrations and test rollback functionality 

Always backup the database before applying a migration

Once project is deployed, test migration time on similar dataset with similar size to live database


### Git Commit Message Standards 

[git commit message standard](http://chris.beams.io/posts/git-commit/)

-   Separate subject from body with a blank line
-   Limit the subject line to 50 characters
-   Capitalize the subject line
-   Do not end the subject line with a period
-   Use the imperative mood in the subject line
-   Wrap the body at 72 characters
-   Use the body to explain what and why vs. how
Large white space changes / code cleanups should be in their own commit



### Git Workflow ###

##### Branches #####

master (production):
kept production ready

develop (staging):
almost all commits should branch from here


Each issue / feature / bug fix should be in its own topic branch.

Almost all changes should be branched from develop. If it is instead a hotfix, the branch should be named "hotfix-*"

To avoid integration problems, all topic branches should be short lived. If not possible, parent branch should be merged back into the topic branch frequently.

###### Before merging into develop: ######

1) All Continuous Integration tests should pass

2) Commits messages should only be about one thing and all changes should be related to the commit message. If they aren't, break them into a separate commit for each type of change, or possibly split into two branches if the changes aren't related at all.

3) All code should conform to the coding standards set.

4) Changes must be manually tested locally while with all commits from develop

###### How to Merge into develop: #####


Do we want to use merges with accurate history or rebase to keep a neat linear history? my (Ben's) proposal:

Rebase should be used to keep the history clean. 

All commits being pulled should be squashed into one commit to remove noise from the git log but kept unsquashed in the topic branch to preserve development history. The squashed commit should have all the other commit messages in the commit description, it should also reference the ticket number used by our project management software.

##### Merging to master: ######

Due to CI and large test coverage, develop should be kept to an almost production ready state in terms of stability. 

Should be tagged with a version number.

Ensure everything is documented, and has all the functionality required for a release.


# Coding Reviews #

possibile options:
-   Bitbucket pull requests
-   Gerrit
-   Phabricator

Make sure code is easy to read, meets business requirements, follows coding standards

Do we want to divide who is primarily responsible for the code reviews by tools?
e.g. developer X ensure caching works, developer Y ensures 

# Deployment #

Text goes here

### Configuration management ###

Possible Options:

-   Chef
-   Puppet
-   Ansible
-   SaltStack
-   Docker

### Scaling Plan ###

Text goes here

# Settings #

Possibly:
    Turn off features with flags e.g. python manage.py runserver --no-cache

### Application Settings ###

local development settings => settings.local

continuous integration settings => settings.test

production server settings => settings.production

All these will extend settings.base

### Dependencies ###

-   requirements/
    -   base.txt
    -   local.txt
    -   test.txt
    -   production.txt
    
### Secret Keys ###

Text goes here
