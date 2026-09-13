# Marmara Üniversitesi Alt Site Tarama Raporu

- Taranan toplam host: **122**
- main.py'nin scraper yapısıyla (`div.blog-pull-right` > `div.row.mb-15` > `h4`+`h6`+`a`) birebir eşleşen: **97**
- Duyuru sayfası bulundu ama yapı farklı: **24**
- Erişilemeyen/hata veren: **1**

Not: Tarama, www.marmara.edu.tr ana sayfasının menü/footer linklerinden çıkarılan 122 alt alan adını kapsıyor; kapsam tamamen ana sayfada linklenenlerle sınırlı, bundan daha derin bir keşif yapılmadı.

## Sonuç Tablosu

| Host | Denenen URL | HTTP Durumu | main.py yapısıyla eşleşti mi | Notlar |
|---|---|---|---|---|
| adalet.marmara.edu.tr | https://adalet.marmara.edu.tr/allnotices | 200 | Evet | 7 duyuru bloğu, 5 örnek h4+a eşleşti |
| aday.marmara.edu.tr | https://aday.marmara.edu.tr/allnotices | 200 | Evet | 10 duyuru bloğu, 5 örnek h4+a eşleşti |
| aef.marmara.edu.tr | https://aef.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| akademikgelisim.marmara.edu.tr | https://akademikgelisim.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| anket.marmara.edu.tr | https://anket.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right konteyneri yok |
| ataturkilkeleri.marmara.edu.tr | https://ataturkilkeleri.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| avesis.marmara.edu.tr | https://avesis.marmara.edu.tr/ | 200 | Hayır | blog-pull-right konteyneri yok |
| avrupa.marmara.edu.tr | https://avrupa.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| bap.marmara.edu.tr | https://bap.marmara.edu.tr/ | ERR:ConnectTimeout | Hayır |  |
| bapko.marmara.edu.tr | https://bapko.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| bidb.marmara.edu.tr | https://bidb.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| bilgiguvenligi.marmara.edu.tr | https://bilgiguvenligi.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| bse.marmara.edu.tr | https://bse.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| bursofisi.marmara.edu.tr | https://bursofisi.marmara.edu.tr/allnotices | 200 | Evet | 6 duyuru bloğu, 5 örnek h4+a eşleşti |
| bys.marmara.edu.tr | https://bys.marmara.edu.tr/v2/Account/Login?ReturnUrl=%2Fv2%2F | 200 | Hayır | blog-pull-right konteyneri yok |
| csuam.marmara.edu.tr | https://csuam.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| cumhuriyetmuzesi.marmara.edu.tr | https://cumhuriyetmuzesi.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| dbb.marmara.edu.tr | https://dbb.marmara.edu.tr/allnotices | 200 | Evet | 5 duyuru bloğu, 5 örnek h4+a eşleşti |
| dehamer.marmara.edu.tr | https://dehamer.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| destek.marmara.edu.tr | https://destek.marmara.edu.tr/Common/ErrorPage | 200 | Hayır | blog-pull-right konteyneri yok |
| dhf.marmara.edu.tr | https://dhf.marmara.edu.tr/allnotices | 200 | Evet | 5 duyuru bloğu, 5 örnek h4+a eşleşti |
| diploma.marmara.edu.tr | https://diploma.marmara.edu.tr/ | 200 | Hayır | blog-pull-right konteyneri yok |
| dobisu.marmara.edu.tr | https://dobisu.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| dsim.marmara.edu.tr | https://dsim.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| e-rehber.marmara.edu.tr | https://e-rehber.marmara.edu.tr/ | 200 | Hayır | blog-pull-right konteyneri yok |
| ebe.marmara.edu.tr | https://ebe.marmara.edu.tr/allnotices | 200 | Evet | 10 duyuru bloğu, 5 örnek h4+a eşleşti |
| ebys.marmara.edu.tr | https://ebys.marmara.edu.tr/enVision/Login.aspx | 200 | Hayır | blog-pull-right konteyneri yok |
| eczacilik.marmara.edu.tr | https://eczacilik.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| eng.marmara.edu.tr | https://eng.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| eob.marmara.edu.tr | https://eob.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| eskar.marmara.edu.tr | https://eskar.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| esks.marmara.edu.tr | https://esks.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right konteyneri yok |
| euam.marmara.edu.tr | https://euam.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| farabi.marmara.edu.tr | https://farabi.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| fbe.marmara.edu.tr | https://fbe.marmara.edu.tr/allnotices | 200 | Evet | 5 duyuru bloğu, 5 örnek h4+a eşleşti |
| fbf.marmara.edu.tr | https://fbf.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| fef.marmara.edu.tr | https://fef.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| fen.marmara.edu.tr | https://fen.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| gastro.marmara.edu.tr | https://gastro.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| gemham.marmara.edu.tr | https://gemham.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| gonullu.marmara.edu.tr | https://gonullu.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| gse.marmara.edu.tr | https://gse.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| gsf.marmara.edu.tr | https://gsf.marmara.edu.tr/allnotices | 200 | Evet | 7 duyuru bloğu, 5 örnek h4+a eşleşti |
| hipam.marmara.edu.tr | https://hipam.marmara.edu.tr/allnotices | 200 | Evet | 2 duyuru bloğu, 2 örnek h4+a eşleşti |
| hukuk.marmara.edu.tr | https://hukuk.marmara.edu.tr/allnotices | 200 | Evet | 12 duyuru bloğu, 5 örnek h4+a eşleşti |
| hukukmusavirligi.marmara.edu.tr | https://hukukmusavirligi.marmara.edu.tr/allnotices | 200 | Evet | 2 duyuru bloğu, 2 örnek h4+a eşleşti |
| icdenetim.marmara.edu.tr | https://icdenetim.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| ics.marmara.edu.tr | https://ics.marmara.edu.tr/allnotices | 200 | Evet | 6 duyuru bloğu, 5 örnek h4+a eşleşti |
| ikf.marmara.edu.tr | https://ikf.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| ilahiyat.marmara.edu.tr | https://ilahiyat.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| iletisim.marmara.edu.tr | https://iletisim.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| imidb.marmara.edu.tr | https://imidb.marmara.edu.tr/allnotices | 200 | Evet | 6 duyuru bloğu, 5 örnek h4+a eşleşti |
| isg.marmara.edu.tr | https://isg.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| isletme.marmara.edu.tr | https://isletme.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| itbf.marmara.edu.tr | https://itbf.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| kalite.marmara.edu.tr | https://kalite.marmara.edu.tr/allnotices | 200 | Evet | 8 duyuru bloğu, 5 örnek h4+a eşleşti |
| kampuskart.marmara.edu.tr | https://kampuskart.marmara.edu.tr/allnotices | 200 | Evet | 5 duyuru bloğu, 5 örnek h4+a eşleşti |
| kariyermerkezi.marmara.edu.tr | https://kariyermerkezi.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| katalog.marmara.edu.tr | https://katalog.marmara.edu.tr/ | 200 | Hayır | blog-pull-right konteyneri yok |
| keyem.marmara.edu.tr | https://keyem.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| korumaguvenlik.marmara.edu.tr | https://korumaguvenlik.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| kurumsaliletisim.marmara.edu.tr | https://kurumsaliletisim.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| kutuphane.marmara.edu.tr | https://kutuphane.marmara.edu.tr/allnotices | 200 | Evet | 12 duyuru bloğu, 5 örnek h4+a eşleşti |
| kvkk.marmara.edu.tr | https://kvkk.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| lab.marmara.edu.tr | https://lab.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| mabkam.marmara.edu.tr | https://mabkam.marmara.edu.tr/allnotices | 200 | Evet | 5 duyuru bloğu, 5 örnek h4+a eşleşti |
| macok.marmara.edu.tr | https://macok.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| makam.marmara.edu.tr | https://makam.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| marahekuyam.marmara.edu.tr | https://marahekuyam.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| marmaratto.marmara.edu.tr | https://marmaratto.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| marpam.marmara.edu.tr | https://marpam.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| mehmetgencitam.marmara.edu.tr | https://mehmetgencitam.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| mezun.marmara.edu.tr | https://mezun.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| mitto.marmara.edu.tr | https://mitto.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| mtf.marmara.edu.tr | https://mtf.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| muisef.marmara.edu.tr | https://muisef.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| mukam.marmara.edu.tr | https://mukam.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| mupress.marmara.edu.tr | https://mupress.marmara.edu.tr/allnotices | 200 | Evet | 10 duyuru bloğu, 5 örnek h4+a eşleşti |
| murcir.marmara.edu.tr | https://murcir.marmara.edu.tr/allnotices | 200 | Evet | 10 duyuru bloğu, 5 örnek h4+a eşleşti |
| musem.marmara.edu.tr | https://musem.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right konteyneri yok |
| muvem.marmara.edu.tr | https://muvem.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| nbe.marmara.edu.tr | https://nbe.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| nbuam.marmara.edu.tr | https://nbuam.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| nsa.marmara.edu.tr | https://nsa.marmara.edu.tr/allnotices | 200 | Evet | 13 duyuru bloğu, 5 örnek h4+a eşleşti |
| nsp.marmara.edu.tr | https://nsp.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| oae.marmara.edu.tr | https://oae.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| ogrencikonseyi.marmara.edu.tr | https://ogrencikonseyi.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| oidb.marmara.edu.tr | https://oidb.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| online.marmara.edu.tr | https://online.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| oyp.marmara.edu.tr | https://oyp.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| pbys.marmara.edu.tr | https://pbys.marmara.edu.tr/v2/Account/Login?ReturnUrl=%2Fv2%2FDashboard | 200 | Hayır | blog-pull-right konteyneri yok |
| pdb.marmara.edu.tr | https://pdb.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| posta.marmara.edu.tr | https://posta.marmara.edu.tr/ | 200 | Hayır | blog-pull-right konteyneri yok |
| saglik.marmara.edu.tr | https://saglik.marmara.edu.tr/allnotices | 200 | Evet | 5 duyuru bloğu, 5 örnek h4+a eşleşti |
| sayilarla.marmara.edu.tr | https://sayilarla.marmara.edu.tr/ | 200 | Hayır | blog-pull-right konteyneri yok |
| sbe.marmara.edu.tr | https://sbe.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| sbf.marmara.edu.tr | https://sbf.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| sbmyo.marmara.edu.tr | https://sbmyo.marmara.edu.tr/allnotices | 200 | Evet | 11 duyuru bloğu, 5 örnek h4+a eşleşti |
| sbssuam.marmara.edu.tr | https://sbssuam.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| sgdb.marmara.edu.tr | https://sgdb.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| shmyo.marmara.edu.tr | https://shmyo.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| siyasal.marmara.edu.tr | https://siyasal.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| sks.marmara.edu.tr | https://sks.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| sosyaltesis.marmara.edu.tr | https://sosyaltesis.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| sporbilimleri.marmara.edu.tr | https://sporbilimleri.marmara.edu.tr/allnotices | 200 | Evet | 1 duyuru bloğu, 1 örnek h4+a eşleşti |
| stkam.marmara.edu.tr | https://stkam.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| sustainability.marmara.edu.tr | https://sustainability.marmara.edu.tr/allnotices | 200 | Evet | 11 duyuru bloğu, 5 örnek h4+a eşleşti |
| takvim.marmara.edu.tr | https://takvim.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right konteyneri yok |
| tbmyo.marmara.edu.tr | https://tbmyo.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| tef.marmara.edu.tr | https://tef.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| teknoloji.marmara.edu.tr | https://teknoloji.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| tip.marmara.edu.tr | https://tip.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| tomer.marmara.edu.tr | https://tomer.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| turkdili.marmara.edu.tr | https://turkdili.marmara.edu.tr/allnotices | 200 | Hayır | blog-pull-right var ama row.mb-15 yok |
| turkiyat.marmara.edu.tr | https://turkiyat.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| ubf.marmara.edu.tr | https://ubf.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| uluslararasi.marmara.edu.tr | https://uluslararasi.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| uzem.marmara.edu.tr | https://uzem.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
| www.marmara.edu.tr | https://www.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| yapi.marmara.edu.tr | https://yapi.marmara.edu.tr/allnotices | 200 | Evet | 15 duyuru bloğu, 5 örnek h4+a eşleşti |
| ydil.marmara.edu.tr | https://ydil.marmara.edu.tr/allnotices | 200 | Evet | 4 duyuru bloğu, 4 örnek h4+a eşleşti |
| yiasm.marmara.edu.tr | https://yiasm.marmara.edu.tr/allnotices | 200 | Evet | 3 duyuru bloğu, 3 örnek h4+a eşleşti |
