from setuptools import find_packages, setup

# NOTE: upstream's requirements.txt is the full *training* stack with hard `==`
# pins (numpy==2.1.2, scipy==1.15.2, …) that conflict with a consumer's own lock.
# This fork is vendored only for the vision_encoder inference path, so we declare
# just that path's runtime deps, UNPINNED, letting the host resolver pick versions.
_RUNTIME_DEPS = [
    "torch",
    "numpy",
    "einops",
    "timm",
    "huggingface_hub",
]

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
    install_requires=_RUNTIME_DEPS,
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
