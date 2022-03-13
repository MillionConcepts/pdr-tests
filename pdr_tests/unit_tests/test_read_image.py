import random

from hypothesis import given, strategies as st
from hypothesis.extra.numpy import arrays, floating_dtypes, integer_dtypes, array_shapes
import numpy as np


from pdr_tests.utilz.unit_utilz import MockData


def test_read_image_simple():
    mock = MockData()
    arr = np.array([[1, 2, 3]], dtype="<f4")
    mock.create_test_raster(arr)
    im = mock.read_image("IMAGE")
    assert (im == arr).all()


def flip():
    return random.randint(0, 1)

rng = np.random.default_rng()


def random_elements(dtype, shape):
    try:
        info = np.iinfo(dtype)
    except ValueError:
        info = np.finfo(dtype)
    uniform = rng.random(shape)
    array = (
        info.max.astype(np.float64)
        - info.min.astype(np.float64)
    ) * uniform + info.min.astype(np.float64)
    return array.astype(dtype)


@st.composite
def various_dtypes(draw):
    byteorder = ("<", ">")[flip()]
    f = draw(floating_dtypes(endianness=byteorder))
    i = draw(integer_dtypes(endianness=byteorder))
    if flip():
        return f
    return i


random_arrays = st.builds(
    random_elements, various_dtypes(), array_shapes(min_dims=2, max_dims=2)
)


@given(input_array=random_arrays)
def test_read_image_fuzz(input_array: np.ndarray):
    mock = MockData()
    mock.create_test_raster(input_array)
    im = mock.read_image("IMAGE")
    assert (im == input_array).all()
