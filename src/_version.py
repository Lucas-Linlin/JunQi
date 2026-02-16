# Main version
v_main = '0.1.0'

# Test version

v_test = '20260216'

if v_test:
    __version__ = f'{v_main}-test-{v_test}'
else:
    __version__ = v_main