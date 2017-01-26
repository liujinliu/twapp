twapp
===========
A simple tornado web app generator, very simple, very clean.  
Just generate your app, and never touch it again.  

INSTALL
~~~~~~~~~~~~~~~
install from source:

::

    git clone git@github.com:liujinliu/twapp.git
    cd twapp 
    make install
    make uninstall ---UNDEPLOY METHOD

USEAGE
~~~~~~~~~~~~~
::

    (twapp)$twapp-make --help
    --app                            twork app name
    --prefix                         install twapp files in [PREFIX] (default
                                     ~/workspace) 


An example of generate a project:

::

    $ twapp-make --app=foo --prefix=mywork 
    $ cd mywork/foo
    $ make build
    $ pip install dist/foo-0.0.1-py2-none-any.whl
    $ foo-start --help
      --base-dir                       put the config path here (default .)
      --debug                          debug option (default False)
      --port                           app listen port (default 8888)
    $ foo-start
    $ curl http://localhost:8888/ping
    foo works well.


