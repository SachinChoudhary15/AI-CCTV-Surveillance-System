from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="AI-CCTV-Surveillance-System",
    version="1.0.0",
    author="Sachin Choudhary",
    author_email="your-email@example.com",   # Apna email yahan likh dena
    description="AI-powered CCTV Surveillance System using YOLOv8, OpenCV, FastAPI and Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "torch",
        "torchvision",
        "ultralytics",
        "opencv-python",
        "numpy",
        "Pillow",
        "imutils",
        "fastapi",
        "uvicorn",
        "streamlit",
        "pandas",
        "requests",
        "python-dotenv",
        "pytest",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)