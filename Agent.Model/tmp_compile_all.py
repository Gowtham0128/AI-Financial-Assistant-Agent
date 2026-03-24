import py_compile,glob,sys,os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
ok = True
for p in glob.glob(os.path.join(root, '**', '*.py'), recursive=True):
    # skip virtual env and hidden folders
    if '\\.venv\\' in p or '\\site-packages\\' in p or '\\__pycache__\\' in p:
        continue
    try:
        py_compile.compile(p, doraise=True)
    except Exception as e:
        ok = False
        print(f"ERROR: {p}: {e}")
if ok:
    print('OK')
else:
    sys.exit(1)
