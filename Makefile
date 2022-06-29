export PYTHONPATH = src



pre-release:
	python util/release.py

pre-patch:
	python util/release.py --patch

post-release:
	python util/release.py --post_release

post-patch:
	python util/release.py --post_release --patch