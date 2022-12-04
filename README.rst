License plate validator
=======================


Installation
------------

.. code-block:: bash

    $ # Clone repository
    $ git clone git@github.com:deluge/license-plate.git

    $ Create your virtualenv (recommended, use pyenv)
    $ Go into project root
    $ mkvirtualenv license-plate

    $ # Activate Environment and install
    $ workon license-plate
    $ make devinstall

    $ # run tests
    $ make tests


Setup the database
------------------

Default databasename for development is `license_plate_dev`

.. code-block:: bash

    $ python src/manage.py migrate


Staring the server & superuser
------------------------------

.. code-block:: bash

    $ # Create a new super user
    $ python src/manage.py createsuperuser

Now you can run the webserver and start using the site.

.. code-block:: bash

   $ python src/manage.py runserver

This starts a local webserver on `localhost:8000 <http://localhost:8000/>`_. To
view the administration interface visit `/admin/ <http://localhost:8000/admin/>`_


Resources
---------

* `Documentation <yu no url>`_
* `Code <https://github.com/deluge/license-plate>`_
