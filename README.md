# cipher_yx2625

A basic text ciphering package

## Installation

Make sure you are downloading this package with **Python3.9 or above** 
```bash
$ pip install cipher_yx2625
```

## Usage

This package is somewhat simple. It applies caesarian ciphering method to shift text by a specified number of positions right (if the shift parameter is positive) or left (if the shift parameter is negative). 

```python:
import cipher_yx2625 from cipher_yx2625

#c all cipher function from cipher_yx2625. 
cipher_yx2625.cipher('Harry', 3) // => 'KduuB'
cipher_yx2625.cipher('H=rmione',-10) // => 'x=hcYedU'
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`cipher_yx2625` was created by Ye (Connie) Xu. It is licensed under the terms of the MIT license.

## Credits

`cipher_yx2625` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
