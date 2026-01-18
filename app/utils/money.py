from decimal import Decimal, ROUND_HALF_UP

MONEY_QUANT = Decimal("0.01")


def as_decimal(value: object) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value or 0))


def quantize_money(value: object) -> Decimal:
    return as_decimal(value).quantize(MONEY_QUANT, rounding=ROUND_HALF_UP)


def sum_money(values: list[object]) -> Decimal:
    total = Decimal("0")
    for item in values:
        total += as_decimal(item)
    return quantize_money(total)
