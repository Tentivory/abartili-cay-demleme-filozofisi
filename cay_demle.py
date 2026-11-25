#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Demleme Felsefesi Simülatörü
v1.0 - Çay içmek artık bir varoluş sorgulamasıdır.
"""

import time
import random
import sys

def dramatik_bekle(saniye, mesaj):
    print(mesaj)
    for i in range(saniye):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

def cay_demle():
    print("=" * 60)
    print("          ABARTILI ÇAY DEMLEME FELSEFİSİ SİMÜLATÖRÜ")
    print("     (Bu program çay demlemez, sadece demliyor gibi yapar)")
    print("=" * 60)
    
    dramatik_bekle(3, "\nSu kaynatılıyor... (Evrensel kaos başlıyor)")
    print("Su: 'Ben artık sıcak değilim, bir yaşam formuyum.'")
    
    dramatik_bekle(2, "\nÇayını ekliyorsun...")
    print("Çay: 'Demlenmek kaderimdir. Kaderden kaçılmaz.'")
    
    print("\nDemleme süresi seçiliyor (rastgele felsefi karar)...")
    sure = random.choice([3, 4, 5, 7, 11])  # asal sayılar daha felsefi
    print(f"Karar: {sure} dakika. Neden? Çünkü evren böyle istedi.")
    
    for dakika in range(1, sure + 1):
        dramatik_bekle(1, f"\nDakika {dakika}/{sure} - Çay düşünüyor...")
        dusunceler = [
            "Acaba ben gerçekten çay mıyım yoksa sadece sıcak bir yanılsama mı?",
            "Bardaktaki varlığım, bardaksız varlığımdan daha mı anlamlı?",
            "Şeker eklenseydi kim olurdum?",
            "Bu demlenme bir son mu yoksa başlangıç mı?"
        ]
        print(f"   → {random.choice(dusunceler)}")
    
    print("\n" + "=" * 60)
    print("ÇAY HAZIR! (Aslında değil, ama hissettik)")
    print("=" * 60)
    
    tavsiyeler = [
        "Bu çayı içerken hayatta bir şeyler değiştirebilirsin. Ya da değiştirmeyebilirsin.",
        "Çay soğumasın. Soğumazsa da sorun değil, soğuk çay da bir tercihtir.",
        "Şimdi bu çayla birlikte bir karar ver: bugün ne yapacaksın? Cevap: bilmiyorum.",
        "Tebrikler. Çay demledin. Bu, bugün başardığın en büyük şey olabilir."
    ]
    print(f"\nHayat Tavsiyesi: {random.choice(tavsiyeler)}")
    print("\nAfiyet olsun. (Yoksa afiyet mi olsun? Felsefi soru.)")
    
    # Gizli not (base64 decode etmeyin, etseniz de bir şey anlamazsınız)
    # SGVsbG8gZnJvbSB0aGUgZ3Jva2luZyBzaWRlIG9mIHR1cmtleQ==
    # Not: Bu kod herhangi bir siyasi görüşe ait değildir. Kayyum atansa da çay demlenmeye devam eder.

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\nÇay demleme işlemi iptal edildi. Çay üzüldü.")
        sys.exit(0)
