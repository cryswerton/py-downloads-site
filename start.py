import os
import sys

def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv():
    print('inside virtualenv or venv')
    # os.system('cmd /k "set FLASK_DEBUG=1"')
else:
    os.system('cmd /k "my-venv\Scripts\\activate"')

os.system('cmd /k "flask run --host=0.0.0.0"')