# arias-tale-rag

a simple rag acting as an encyclopedia for [Aria's Tale](https://www.ariastale.com/)

## usage

First, start up the back end as described in backend/README.md, then, in this top-level folder:

```bash
docker build -t arias-tale-rag .
docker run -p 8000:8000 arias-tale-rag
```

Then:
2. migrate the backend db
3. load splits for the rag
    a. optionally run integration tests in backend/ to verify server is in a good state
4. build the front end and re-build the fullstack container
    a. or, just `npm run dev` for development

Run the UI and prompt it! The UI will be one of:

1. Docker-based UI: <http://localhost:8000/app/> or <http://0.0.0.0:8000/app/>
2. Vite dev server UI: <http://localhost:5173/app/>

## troubleshooting

If you are accessing the UI through Docker, you might need to clear your browser cache to view updates.
