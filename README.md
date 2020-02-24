## linear_regression :rocket:
Machine learning introduction

### Hypothesis :taxi:

`Ro = b + m * o`

### Gradient descent :mountain_cableway:

```
tmp0 = p0 - lrate * (d * sum(hyp - y))
tmp1 = p1 - lrate * (d * sum((hyp - y) * X))
p0 = tmp0
p1 = tmp1
```

### Implementation :airplane:

A trainer which train a model given an datasets
> The dataset must follow this pattern:
> ```
> columns: [X, y]
> ```

A reader which predict price based on a model
> The model must follow this pattern:
> ```
> columns: [theta0, theta1, Xmin, Xmax, ymin, ymax]
> ```

### Usage :boat:

##### `python train.py`
```
usage: python train.py [-h] [--path path] [--out path] [--plot PLOT]
                [--epochs EPOCHS] [--lrate LRATE]

Train a model given a dataset

optional arguments:
  -h, --help       show this help message and exit
  --path path      must be a valid dataset path
  --out path       must be a valid output path
  --plot PLOT      plot training
  --epochs EPOCHS  number of iteration
  --lrate LRATE    number of iteration
```
##### `python predict.py`
```
usage: predict.py [-h] [--path path] [-p path] <mileage>

Predict the price given an mileage

positional arguments:
  <mileage>    must be a valid integer

optional arguments:
  -h, --help   show this help message and exit
  --path path  must be a valid model.csv path
  -p path      must be a valid model.csv path
```
