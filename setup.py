from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="fb_perception_models",
    version="1.0.0",
    author="Meta AI Research, FAIR",
    description="Models of the Perception family.",
    url="https://github.com/facebookresearch/perception_models",
    # Everything ships under the single top-level `fb_perception_models` package
    # (upstream's generic `core`/`apps` were nested under it) so nothing collides
    # with a consumer's own top-level `core` namespace.
    packages=find_packages(include=["fb_perception_models", "fb_perception_models.*"]),
    package_data={
        "fb_perception_models.vision_encoder": ["bpe_simple_vocab_16e6.txt.gz"]
    },
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
    ],
    license="FAIR Noncommercial Research License",
    # Upstream set >=3.11 conservatively; the vision_encoder import path uses no
    # 3.11-only features and compiles/runs under 3.10 (matches the voxel monorepo
    # and the sibling dinov2 fork). Relaxed so it resolves in a 3.10 pip lock.
    python_requires=">=3.10",
    include_package_data=True,
)
