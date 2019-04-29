import numpy as np
import timeit

import pytest

from src.invoice_stats import InvoiceStats, ArrayList, InvoiceStatsSorted
from utils.utils import get_size

from collections import deque


@pytest.fixture
def arg(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def example_invoices():
    n = int(1e5)
    return np.random.randint(0, 2e10, dtype=np.int64, size=n)


@pytest.fixture
def example_invoice_stats_list(example_invoices):
    ivs = InvoiceStats([])
    ivs.add_invoices(example_invoices)
    return ivs


@pytest.fixture
def example_invoice_stats_al(example_invoices):
    ivs = InvoiceStats(ArrayList())
    ivs.add_invoices(example_invoices)
    return ivs


@pytest.fixture
def example_invoice_stats_deque(example_invoices):
    ivs = InvoiceStats(deque())
    ivs.add_invoices(example_invoices)
    return ivs


@pytest.fixture
def example_invoice_stats_sorted(example_invoices):
    ivs = InvoiceStatsSorted()
    ivs.add_invoices(example_invoices)
    return ivs


# @pytest.mark.parametrize('arg', ['example_invoice_stats_sorted', 'example_invoice_stats_al', 'example_invoice_stats_list'], indirect=True)
@pytest.mark.parametrize('arg', ['example_invoice_stats_al'], indirect=True)
def test_invoice_stats_array_list(arg):
    number = 100
    print("=========== " + str(arg))
    print("Memory Size = " + str(get_size(arg)))
    print("using partition = " + str(arg.get_median()))
    print("time = " + str(timeit.timeit(arg.get_median, number=number)))
    print("numpy  = " + str(arg.get_median_np()))
    print("time = " + str(timeit.timeit(arg.get_median_np, number=number)))


def test_sorted(example_invoice_stats_sorted):
    print(example_invoice_stats_sorted.get_mean())


def test_sorted2(example_invoice_stats_sorted):
    print(example_invoice_stats_sorted.get_median())
    print(example_invoice_stats_sorted.get_median_np())


def test_add_invoice(example_invoice_stats_list):
    pass


def test_add_invoices():
    pass


def test_clear():
    pass


def test_median():
    pass


def test_mean(example_invoice_stats_list):
    print("mean_np = " + str(example_invoice_stats_list.get_mean_np()))
    print("mean = " + str(example_invoice_stats_list.get_mean()))
