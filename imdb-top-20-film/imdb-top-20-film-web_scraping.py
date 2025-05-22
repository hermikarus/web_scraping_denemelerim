import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/133.0.0.0 Safari/537.36 OPR/118.0.0.0"
    )
}

# Veri çekme ve DataFrame oluşturma fonksiyonu
def veri_cek(url, headers, limit=20):
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")

    liste = soup.find_all(
        "li",
        {"class": "ipc-metadata-list-summary-item"},
        limit=limit
    )

    kayit_tarihi = datetime.now().strftime("%d-%m-%Y")
    film_listesi = []

    for item in liste:
        film_adi = item.find("h3", {"class":"ipc-title__text"}).text
        puan = item.find("span", {"class":"ipc-rating-star--rating"}).text
        puanlama_sayisi = item.find(
            "span", class_="ipc-rating-star--voteCount"
        ).text.strip().strip("() ")
        film_yili_ve_suresi = item.find_all(
            "span",
            {"class":"sc-4b408797-8 iurwGb cli-title-metadata-item"}
        )
        film_yili = film_yili_ve_suresi[0].text
        film_suresi = film_yili_ve_suresi[1].text

        film_listesi.append({
            "Film Adı": film_adi,
            "Film Puanı": puan,
            "Puanlama Sayısı": puanlama_sayisi,
            "Film Yılı": film_yili,
            "Film Süresi": film_suresi,
            "Kayıt Tarihi": kayit_tarihi
        })

    df = pd.DataFrame(film_listesi)
    return df, kayit_tarihi

# Veri çekme ve DataFrame oluşturma
df, kayit_tarihi = veri_cek(url, headers)
klasor_adi = f"imdb-top-20-film_{kayit_tarihi}"
os.makedirs(klasor_adi, exist_ok=True)


# Dosya kaydetme fonksiyonu
def dosya_kaydet(df, klasor_adi, kayit_tarihi):
    csv_dosya = os.path.join(klasor_adi, f"imdb-top-20-film_{kayit_tarihi}.csv")
    excel_dosya = os.path.join(klasor_adi, f"imdb-top-20-film_{kayit_tarihi}.xlsx")

    try:
        df.to_csv(csv_dosya, index=False, encoding="utf-8-sig")
        df.to_excel(excel_dosya, index=False)
        print(f"Dosya kaydedildi: {csv_dosya} ve {excel_dosya}")
    except Exception as e:
        print("Dosya kaydedilirken bir hata oluştu:")
        print(f"Hata kodu: {type(e).__name__}: {e}")

dosya_kaydet(df, klasor_adi, kayit_tarihi)

# Grafik çizme fonksiyonu
def grafik_ciz(df, klasor_adi, kayit_tarihi):
    df["Film Puanı"] = df["Film Puanı"].astype(float)
    df_sorted = df.sort_values(by="Film Puanı", ascending=False)

    plt.figure(figsize=(16, 9))
    bars = plt.barh(
        df_sorted["Film Adı"],
        df_sorted["Film Puanı"],
        color="darkorange",
        edgecolor="black"
    )

    plt.xlabel("IMDb Puanı")
    plt.title(f"IMDB İLK 20 FİLM PUANLARI ({kayit_tarihi})", fontsize=14, fontweight="bold", color="black")
    plt.xlim(0, 10)
    plt.yticks(fontsize=9)              


    for i, bar in enumerate(bars):
        puan = bar.get_width()
        puanlama_sayisi = df_sorted.iloc[i]["Puanlama Sayısı"]
        plt.text(
            puan + 0.1,
            bar.get_y() + bar.get_height() / 2,
            f"{puan:.1f} puan\n{puanlama_sayisi} oy",
            va="center",
            fontsize=9
        )

    plt.tight_layout()
    grafik_dosya = os.path.join(klasor_adi, f"imdb-top-20-puan_grafik_{kayit_tarihi}.png")
    plt.savefig(grafik_dosya)
    plt.show()

    print(f"Grafik kaydedildi: {grafik_dosya}")

grafik_ciz(df, klasor_adi, kayit_tarihi)