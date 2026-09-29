"""Modul contoh fungsi dengan gaya penulisan sesuai PEP 8."""


def check_values(first, second, third, numbers, extra):
    """Periksa kondisi input, lalu jumlahkan nilai pertama dengan extra.

    Mengembalikan hasil penjumlahan jika semua kondisi terpenuhi,
    selain itu mengembalikan None.
    """
    if first and not second and third is None:
        return numbers[0] + extra
    return None


if __name__ == "__main__":
    print(check_values(True, False, None, [2], 3))
