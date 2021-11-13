# Change With Tip

1. Installation for backend instructions
  ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
  ```

2. Frontend Installation
```sh
cd templates && npm install
npm start
```
Visit http://localhost:4200 to use the application.

Prod Mode:

Build frontend:
```sh
cd templates && npm install
ng build --prod
```

Start prod server:
```sh
  flask run
```

Visit http://localhost:5000/ to use the application.
