BBFSA Reference

DataFrame Design
-------------

The spectra is to be considered a pandas DataFrame where the wavelength is labeled as wn and the absorbance intensity as absorbance

.. code:: python
    df.wn #wavenumber
    df.ab #absorbance intensity

baseline
--------

baseline returns a basline corrected spectra. Indexes are preserved

.. code:: python
    df.wn #wavenumber
    df.ab #baseline corrected #absorbance intensity

slice
-----
slice returns returns a sliced spectra ranging from maxWN >= to >= minWN. Indexes are destroyed

 .. code:: python
    df.wn #sliced wavenumber
    df.ab #sliced absorbance intensity

peakpickMax
-----------
returns local maximum(s)

peakpickMin
-----------
returns local minimum(s)
 