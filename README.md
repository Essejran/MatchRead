# book_recommendation101
A very basic first attempt at creating a book recommendation system using the data from [here](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) as well as [here](https://github.com/Shantanuh10/Book-Recommendation-System?tab=readme-ov-file)

## Getting Started with This Repository

### I. BEFORE CLONING THE REPO:
This repository uses a zipped data directory (data.zip) and the unzipped version is in .gitignore.
This repository uses Git Large File Storage (LFS) to handle large files. To ensure that you can clone and work with the repository effectively, follow these steps:

### 1. Install Git LFS

Before cloning the repository, you need to install Git LFS:

- **macOS:**
```bash
brew install git-lfs
```
- **linux:**
```bash
sudo apt-get install git-lfs
```
- **windows:**
  Download the installer from [Git LFS](https://git-lfs.com/).

#### 2. Initialize Git LFS
```bash
git lfs install
```

#### 3. Clone this repo 
```bash
git clone git@github.com:Essejran/MatchRead.git
```

#### 4. Verify large files:
```bash
git lfs ls-files
```

### II. Set up your Environment

**`Note:`**

- If there are errors during environment setup, try removing the versions from the failing packages in the requirements file. M1 shizzle.
- In some cases it is necessary to install the **Rust** compiler for the transformers library.
- make sure to install **hdf5** if you haven't done it before.

 - Check the **rustup version**  by run the following commands:
    ```sh
    rustup --version
    ```
    If you haven't installed it yet, begin at `step_1`. Otherwise, proceed to `step_2`.


### **`macOS`** type the following commands : 

- `Step_1:` Update Homebrew and install **rustup** and **hdf5** by following commands:

    ```BASH
    brew install rustup
    rustup-init
    ```
    Then press ```1``` for the standard installation.
    
    Then we can go on to install hdf5:
    
    ```BASH
     brew install hdf5
    ```

  Restart Your Terminal and then check the **rustup version**  by running the following commands:
     ```sh
    rustup --version
    ```
 
- `Step_2:` Install the virtual environment and the required packages by following commands:

  > NOTE: for macOS with **M1, M2** chips (other than intel)
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements_M1.txt
    ```
  > NOTE: for macOS with **intel** chips
  ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    
### **`WindowsOS`** type the following commands :

- `Step_1:` Install **rustup**  by following :
  
  1. Visit the official Rust website: https://www.rust-lang.org/tools/install.
  2. Download and run the `rustup-init.exe` installer.
  3. Follow the on-screen instructions and choose the default options for a standard installation.
  4. Then press ```1``` for the standard installation.
 
     
    Then we can go on to install hdf5:

    ```sh
     choco upgrade chocolatey
     choco install hdf5
    ```
    Restart Your Terminal and then check the **rustup version**  by running the following commands:
  
     ```sh
    rustup --version
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-bash` CLI :
  
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:
    ```Bash
    python.exe -m pip install --upgrade pip
    ```
Source for the environment settings: NeueFische

## Load the data to your notebook:
In any notebook, to quickly load datasets, run the following code in a new cell at the beginning of your notebook:

```%run import_data.ipynb```
