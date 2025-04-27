# recipe-api

# python で API の作成演習

### フォルダ構成

今回は以下を想定
recipe_api/
├── main.py # FastAPI アプリ立ち上げ
├── controllers/
│ └── recipe_controller.py # リクエストを受けるコントローラー
├── models/
│ └── recipe_model.py # レシピのデータ管理
├── views/
│ └── recipe_view.py # レスポンス整形
└── data/
└── recipes.py # レシピの初期データ
