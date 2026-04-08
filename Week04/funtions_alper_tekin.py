import inspect

# 1. custom_power: Lambda fonksiyonu
# x positional-only (/ işareti öncesi), e positional-or-keyword
custom_power = lambda x=0, /, e=1: x ** e

# 2. custom_equation: Belirtilen kurallara göre detaylı fonksiyon
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Belirtilen formüle göre hesaplama yapar.

    :param x: Positional-only taban değeri.
    :param y: Positional-only taban değeri.
    :param a: x için üs değeri.
    :param b: y için üs değeri.
    :param c: Keyword-only bölen değeri.
    :return: Hesaplama sonucu (float).
    """
    return float((x**a + y**b) / c)

# 3. fn_w_counter: Çağrı sayısını ve çağıran bilgisini tutan fonksiyon
def fn_w_counter():
    # Fonksiyonun özniteliklerini (attributes) kullanarak sayacı tutuyoruz
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers = {}

    fn_w_counter.total_calls += 1
    
    # Bir üst katmandaki (çağıran) fonksiyonun adını alıyoruz
    frame = inspect.currentframe().f_back
    caller_name = frame.f_globals.get('__name__', '__main__')
    
    # Sözlükte ilgili çağıranın sayısını güncelle
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    
    return (fn_w_counter.total_calls, fn_w_counter.callers)
