import torch

from . import common_utils
from .kaldi_compatibility_impl import Kaldi


@common_utils.skipIfNoCuda
class TestKaldiFloat32(Kaldi, common_utils.TestCase):
    dtype = torch.float32
    device = torch.device('cuda')


@common_utils.skipIfNoCuda
class TestKaldiFloat64(Kaldi, common_utils.TestCase):
    dtype = torch.float64
    device = torch.device('cuda')
