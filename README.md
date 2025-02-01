
# AI Workflow Demo

## pythonのバージョン管理

- 使用ライブラリ`pyenv`
```sh
brew install pyenv
pyenv install 3.12
```

- バージョン切り替え
```sh
poetry env list
# .venv

poetry env remove .venv
poetry env use 3.10.4
poetry install
```

.python-versionファイルでバージョンを指定

## フォーマット、リント設定

下記のvscode拡張機能をインストール
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
  - [公式サイト](https://docs.astral.sh/ruff/)

## プロジェクトのセットアップ

### 1. poetryの設定〜モジュールインストール

#### venvの作成場所をプロジェクト直下にする設定（globalに設定される）
```sh
poetry config virtualenvs.in-project true
```

#### 初回インストール
```sh
poetry install

# もしくは
make init
```

### 2. poetryで実行

- pythonで起動
```sh
poetry run src/main.py

# もしくは
make dev
```

- streamlitを起動
```sh
poetry run streamlit run src/main.py

# もしくは
make streamlit
```

### poetryの色々なコマンド
```sh
# モジュールのpyproject.tomlに追記とインストール
poetry add 【モジュール名】

# モジュールのpyproject.tomlからの削除とアンインストール
poetry remove 【モジュール名】

# 全てアップデート、最新時はスキップ
poetry update

# モジュールのアップデート、最新時はスキップ
poetry update 【モジュール名】

# updateをしたらどうなるかを表示
poetry update –-dry-run

# 全モジュールのpyproject.tomlからの削除とアンインストール
poetry env remove --all
```
