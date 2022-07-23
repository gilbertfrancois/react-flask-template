# React - Flask template
_Gilbert François Duivesteijn_

## Abstract

This is a bare minimal template, which I personally use for developing a React web application with a python Flask backend.

## Backend

Step 1: Install python environment. If you use poetry, then simply run:

```sh
cd backend
poetry install
```

- Step 2: Change the port number in `main.py` if you don't want to run it on the default port 5000.

- Step 3: Start the development backend

```sh
poetry run python main.py
```

## Frontend

- Step 1: Install and start the frontend:

```sh
cd frontend
npm install
rpm run dev
```
A development webserver will start at `http://localhost:1234`. If you prefer another port, you can use the `PORT` environment variable. 

- Step 2: Set the `API_URL` in `<project_folder>/frontend/config.js` that points to the backend address (and port).

## Cross-Origin Resource Sharing (CORS)

Since in development mode the frontend and backend run on same server, but different ports, the browser will block the responses from the backend. The backend needs to take care of additional permissions in the header. This project has taken care of this in the backend boilerplate. But it is advised to revise the defaults in `main.py` and make security stronger, if applicable.

## Production

Build the frontend with `npm run prod`. The compiled sources will be placed in `<project_folder>/frontend/dist`. Use e.g. Nginx to serve the files. For the backend, use e.g. wsgi-mod, instead of the flask build-in development webserver.


