# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['funktions.py'],
    pathex=[],
    binaries=[],
    datas=[("C:\Users\Thomas Karrer\Desktop 3\Python Projekte\Multi_GPT_Voice_Assistent_nogui\Lib\site-packages\vosk", "./vosk"],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='funktions',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
