Prepare the database
====================
```
flask db init
flask db migrate
flask db upgrade
```

Set up admin account
=====================

Run the following commands in flask shell
```
# flask shell

from app.models import Employee
from app import db
admin = Employee(email="admin@admin.com",username="admin",password="admin2018",is_admin=True)
db.session.add(admin)
db.session.commit()
```