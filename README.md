# mini-vocab Projesi

## V1 GÖREVLERİ (TASKS):
1. `list` komutunu for döngüsü ile satır satır okuyacak şekilde kodlamak.
2. Kullanıcının eksik argüman girdiği durumlardaki hata mesajlarını anlaşılır ve Türkçe yapmak.
3. Listeleme çıktısını daha temiz bir formata sokmak.

## V0 -> V1 Değişiklik Özeti:
Geçen hafta (V0) listeleme işlemi yapılamıyordu. Bu sürümde (V1) "for" döngüsü kullanılarak dosyadan okuma işlemi eklendi ve `list` komutu başarıyla çalışır hale getirildi. Ayrıca genel kullanıcı deneyimi için hata mesajları iyileştirildi.

## V2 GÖREVLERİ (TASKS):
1. `search` komutu for döngüsü kullanılarak arama yapacak şekilde kodlandı.
2. `delete` komutu döngü ile dosyadan istenilen satırı silecek şekilde aktif edildi.
3. Projeye kelime öğrenme durumlarını sayan yepyeni bir `stats` komutu eklendi.

## V1 -> V2 Değişiklik Özeti:
Bu sürümde (V2) projenin işlevselliği büyük ölçüde tamamlandı. Önceki sürümlerde çalışmayan `delete` ve `search` komutları fonksiyonel hale getirildi. SPEC dosyasına yeni eklenen `stats` komutu koda uyarlandı. Ayrıca kelime silindiğinde yeni eklenen kelimelerin ID'lerinin çakışmaması için `add` komutundaki ID atama mantığı daha güvenli hale getirildi.
