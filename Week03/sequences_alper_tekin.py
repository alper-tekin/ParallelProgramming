def remove_duplicates(seq: list) -> list:
    """
    Bu fonksiyon bir listedeki mükerrer (tekrar eden) öğeleri kaldırır.
    Sıralamayı korumak için dict.fromkeys kullanılmıştır.
    """
    return list(dict.fromkeys(seq))

def list_counts(seq: list) -> dict:
    """
    Bu fonksiyon bir listedeki her bir öğenin kaç kez geçtiğini sayar.
    """
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(d: dict) -> dict:
    """
    Bu fonksiyon bir sözlüğün anahtarlarını (keys) ve değerlerini (values) tersine çevirir.
    Not: Eğer birden fazla aynı değer varsa, sonuncusu anahtar olur.
    """
    return {value: key for key, value in d.items()}

