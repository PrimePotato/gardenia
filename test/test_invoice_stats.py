import numpy as np
import timeit

import pytest
import sys

from src.invoice_stats import InvoiceStats


@pytest.fixture
def example_invoices():
    n = int(1e5)
    return np.random.randint(0, 2e10, dtype=np.int64, size=n)


@pytest.fixture
def example_invoice_stats(example_invoices):
    ivs = InvoiceStats()
    ivs.add_invoices(example_invoices)
    return ivs


@pytest.fixture
def example_invoice_stats_al(example_invoices):
    ivs = InvoiceStats()
    ivs.add_invoices(example_invoices)
    return ivs


def test_invoice_stats(example_invoices):
    ivs = InvoiceStats()
    for x in example_invoices:
        ivs.add_invoice(x)


#
# def test_invoice_stats(example_invoices):
#     ivs = InvoiceStats()
#     for x in example_invoices:
#         ivs.add_invoice(x)


def test_invoice_stats2(example_invoices):
    ivs = InvoiceStats()
    print("Memory = " + str(get_size(ivs)))

    ivs.add_invoices(example_invoices)

    print("Memory = " + str(get_size(ivs)))
    # print(timeit.timeit(lambda _: ivs.add_invoices(example_invoices), number=1))

    number = 100
    print("===========")
    print("mine = " + str(ivs.get_median()))
    print("time = " + str(timeit.timeit(ivs.get_median, number=number)))

    # print(timeit.timeit("np_mean = " + ivs.get_mean, number=number))

    print("numpy  = " + str(ivs.get_median_np()))
    print("time = " + str(timeit.timeit(ivs.get_median_np, number=number)))
    # print("meen np = " + ivs.get_mean())
#
#
# def test_invoice_stats4(example_invoice_stats):
#     print("Memory = " + str(sys.getsizeof(example_invoice_stats)))
#     # print(timeit.timeit(lambda _: ivs.add_invoices(example_invoices), number=1))
#
#     number = 100000
#     print("===========")
#     print("mine = " + str(example_invoice_stats.get_median()))
#     print("time = " + str(timeit.timeit(example_invoice_stats.get_median, number=number)))
#
#     # print(timeit.timeit("np_mean = " + ivs.get_mean, number=number))
#
#     print("numpy  = " + str(example_invoice_stats.get_median_np()))
#     print("time = " + str(timeit.timeit(example_invoice_stats.get_median_np, number=number)))
#     # print("meen np = " + ivs.get_mean())
#

def test_invoice_stats3(example_invoices):
    ivs = InvoiceStatsAl()
    ivs.add_invoices(example_invoices)
    # print(timeit.timeit(lambda _: ivs.add_invoices(example_invoices), number=1))

    number = 100000
    print("===========")
    print("mine = " + str(ivs.get_median()))
    print("time = " + str(timeit.timeit(ivs.get_median, number=number)))

    # print(timeit.timeit("np_mean = " + ivs.get_mean, number=number))

    print("numpy  = " + str(ivs.get_median_np()))
    print("time = " + str(timeit.timeit(ivs.get_median_np, number=number)))
    # print("meen np = " + ivs.get_mean())


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size