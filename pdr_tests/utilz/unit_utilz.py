"""supporting code for unit tests."""
from functools import partial

import numpy as np

import pdr
import pvl


class MockData:
    def __init__(self):
        self.LABEL = {}
        self.file_mapping = {"LABEL": "test.lbl"}

    def create_test_raster(
        self,
        array: np.ndarray,
        object_name="IMAGE",
        bounce_to="test.img"
    ):
        dtype = array.dtype.descr[0][1]
        if dtype[1] in np.typecodes["AllInteger"]:
            category = "i"
        elif dtype[1] in np.typecodes["AllFloat"]:
            category = "f"
        else:
            category = "v"
        endian = dtype[0]
        self.LABEL[object_name] = {
            "SAMPLE_TYPE": reverse_sample_types(category, endian),
            "SAMPLE_BITS": array.itemsize * 8,
            "LINES": array.shape[0],
            "LINE_SAMPLES": array.shape[1]
        }
        with open(self.file_mapping["LABEL"], "wb+") as bounce:
            pvl.dump(self.LABEL, bounce)
        self.file_mapping[object_name] = bounce_to
        with open(bounce_to, "wb+") as bounce:
            bounce.write(array.tobytes())

    @staticmethod
    def data_start_byte(*_, **__):
        return 0

    read_image = pdr.Data.read_image

    def __getattr__(self, attr):
        try:
            attr = self.__getattribute__(attr)
        except AttributeError:
            return partial(getattr(pdr.Data, attr), self)
        return attr


def reverse_sample_types(category, endian):
    if category == "f":
        return {">": "IEEE_REAL", "<": "PC_REAL"}[endian]
    if category == "i":
        return {">": "MSB_INTEGER", "<": "LSB_INTEGER"}[endian]
    if category == "v":
        return "MSB_BIT_STRING"
    raise ValueError
