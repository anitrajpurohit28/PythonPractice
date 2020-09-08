# commissionemployee.py
"""Commission Employee base class."""

class CommissionEmployee:
    """An employee who gets paid commission based on sales"""

    def __init__(self, first_name, last_name, ssn,
                 gross_sales, commission_rate):
        """Initialize CommissionEmployee attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self._gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        """Set gross sales or raise ValueError if invalid."""
        if sales < Decimal('0.0'):
            raise ValueError('Gross sales should be >= 0')

        self._gross_sales = sales




