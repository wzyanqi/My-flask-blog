import sys
import os
import sae

app_root = os.path.dirname(__file__)
sae.add_vendor_dir(app_root)
sae.add_vendor_dir(os.path.join(app_root, 'venv/Lib/site-packages'))
sae.add_vendor_dir(os.path.join(app_root, 'venv/Lib'))
sae.add_vendor_dir(os.path.join(app_root, 'venv'))
sae.add_vendor_dir(os.path.join(app_root, 'venv/Scripts'))


from manage import app
application = sae.create_wsgi_app(app)

