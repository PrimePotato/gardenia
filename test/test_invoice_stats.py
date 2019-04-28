import numpy as np
import timeit

import pytest
import sys

from src.invoice_stats import InvoiceStats, InvoiceStatsAl


@pytest.fixture
def example_invoices():
    n = int(1e4)
    return np.random.randint(0, 2000000000000000, dtype=np.int64, size=n)


def test_invoice_stats(example_invoices):
    ivs = InvoiceStats()
    for x in example_invoices:
        ivs.add_invoice(x)


def test_invoice_stats2(example_invoices):
    ivs = InvoiceStats()
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
