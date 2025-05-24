### 1. What are the advantages of relative imports in large-scale projects?

* **Easier refactoring:** Relative imports allow you to move entire packages or subpackages around without changing import statements, because they use the package’s internal structure rather than full paths.
* **Improved modularity:** They emphasize that modules belong to the same package, helping maintain encapsulation.
* **Cleaner code:** They reduce verbosity by avoiding long absolute paths inside a package.
* **Avoid naming conflicts:** Since they use relative paths, they minimize the chance of colliding with similarly named modules elsewhere in the project or environment.

---

### 2. How does venv help in dependency management for teams?

* **Isolated environments:** Each developer gets a separate Python environment, so dependencies don’t clash between projects or team members.
* **Reproducibility:** Using `requirements.txt` inside a virtual environment ensures everyone installs the exact same package versions.
* **Avoids polluting system Python:** Keeps global Python clean and stable.
* **Easier debugging:** Problems related to dependencies are isolated within the venv.
* **Simplifies CI/CD:** Continuous integration servers can replicate the environment easily.

---

### 3. What happens if you forget to include `__init__.py` in a subpackage?

* **Python <3.3:** The folder is **not recognized as a package**, so you cannot import modules using package syntax from it.
* **Python ≥3.3:** Implicit namespace packages allow imports without `__init__.py`, but:

  * Some tooling and IDEs may not recognize the folder as a package.
  * You lose the ability to execute package initialization code.
  * Relative imports inside that folder can break or behave unexpectedly.

---

### 4. Explain `pyproject.toml` vs `setup.py` — what is the future of packaging in Python?

* **`setup.py`:** Traditional Python packaging script using setuptools; it’s executable Python code defining how to build/install a package.
* **`pyproject.toml`:** A newer, declarative configuration file introduced by [PEP 518](https://www.python.org/dev/peps/pep-0518/) specifying build system requirements and package metadata in a standardized format.
* **Future:**

  * `pyproject.toml` is becoming the **standard** for packaging configuration, enabling **build system independence** (e.g., poetry, flit, setuptools).
  * It supports **declarative metadata** and better tooling interoperability.
  * `setup.py` may become optional or even deprecated for many projects.
* **Summary:** Move toward `pyproject.toml` for cleaner, more standardized, and tool-agnostic packaging.

---