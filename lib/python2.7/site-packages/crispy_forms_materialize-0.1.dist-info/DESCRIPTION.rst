Django application to add 'django-crispy-forms' layout objects for Materialize

Home-page: http://pypi.python.org/pypi/crispy-forms-materialize
Author: Emiliano Dalla Verde Marcozzi
Author-email: edvm@fedoraproject.org
License: GPL v3
Description: .. _docutils: http://docutils.sourceforge.net/
        .. _Django: https://www.djangoproject.com/
        .. _django-materialize-css: https://pypi.python.org/pypi/django-materialize-css/0.0.1
        .. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
        .. _Materialize: http://materializecss.com 
        
        Introduction
        ============
        
        This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Materialize`_.
        
        This app does not embed a `Materialize`_ release, you will have to install `django-materialize-css`_
        as a dependency.
        
        Links
        *****
        
        * Read the documentation on `Read the docs soon!`;
        * Download his `PyPi package https://pypi.python.org/pypi/django-materialize-css/0.0.1`
        * Clone it on his `Github repository <https://github.com/edvm/crispy-forms-materialize`;
        
        Requires
        ========
        
        * `django-crispy-forms`_ = 1.4.x;
        * `django-materialize-css`_ = 1.4.x;
        
        Installation
        ============
        
        Just register the app in your project settings like that :
        
        .. sourcecode:: python
        
            INSTALLED_APPS = (
                ...
                'materialize',
                'crispy_forms',
                'crispy_forms_materialize',
                ...
            )
        
        Then append this part to specify usage of the Materialize set :
        
        .. sourcecode:: python
        
            # Default layout to use with "crispy_forms"
            CRISPY_TEMPLATE_PACK = 'materialize_css_forms'
        
        All other `django-crispy-forms`_ settings option apply, see its documentation for more details.
        
Platform: UNKNOWN
Classifier: Development Status :: 5 - Production/Stable
Classifier: Environment :: Web Environment
Classifier: Framework :: Django
Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Classifier: Operating System :: OS Independent
Classifier: Programming Language :: JavaScript
Classifier: Programming Language :: Python :: 2.6
Classifier: Programming Language :: Python :: 2.7
Classifier: Programming Language :: Python :: 3.3
Classifier: Topic :: Internet :: WWW/HTTP
Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content
Classifier: Topic :: Software Development :: Libraries :: Python Modules
