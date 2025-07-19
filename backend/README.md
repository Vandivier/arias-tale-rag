# google-adk backend

this backend `requires-python = ">=3.11,<4.0"`

install and run the app using [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

now you can run the app via the adk cli

```bash
adk web
```

## unit testing

```bash
uv run pytest src/test_unit.py
```

## eval and integration testing

We estimate accuracy as the percentage of passed test cases in src/integration_tests.py

Run the server with Docker as mentioned in the top-level README.md:

```bash
docker build -t adk-quickstart .
docker run -p 8000:8000 adk-quickstart
```

Now you can validate that the server is running properly with a curl command:

```bash
curl -X POST http://localhost:8000/invoke \
-H "Content-Type: application/json" \
-d '{"query": "Hello, what can you do?"}'
```

Once the server is working properly, run the integration test:

```bash
uv run pytest src/test_integration.py
```
