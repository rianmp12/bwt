# Simple Binary Wavelet transform + Chebyshev map

This application implements the Binary Wavelet Transform combined with the Chebyshev Map and works only on single-channel images.

## Recommended Environment

It is recommended to use Python 12.5 for compatibility and optimal performance.

## Execution

*1. Create and Activate a Virtual Environment:*

``` 
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Linux/MacOS
source .venv/bin/activate
 ```
*2. Install Dependencies:*

``` 
pip install -r requirements.txt 
```

After:

Use the bwt_tests notebook to run encryption and your cryptographic tests.
You can also use the aes_tests notebook to make comparisons with the proposed algorithm.

## Troubleshooting
If issues arise, adjust the pyzmq package version:
```
python -m pip uninstall pyzmq
pip install pyzmq==25.1.2
```

Use this link for the dataset used in the notebook: https://drive.google.com/drive/folders/1OvIbDbDe3DeQ6TZSQF_XQjHltw6zp26W?usp=drive_link

## References
<a id="1">[1]</a> 
N.F. Law, W.C. Siu. 
_A filter design strategy for binary field wavelet transform using the perpendicular constraint._ 
Signal Processing 87 (2007) 2850–2858.
