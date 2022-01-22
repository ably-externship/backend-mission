from .common import *

DEBUG = False 

if DEBUG :
    INSTALLED_APPS += ['debug_toolbar',]

    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]