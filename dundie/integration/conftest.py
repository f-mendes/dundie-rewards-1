MARKER = """\
integration: Mark integration test
high: High Priority
medium: Medium Priority
low: Low Priority
"""

# Throwing warnning in the tests
#def pytest_configure(config):
#   map(lambda line: config.addinivalue_line('markers', line), MARKER.split("\n"))

def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers', line)
    