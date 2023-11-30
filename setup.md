# Setting up the python environment

## Installing pyenv
### Windows
1. Install WSL2 (Windows service for linux ver.2); following is an example in Windows 10
    * Open "Windows Power Shell" or "Terminal" as Administrator.
    * Type `wsl --set-default-version 2` (for safe)
    * Type `wsl --install -d Ubuntu`.
    * After installation is done, open `Ubuntu` in Application.

* When above doesn't work, check "Windows の機能の有効化、または無効化", then "Linux 用 Windows サブシステム", "仮想マシンプラットフォーム" is ON.
* Note that WSL makes home directory (`/home/your_name`) which is different from the Windows user directory (`C:\Users\your_name`).
* You can access Windows system from Ubuntu like: `cd` to Desktop by `cd /mnt/c/Users/your_name/Desktop/`.
* It is useful to make symbolic link between Ubuntu and Windows like
    ```bash
    cd
    ln -s /mnt/c/Users/your_user_name/Desktop/ desktop
    ```
* If some commands are unavailable (e.g. vi), install them by `sudo apt install vim`.

2. Install Dependencies
```bash
sudo apt update
sudo apt -y upgrade
```
then
```bash
sudo apt install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncursesw5-dev \
    tk-dev \
    libffi-dev \
    liblzma-dev
```

3. Clone pyenv
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

4. Update Bash Configuration
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
```

5. Reload Bash Configuration
```bash
source ~/.bashrc
```

### Mac
1. Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install pyenv via Homebrew
```bash
brew install pyenv
```

3. Add pyenv to Shell
* Add pyenv to your shell's configuration file (.bash_profile, .bashrc, .zshrc, or similar).
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```

4. Restart or Reload Shell Configuration
```bash
source ~/.bash_profile
```

##  Install Python using pyenv
1. List available Python versions
```bash
pyenv install --list
```

2. Choose a version and install it (e.g., Python 3.9.5)
```bash
pyenv install 3.9.5 --verbose
```
* It will take some time ...

3. Set Global Python Version
```bash
pyenv global 3.9.5
```

4. Verify Installation
```bash
python --version
```

### Troubleshooting
* `'ImportError: No module named '_tkinter', please install the python3-tk package'`
    * Do `sudo apt install python3-tk`.


## Google Colaboratory
### Uploading data
* You can upload the files in Colab webpage, but it is better setup the Google Drive and move data from it.
* Setup the google site to make Google Drive account.
* Upload the file/folder with Google Drive.

* Putting `!` indicates the *shell command*.
* Putting `%` indicates the *magic command*.
* To change the directory, specify `%cd` (not `!cd` because it generates new shell).

* You can directly edit the python script (.py) file in Google Colab.

### Using GPU
1. "Runtime" tab.
2. "Change the type of Runtime".
3. Choose GPU you want.
