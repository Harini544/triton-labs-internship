# ML Data Loader

## Project Purpose

This project is designed for a beginner-friendly ML internship learning track. It teaches:

- reproducible environment setup
- how ML projects are structured
- iterators and generators
- lazy evaluation
- memory-efficient data loading
- simple testing and memory measurement

The goal is not to build a large ML pipeline yet. The focus is on understanding the foundations that make ML projects reliable, efficient, and easy to reproduce.

---

## Internship Roadmap

D1 — Environment Setup
D2 — Iterators
D3 — OOP / Pipeline (Upcoming)
D4 — Type Hints / Pydantic (Upcoming)
D5 — Decorators / Context Managers (Upcoming)
D6 — Exceptions (Upcoming)
D7 — Logging (Upcoming)
D8 — SOLID Refactor (Upcoming)
D9 — Testing (Upcoming)
D10 — Debug / Profile (Upcoming)
D11 — Branching (Upcoming)

Current implementation:

- D1 — implemented
- D2 — implemented

Future D3-D11 tasks will be added later when the mentor provides the detailed requirements.

---

## D1 — Environment Setup

### 1. venv vs conda vs poetry

A Python environment keeps project dependencies separate from the system Python. This matters because different projects may need different versions of packages.

#### venv

- venv is Python's built-in virtual environment tool.
- It creates an isolated project environment.
- It is lightweight and works well for simple Python projects.
- It solves the problem of dependency conflicts between projects.
- Advantage: built into Python, easy to use.
- Disadvantage: it does not manage dependency resolution as advanced as Poetry.

#### conda

- conda is a package and environment manager used heavily in data science and ML.
- It can manage Python packages and non-Python libraries more broadly than venv.
- It solves environment reproducibility for scientific workflows and complex dependencies.
- Advantage: good for scientific/ML environments with many compiled dependencies.
- Disadvantage: heavier than venv, and more setup is sometimes needed.

#### poetry

- Poetry is a dependency manager and packaging tool for Python projects.
- It helps create environments, install dependencies, and manage project metadata.
- It solves the problem of dependency declaration and reproducible installation.
- Advantage: modern workflow, lockfile support, package management.
- Disadvantage: an extra tool to learn, and some projects prefer the simpler venv workflow.

### Why reproducibility matters

Reproducibility means the same project can be installed and run the same way on different machines. This matters in software and especially in ML because:

- results depend on library versions
- data processing steps may change with package versions
- model behavior may differ between runs if environment changes
- collaborators need to work in the same environment

### Why it matters in ML

ML workflows depend on specific versions of Python, libraries, and data-processing tools. A model trained with one version of a library may behave differently from one trained with another version. Reproducible setups reduce surprises and make debugging easier.

### 2. Dependency pinning

Dependencies can be specified in different ways.

- Loose version: package>=1.0
- This allows newer versions to be installed.
- It is flexible, but it can change behavior over time.

- Pinned version: package==1.2.3
- This locks the exact installed version.
- It helps reproducibility.

- Lockfiles: a lockfile records the exact dependency versions used in a project.
- Examples include Poetry lock files or pip-style compiled dependency lock files.
- They are useful because they let teammates install the exact same package set.

In ML, reproducibility matters because small dependency changes can affect data pipelines, model training, and evaluation results.

### 3. pyproject.toml

pyproject.toml is the modern Python project configuration file.

It is used for:

- project metadata
- build configuration
- tool configuration
- dependency settings in modern Python projects

Modern Python projects use it because it is standardized and clearer than older patterns. It is the recommended place for Python project metadata.

setup.py used to be common for Python packaging, but it is becoming less common because pyproject.toml is more modern, structured, and easier to use with build tools.

### 4. Project layout

#### Flat layout

A flat layout keeps all project files in one folder. It is easy to read for small projects.

#### src/ layout

A src/ layout places package code under a src/ directory instead of directly in the project root. This helps separate project source code from setup files and helps reduce accidental imports.

Advantages of src/ layout:

- cleaner project structure
- less confusion between project files and installed package code
- better for real-world Python projects
- easier to scale as the project grows

### 5. ML repository structure

This project uses a basic ML repository structure:

- data/ for datasets and data folders
- notebooks/ for experiments and exploration
- configs/ for configuration files
- scripts/ for utility and environment scripts
- tests/ for automated tests
- src/ for package source code

### 6. .gitignore for ML

A .gitignore file prevents large or temporary files from being tracked in Git. This is especially important in ML projects because the repo should not store:

