# Analyze Data

## Build your docker container 
```
docker build . -t log_analysis_me
```

## Then run passing a path arguments to your text file (default: ./logs/logs.txt)

```
docker run -v $(pwd):/log_analysis log_analysis_me --path=./logs/foo.txt
```

# Suit tests

To run suit test just: 
```shell
    python3 analysis_test.py
```

