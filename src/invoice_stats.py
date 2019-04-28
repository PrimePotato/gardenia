import numpy as np
import math


class InvoiceStats(object):
    def __init__(self):
        self._invoices = []

    def add_invoices(self, invoices):
        self._invoices.append(invoices)

    def add_invoice(self, invoice):
        self._invoices.append(invoice)

    def clear(self):
        self._invoices.clear()

    def get_median_np(self):
        return np.median(self._invoices)

    def get_median(self):
        m = (len(self._invoices) - 1) / 2
        c = math.ceil(m)
        f = math.floor(m)
        ary = np.array(self._invoices)
        ary.partition([c, f])
        return (ary[c] + ary[f]) / 2

    def get_mean(self):
        return np.mean(self._invoices)


class InvoiceStatsAl(object):
    def __init__(self):
        self._invoices = ArrayList()

    def add_invoices(self, invoices):
        self._invoices.append(invoices)

    def add_invoice(self, invoice):
        self._invoices.append(invoice)

    def clear(self):
        self._invoices.clear()

    def get_median_np(self):
        return np.median(self._invoices.to_array())

    def get_median(self):
        m = (len(self._invoices)) / 2
        c = math.ceil(m) - 1
        f = math.floor(m) - 1
        ary = self._invoices.to_array()
        ary.partition([c, f])
        return (ary[c] + ary[f]) / 2

    def get_mean(self):
        return np.mean(self._invoices)


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

    def to_array(self):
        return self._base[0:self.idx]




