!SLIDE smbullets

# Trucos

* Rutas relativas en settings.py
* APPS locales en apps/
* local_settings.py
* render_to decorator
* django-debug-toolbar

!SLIDE smaller

# Rutas relativas en settings.py

    @@@python
    import os
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static') 

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'templates')
    )

!SLIDE smaller

# APPS locales en apps/

    @@@python
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

!SLIDE smaller

# local_settings.py

    @@@python
    # Con local_settings podemos reescribir / agregar settings
    # que sean propios de la maquina donde se encuentre, 
    # por ejemplo BBDD y DEBUG
    # MANTENER SIEMPRE ABAJO; PARA SOBREESCRIBIR

    try:
        from local_settings import *
    except ImportError:
        pass

!SLIDE smaller

# render_to decorator

    @@@python
    from annoying.decorators import render_to
    
    @render_to('template.html')
    def foo(request):          
        bar = Bar.object.all()  
        return {'bar': bar}     
    
    # equals to 
    def foo(request):
        bar = Bar.object.all()  
        return render_to_response('template.html', 
            {'bar': bar},    
            context_instance=RequestContext(request))


!SLIDE smaller

# django-debug-toolbar

    @@@python
    if DEBUG:
        try:
            #Check if django-debug-toolbar is installed
            import debug_toolbar
            MIDDLEWARE_CLASSES += (
                'debug_toolbar.middleware.DebugToolbarMiddleware',
            )

            INTERNAL_IPS = ('127.0.0.1',) 

            INSTALLED_APPS += ('debug_toolbar', ) 

            DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False} 
        except: 
            pass 
