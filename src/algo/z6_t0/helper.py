from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    return Fraction(( f1.numer * f2.denom + f2.numer * f1.denom), (f1.denom * f2.denom))
