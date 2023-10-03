# NOTE
## structure
```
code1
|---methods
|---static
|   |---js
|   |   |---morninghill.js
|   |---style
|   |   |---home.css
|---templates
|   |---home.html
|   |---store.html
|---app.py
|---note.md
```
## database design
### orderfood.db
**stores**  
|area|store|s_id|main|
|---|---|---|---|
|靜園|極咖哩|品項id|品項|
|靜園|極咖哩|.|.|
|宜園|早安山丘|||
|至善|好吃鮮果|||

**users**
|u_id|email|pwd|acc|name|
|---|---|---|---|---|
|1|auth@auth.com|admin|admin|admin|

**order**
|id|u_id|s_id|count|money|createTime|
|---|---|---|---|---|---|
|1|1|1|2|60|2023-08-29 00:00:00|
|2|1|3|3|150|2023-09-01 12:00:00|

**簡介**
Uber 功能全都要有 店家要可看到餐點內容
登入(分為買家、賣家)
