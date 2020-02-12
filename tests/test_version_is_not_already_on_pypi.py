import subprocess, sys
from pkg_resources import safe_version

from beryl_plugin import __version__

def test_version_is_not_already_on_pypi():
	_, pip_output = subprocess.getstatusoutput([sys.executable, '-m', 'pip', 'install', 'beryl-plugin=='])
	available_versions = pip_output.split("(")[1].split(")")[0].replace("from versions: ", "").split(", ")
	print(available_versions)
	assert not safe_version(__version__) in available_versions

if __name__ == "__main__":
	test_version_is_not_already_on_pypi()
