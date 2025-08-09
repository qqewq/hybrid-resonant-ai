from setuptools import setup, find_packages

setup(
    name="hybrid_resonant_ai",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch",
        "transformers",
        "numpy",
        "scikit-learn"
    ],
)
