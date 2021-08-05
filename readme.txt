
--
https://www.youtube.com/watch?v=GdlFhF6gjKo
-
-
https://github.com/ccxt/ccxt
-
https://github.com/sammchardy/python-binance
-
https://github.com/EasyAI/Simple-Binance-Trader
-




------------------------
https://github.com/jakerieger/FlaskIntroduction
-----------   flask
pip install flask flask-sqlalchemy
-
https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
-

---- # on normal
pip install gunicorn
-- # on debian
sudo apt-get install gunicorn3


-----------------------------------------------
-------------- Heroku
https://devcenter.heroku.com/articles/heroku-cli
-
in terminal :
heroku login
-
user name
passwork
-
pip install gunicorn
-
touch Procfile 
(paste this in it) web: gunicorn app:app
-
pip freeze > requirements.txt
-
git init
-
git add .
-
git commit -m "init commit"
-
heroku create flaskappcrud
-
git remote -v
-
git push heroku master
-
