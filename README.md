# moto-issue

## Steps to reproduce

Set up environment:

```
mamba create -n moto-issue python=3.9
mamba activate moto-issue
pip install -r requirements.txt
```

Run tests:

```
pytest tests/
```

Demo with a real table:

```
export AWS_PROFILE=<profile>
python create_table.py
python update_item.py
```
