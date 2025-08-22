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

<a id="2">[2]</a> 
Pan, H.; Siu, W.-C.; Law, N.-F. 
_Lossless Image Compression Using Binary Wavelet Transform._ 
IET Image Processing 2007, 1, 353. https://doi.org/10.1049/iet-ipr:20060195.

<a id="3">[3]</a> 
Lorenz, E.N. 
_Predictability: Does the Flap of a Butterfly’s Wings in Brazil Set Off a Tornado in Texas?_ 
Proceedings of the American Association for the Advancement of Science, Washington, D.C., USA, 1972.

<a id="4">[4]</a> 
Swanson, M.D.; Tewfik, A.H. 
_A Binary Wavelet Decomposition of Binary Images._ 
Proceedings of the 1996 IEEE International Conference on Acoustics, Speech, and Signal Processing, 1996. https://doi.org/10.1109/ICASSP.1996.545984.

<a id="5">[5]</a> 
Kumari, M.; Gupta, S.; Sardana, P. 
_A Survey of Image Encryption Algorithms._ 
3D Research 2017, 8, 4. https://doi.org/10.1007/s13319-017-0148-5.

<a id="6">[6]</a> 
Silva, B.; Almeida, H.P.; Oliveira, C.C.; Oliveira, D.C. 
_Asymmetric Image Encryption Using the RSA Algorithm._ 
Universidade de Uberaba and Universidade Federal de Uberlândia, 2013. Available online: https://peteletricaufu.com.br/static/ceel/doc/artigos/artigos2013/ceel2013_029.pdf (accessed on 20 August 2025).

<a id="7">[7]</a> 
Chang, C.-C.; Hwang, M.-S.; Chen, T.-S. 
_A New Encryption Algorithm for Image Cryptosystems._ 
Journal of Systems and Software 2001, 58, 83–91. https://doi.org/10.1016/s0164-1212(01)00029-2.

<a id="8">[8]</a> 
Raj, R.; Paul, S. 
_Image Encryption Using Chaotic Maps of Various Dimensions: Review._ 
International Journal of Research in Engineering and Technology 2016, 5, 94–96. Available online: http://ijret.esatjournals.org (accessed on 20 August 2025).

<a id="9">[9]</a> 
Rosen, J.; Scherr, Z.; Weiss, B.; Zieve, M.E. 
_Chebyshev Mappings of Finite Fields._ 
Am. Math. Mon. 2012, 119, 151. https://doi.org/10.4169/amer.math.monthly.119.02.151.

<a id="10">[10]</a> 
Yoon, E.-J.; Jeon, I.-S. 
_An Efficient and Secure Diffie–Hellman Key Agreement Protocol Based on Chebyshev Chaotic Map._ 
Commun. Nonlinear Sci. Numer. Simul. 2011, 16, 2383–2389. https://doi.org/10.1016/j.cnsns.2010.09.021.

<a id="11">[11]</a> 
Attaullah; Javeed, A.; Shah, T. 
_Cryptosystem Techniques Based on the Improved Chebyshev Map: An Application in Image Encryption._ 
Multimed. Tools Appl. 2019. https://doi.org/10.1007/s11042-019-07981-8.

<a id="12">[12]</a> 
Kuznetsov, N.V. 
_The Lyapunov Dimension and Its Estimation via the Leonov Method._ 
Phys. Lett. A 2016, 380, 2142–2149. https://doi.org/10.1016/j.physleta.2016.04.036.

<a id="13">[13]</a> 
Orrell, D.; Smith, L.A. 
_Visualizing Bifurcations in High Dimensional Systems: The Spectral Bifurcation Diagram._ 
Int. J. Bifurcat. Chaos 2003, 13, 3015–3027. https://doi.org/10.1142/s0218127403008387.
