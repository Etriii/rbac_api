Install this following:
```
pip install -r requirements.txt
```

To run migrations:

``` generate migration
```
In Windows:
alembic revision --autogenerate -m "Migration Message"

``` run migration
alembic upgrade head
```
In Windows:
python -m alembic upgrade head


To run the app:
```
uvicorn app.main:app --reload
```
In Windows:
python -m uvicorn app.main:app --reload



