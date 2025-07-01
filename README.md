<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [トラブルシューティング](#トラブルシューティング)

<!-- READMEの作成方法のドキュメントのリンク -->
<br />
<div align="right">
    <a href="READMEの作成方法のリンク"><strong>READMEの作成方法 »</strong></a>
</div>
<br />
<!-- プロジェクト名を記載 -->

## プロジェクト名

コマンドライン単語帳（Python 学習 Day1）

<!-- プロジェクトについて -->

## プロジェクトについて

英単語と日本語訳を登録し、クイズ形式で出題するシンプルな単語帳を作成する。

<!-- プロジェクトの概要を記載 -->

  <p align="left">
    <br />
    <!-- プロジェクト詳細にBacklogのWikiのリンク -->
    <a href="Backlogのwikiリンク"><strong>プロジェクト詳細 »</strong></a>
    <br />
    <br />

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク | バージョン |
| -------------------- | ---------- |
| Python               | 3.11.7     |

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

<!-- Treeコマンドを使ってディレクトリ構成を記載 -->

❯ tree -a
.
工事中

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

<!-- コンテナの作成方法、パッケージのインストール方法など、開発環境構築に必要な情報を記載 -->

### ワークスペース作成

`cd`コマンドでプロジェクトを作成する位置へ移動
`mkdir wordbook-project`を実行し、ワークスペースを作成

### 仮想環境の作成

`python -m venv venv`を実行する。
wordbook-project フォルダに venv というサブフォルダが生成される ← 仮想環境本体

### 仮想環境のアクティベート（有効化）

`source venv/bin/activate`
成功するとコマンドプロンプトの先頭に(venv)と表示される
※このコマンドは、ターミナルを開くたびに実行する必要がある

### 仮想環境のデアクティベート（無効化）

`deactivate`
コマンドプロンプトの(venv)表示が消え、元のグローバル環境に戻る
