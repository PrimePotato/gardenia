import numpy as np
import math

from sortedcontainers import SortedList


class InvalidInvoiceException(BaseException):
    pass


class InvoiceStats(object):
    # Designed to work with different unsorted data containers
    def __init__(self, data_container):
        self._invoices = data_container
        self._total = 0
        self._n = 0
        self._mean = 0

    @staticmethod
    def convert_validate_invoice_to_int(v):
        if (np.int64(100 * v) - 100 * v) > 1e-15:
            raise InvalidInvoiceException("Invalid invoice = " + str(v) + " " + str((np.int64(100 * v) - v)))
        return np.int64(100 * v)

    def add_invoices(self, invoices):
        for v in invoices:
            self.add_invoice(v)

    def add_invoice(self, invoice):
        v = InvoiceStats.convert_validate_invoice_to_int(invoice)
        self._n += 1
        self._invoices.append(v)
        self._total += v
        self._mean = self._mean * ((self._n - 1) / self._n) + (v / self._n)

    def clear(self):
        self._n = 0
        self._total = 0
        self._mean = 0
        self._invoices.clear()

    def get_median_np(self):
        return np.median(self._invoices) / 100

    def get_median(self):
        m = (len(self._invoices) - 1) / 2
        c = math.ceil(m)
        f = math.floor(m)
        ary = np.array(self._invoices)
        ary.partition((c, f))
        return (ary[c] + ary[f]) / 200

    def get_mean_np(self):
        return np.mean(self._invoices) / 100

    def get_mean(self):
        return self._mean / 100


class InvoiceStatsSorted(InvoiceStats):
    # Using a sorted container, which speeds up the median calc but slows insertion
    def __init__(self):
        super().__init__(SortedList())

    def add_invoice(self, invoice):
        v = InvoiceStats.convert_validate_invoice_to_int(invoice)
        self._n += 1
        self._invoices.add(v)
        self._total += v
        self._mean = self._mean * ((self._n - 1) / self._n) + (v / self._n)

    def get_median(self):
        m = (len(self._invoices) - 1) / 2
        c = math.ceil(m)
        f = math.floor(m)
        return (self._invoices[c] + self._invoices[f]) / 200


class ArrayList(object):
    def __init__(self):
        self.idx = 0
        self.base_len = 2
        self._base = np.array([0] * self.base_len, dtype=np.int64)

    def __len__(self):
        return self.idx + 1

    def append(self, x):
        if self.idx + 1 > self.base_len:
            self.base_len *= 2
            self._base = np.append(self._base, np.array([0] * self.base_len, dtype=np.int64))
        self._base[self.idx] = x
        self.idx += 1

    def __array__(self):
        return self._base[0:self.idx]

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        yield self._base[self.i]
        self.i += 1
