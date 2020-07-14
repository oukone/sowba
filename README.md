## Python dev

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Install RockDB
```
pip install Cython
sudo apt install build-essential libsnappy-dev \
                zlib1g-dev libbz2-dev libgflags-dev \
                librocksdb-dev liblz4-1 liblz4-dev
pip install python-rocksdb
```

## Run

uvicorn main:app --reload