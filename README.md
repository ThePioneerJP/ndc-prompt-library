# NDC Prompt Library

![file-GZOdguAbdEHCYEoplSeSO5ww](https://github.com/ThePioneerJP/ndc-prompt-library/assets/116901962/ad6e277a-f45e-44c0-a5ce-8c856c0f5967)

English version: [README_EN.md](README_EN.md)

## 概要

NDC Prompt Libraryは、日本十進分類法（Nippon Decimal Classification、NDC）に基づいて作成されたシステムプロンプトのライブラリです。このライブラリは、NDCの分類体系に沿って整理されており、様々な分野のプロンプトを効率的に管理し、利用することができます。

## 構成

ライブラリの詳細な構成については、[ndc_list.md](ndc_list.md)を参照してください。このファイルには、NDCの分類に従ったプロンプトの一覧が記載されています。

## ディレクトリ構造の自動生成

本リポジトリには、[create_directories.py](create_directories.py)というPythonスクリプトが含まれています。このスクリプトは以下の機能を持っています：

- このスクリプトが設置されたディレクトリ内に置かれている[directory_structure.txt](create_directories.py)ファイルに記述されたディレクトリ構造（Githubなどで一般的に使用される形式）に基づいて、自動的にこれを生成します。
- `.gitignore`ファイルも自動的に生成されるため、このディレクトリ構造はGithubでも共有可能な形式になっています。

このスクリプトは、本ライブラリのディレクトリ構造を作成する際に使用されましたが、他のプロジェクトでも利用可能です。ぜひご活用ください。

## ライセンス

このプロジェクトは[MISA-RM](LICENSE.md)ライセンスの下で公開されています。使用する際は、ライセンスの条件を確認してください。

## 貢献

プロンプトの追加や改善、バグ報告などの貢献を歓迎します。プルリクエストやイシューを通じて、プロジェクトの発展にご協力ください。

## 連絡先

質問や提案がある場合は、Githubのイシューを通じてお問い合わせください。
