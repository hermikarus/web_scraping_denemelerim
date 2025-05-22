Bu proje, IMDB Top 250 listesinin ilk 20 filmini Python kullanarak otomatik olarak çekip, yapılandırılmış veri dosyalarına kaydeder ve verileri görsel olarak analiz eder.

Amaç, IMDB’nin güncel "Top 250" listesindeki en yüksek puanlı 20 filmin:
+ Adı
+ IMDB puanı
+ Toplam oy sayısı
+ Yayın yılı
+ Süresi
gibi temel bilgileri çekmek, bunları .csv ve .xlsx formatlarında saklamak ve IMDB puanlarını görselleştirerek analiz kolaylığı sağlamaktır.

Özellikler:
+ IMDB web sitesinden HTML içeriği requests ve BeautifulSoup ile dinamik olarak alınır.
+ Çekilen veriler pandas ile işlenerek temiz bir DataFrame formatına dönüştürülür.
+ Her çalıştırmada kayıt tarihiyle isimlendirilmiş bir klasör oluşturulur.
+ Veriler .csv ve .xlsx dosyaları olarak kaydedilir.
+ IMDB puanları yatay bar grafiğiyle görselleştirilir (matplotlib).
+ Her barın ucunda puan ve toplam oy sayısı etiketlenir.
+ Grafik .png formatında aynı klasöre kaydedilir

Kullanılan Kütüphaneler:

+ requests – IMDB sayfasından HTML içeriğini almak için
+ BeautifulSoup – HTML içeriğini parse edip veri çıkarmak için
+ pandas – Verileri tabloya dönüştürmek ve .csv / .xlsx formatlarında kaydetmek için
+ datetime – Kayıt tarihini dinamik olarak almak için
+ os – Klasör ve dosya işlemleri için
+ matplotlib – IMDB puanlarını bar grafiği olarak görselleştirmek için

İleride bu klasör, IMDB dışındaki diğer web sitelerinden çekilecek verileri de içerecek şekilde genişletilebilir.
Kod dosyası imdb-top-20-film-web_scraping.py ismiyle bu klasörde yer almaktadır.