- __pycache__/
- .venv/
- venv/
- .env
- .pytest_cache/
- .ipynb_checkpoints/
- large datasets
- model files
- checkpoints
- logs

This keeps repositories small and helps avoid committing data or model artifacts by accident.

### 7. README structure

A good README explains what the project does and how to run it. A stranger should be able to understand:

- what the project is for
- how the environment is set up
- how to install dependencies
- how to run tests
- how to run the main scripts
- what the project folders mean

---

## D2 — Iterators

This project introduces the core ideas behind iterators, generators, and lazy evaluation.

### __iter__

__iter__() is called by Python when a for loop starts iterating. It gives Python the iterator object.

### __next__

__next__() returns the next value. When there are no values left, it raises StopIteration.

### StopIteration

StopIteration tells Python that the iteration is complete. A for loop stops when it receives this signal.

### Generators

A generator function uses yield instead of return. This makes it lazy: it produces one item at a time instead of building everything at once.

### yield

yield pauses the function and returns a value to the caller. The next time the generator is asked for more values, it resumes from where it left off.

### return vs yield

- return ends the function completely
- yield pauses the function and can continue later

### Generator expressions

A list comprehension is eager:

[x * 2 for x in numbers]

This creates the entire list immediately.

A generator expression is lazy:

(x * 2 for x in numbers)

This produces values one at a time when requested.

### Lazy evaluation vs eager evaluation

Lazy evaluation avoids loading everything into memory at once. This is useful when reading large CSV files or huge datasets.

Eager evaluation loads everything immediately, which can consume more memory.

### itertools

The itertools module gives helpers for working with iterators, such as:

- islice
- chain
- batched

In this project, examples are included in the iterator_examples module.

If itertools.batched is unavailable in an older Python version, the project includes a simple fallback implementation instead of breaking.

### Memory measurement

Python includes tracemalloc for measuring memory usage. It helps us compare how much memory a lazy iterator uses versus a less careful approach.

This project includes a script that generates temporary CSV data and compares memory use across different dataset sizes.

---

## Project Structure

- src/ml_data_loader/: Python package for the learning project
  - __init__.py: package entry point
  - data_loader.py: lazy CSV loader and generator examples
  - iterator_examples.py: itertools examples
- data/: raw data and prepared data directories
  - raw/: raw inputs
  - processed/: processed outputs
  - sample/: sample CSV files used for learning
- notebooks/: place for experiments and notebooks
- configs/: configuration files
- scripts/: setup and utility scripts
- tests/: automated tests
- requirements.txt: pinned Python dependencies
- pyproject.toml: modern project metadata and config
- .gitignore: keeps temporary and large files out of Git
- README.md: project overview and learning instructions

---

## Setup

### Windows setup with venv

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

### Using the setup script

This project includes a PowerShell helper script:

```powershell
./scripts/setup.ps1
```

The script will:

1. create the virtual environment if it does not exist
2. activate it
3. install pinned requirements
4. install the package in editable mode
5. run a quick verification with pytest
6. print a confirmation message

---

## Running Tests

From the project root:

```powershell
pytest
```

This runs the test suite and verifies the CSV iterator behavior.

---

## Running Memory Experiment

From the project root:

```powershell
python scripts/memory_test.py
```

The script creates temporary CSV datasets, runs the lazy iterator, measures memory with tracemalloc, and prints actual results.

---

## Memory Experiment Results

Add your actual output here after running the experiment.

Example section:

```text
Dataset Size | Batch Size | Current Memory | Peak Memory
---------------------------------------------------------
100          | 100        | ...            | ...
1000         | 100        | ...            | ...
10000        | 100        | ...            | ...
```

What should be observed conceptually:

- memory should stay relatively stable as dataset size grows
- the implementation should not load the entire file into memory at once
- batch size and file size are important factors
- exact values vary by operating system, Python version, and machine

---

## Learning Order

Study in this order:

1. D1 repository structure
2. venv
3. dependency pinning
4. pyproject.toml
5. src layout
6. .gitignore
7. README
8. D2 __iter__
9. __next__
10. StopIteration
11. generators
12. yield
13. generator expressions
14. itertools
15. tracemalloc
16. memory experiment

After that, continue with D3 when the mentor gives the next task.

---

## Notes

This project intentionally implements only D1 and D2. The future D3-D11 roadmap is documented here, but not built yet. This keeps the project clean and ready for the next mentor tasks without inventing requirements in advance.
