# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

ncnn_datas, ncnn_binaries, ncnn_hiddenimports = collect_all("ncnn")
ultra_datas, ultra_binaries, ultra_hiddenimports = collect_all("ultralytics")

a = Analysis(
    ['pd_node/__main__.py'],
    pathex=[],
    binaries=ncnn_binaries + ultra_binaries,
    datas=ncnn_datas + ultra_datas + [("pd_node/static", "static"), ("pd_node/models", "models")],
    hiddenimports=ncnn_hiddenimports + ultra_hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pd-node',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pd-node',
)
