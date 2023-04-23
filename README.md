# Pitch Recognition

## Quick Start

### 1. 単音の特定

#### 🌐 共通

1. `src` ディレクトリに `wav_files` ディレクトリを作成する

```bash
📁 src
┗ 📁 wav_files
```

2. `wav_files` ディレクトリに解析したい音声ファイルを入れる

```bash
📁 src
┗ 📁 wav_files
  ┣ a.wav
  ┣ b.wav
  ┗ c.wav
```

#### 🖥️ ローカルの Python 環境で動かす場合

1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

2. 実行

```bash
python src/main.py
```

#### 🐳 Docker 環境で動かす場合

```bash
docker-compose up
```
