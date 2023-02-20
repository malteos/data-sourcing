# data-sourcing

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# App
streamlit run sourcing_form.py --server.port=8501 --server.address=0.0.0.0

streamlit run sourcing_form.py --server.port=8501 --server.address=0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false --server.baseUrlPath=/foobar/123

# Docker
docker pull ghcr.io/malteos/data-sourcing:latest
```


