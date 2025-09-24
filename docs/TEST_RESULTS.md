# 🧪 Test Results

Ejecutado con:
```sh
python -m pytest --cov=app
```

---

## ✅ Resumen
- **Total tests:** 69  
- **Passed:** 69  
- **Failed:** 0  
- **Cobertura total:** 97%  

---

## 📊 Detalle de cobertura

```
Name                               Stmts   Miss  Cover
------------------------------------------------------
app\core\config.py                     9      0   100%
app\core\security.py                  37      2    95%
app\core\types.py                      3      0   100%
app\core\validators.py                10      1    90%
app\crud\author.py                    19      0   100%
app\crud\book.py                      31      9    71%
app\crud\user.py                      21      0   100%
app\db\base.py                         3      0   100%
app\db\session.py                     18      8    56%
app\main.py                            7      0   100%
app\models\__init__.py                 3      0   100%
app\models\author.py                  11      0   100%
app\models\book.py                    13      0   100%
app\models\user.py                    13      0   100%
app\routers\auth.py                   15      0   100%
app\routers\author.py                 23      0   100%
app\routers\book.py                   34      1    97%
app\routers\user.py                   27      0   100%
app\schemas\auth.py                   13      0   100%
app\schemas\author.py                 28      2    93%
app\schemas\book.py                   34      1    97%
app\schemas\user.py                   36      1    97%
app\services\auth.py                  13      0   100%
app\services\author.py                31      0   100%
app\services\book.py                  59      4    93%
app\services\user.py                  45      0   100%
app\test\auth\auth_data.py             2      0   100%
app\test\auth\test_auth.py            21      0   100%
app\test\auth\test_auth_token.py      16      0   100%
app\test\author\author_data.py         3      0   100%
app\test\author\test_authors.py       48      0   100%
app\test\books\book_data.py            2      0   100%
app\test\books\test_book_auth.py      51      0   100%
app\test\books\test_books.py          67      1    99%
app\test\conftest.py                  39      0   100%
app\test\test_db.py                   15      0   100%
app\test\users\test_users.py          72      0   100%
app\test\users\user_data.py            3      0   100%
------------------------------------------------------
TOTAL                                895     30    97%
```

---

⏱️ Tiempo de ejecución: **39.75s**  