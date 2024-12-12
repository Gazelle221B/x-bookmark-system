# Xブックマーク整理システム

X（旧Twitter）のブックマークを自動的に取得し、LLM（ChatGPT, Claude, Gemini）を活用した分類・要約・タグ抽出を行った上で、Notionデータベースに登録するシステムです。  
このリポジトリには、スクレイピング、データ前処理、LLMとの連携、Notionへの登録までの処理フローが含まれます。

## 特徴

- **Playwright**を用いてXブックマークページからツイート情報を自動取得
- **LLM (OpenAI, Claude, Gemini)** によるツイート内容のカテゴリ分類、要約、タグ付け
- **Notion API**を通じてデータベースへ情報を登録
- `pytest`と`flake8`を用いたテスト・Lint整備で品質確保
- `.env`ファイルを用いて機密情報（Xログイン情報、LLM APIキー、Notionトークン）を安全に管理（.gitignoreでリポジトリ外に）

## 開発環境セットアップ手順

1. **リポジトリクローン**
   ```bash
   git clone https://github.com/Gazelle221B/x-bookmark-system.git
   cd x-bookmark-system
