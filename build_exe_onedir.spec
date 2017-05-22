# -*- mode: python -*-

import os

block_cipher = None

main_file = 'hello_world.py'

a = Analysis(
    [main_file],
    pathex=[],
    binaries=[
    ],
    datas=[
#        (
#            os.path.join('C:\\Windows', 'System32', 'vcruntime140.dll'),
#            '.',
#        ),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='hello_world',
    debug=False,
    strip=False,
    upx=False,
    console=False,
    icon=os.path.join('data', 'icon.ico'),
)

coll = COLLECT(
    exe,
    Tree('data', prefix='data'),
    a.binaries + [
    ],
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name='hello_world'
)