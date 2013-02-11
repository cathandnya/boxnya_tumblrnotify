# TumblrNotify
===================

Tumblr の Notification の Boxnya input プラグインです。  
Boxnya は↓を参照。  
https://github.com/non-117/Boxnya  

## インストール

Boxnyaのlib/inputsにファイルを配置してください。

## 設定

settings.py の MODULE_SETTINGS に以下を追加。

    "tumblrnotify":[{
        "email": メールアドレス,
        "password": パスワード,
        "blog": 通知するブログ名,
        "period": 更新間隔を秒数で指定　例: 300
    },]

