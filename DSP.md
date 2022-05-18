# DSP (Dokument specifikace požadavků)

## Úvod

Cílem tohoto dokumentu je představit aplikaci chatbota rozděleného na kientskou a serverovou část a popsat jeho chování a jeho vazby na další prostředí

## Popis

### Popis systémového prostředí

Aplikace chatbota má dvě části: klientskou, která zprostředkovává grafické rozhraní pro uživatele, pro komunikaci s chatbotem a serverovou,která zpracovává dotazy a vrací odpovědi na otázky. Obě části běží odděleně a je možné je nahradit, komunikace je založena na společném inteface(rozhraní). Aplikace je přítupná veřejně na internetu, není proto potřeba inplementovat přihlašování. Základní jazyk aplikace je anglický a je možné jej rozšířit o další jazyky.

### Funkční požadavky klientské části

- Požadavek je vyvolán zadáním dotazu do inputbox a odesláním dotazu pomocí klávesy enter, či pomocí tlačítka poslat
- Posílá uživatelský vstup na server
- Zobrazuje odpověďze serveru (plaintext a html kód)
- Zobrazuje i historii konverzace (pouze do obnovení prohlížeče)
- Design webové stránky může být libovolný, důležitá je pouze  funkcionalita
- Funguje na telefonu, tabletu a PC.

![Náčrt klientské části](https://i.imgur.com/5GwnULM.png)

### Funkční požadavky servrové části

- Servrová část musí být navržena tak, aby mohla být jednoduše rozšiřitelná o další požadavky a daší jazyky

| Požadavek | Klíčové slovo/klíčová slova | Odpověď serveru | Poznámka |
| --- | --- | --- | --- |
| vypsání jména chatbota | name | Hi, nice to meet you! My name is $chatbot_name | $chatbot_name je proměná, kde bude určeno, jak se chatbot jmenuje |
| vypsání času na serveru | time | The time is $HH:MM:SS, at least at my place. | $HH:MM:SS, je proměná ukazující aktuální čas na serveru, zároveň by časměl být zobrazen v tomto fotmátu |
| vypsání kurzu EURA s možností vypsat i zpětně | exchnge rate, euro, exchange | Exchange rate is $rate CZK for 1 EUR/On $date the exchnage rate was $rate CZK for 1 EUR | proměná $rate říka kurz koruny k euru, proměná $DD.MM.YYY se řídí tím, že pokud zadal užiatel datum vypíše mu k danému dni kurz |
| vypsání nápovědy | help | Here is what I can do: -help - I tell you, what I can do - time -  I tel you, what time is it, at least at my place. - exchange rate - I tell you an exchange rate betwean EUR and CZK |  |

### Další požadavky

- Aplikace musí být přístupná pro více uživatelů najednou
- Musí mít ochranu proti velkému množsví požadavků

### Designová a implementační omezení

- hardwarové omezení - aplikace poběží na Heroku, které nabízí určité služby zdarma, aplikace je však omezena náročností
- serverová část v jazyce python + flask server
- iterface mezi serverovou a klientskou částí
- formát komunikace serveru s klientem je json (následuje ukázka, jak by měla vypadat)

```
{
    "bot_id": "1",
    "language": "en",
    "message": "Test Message",
    "image": "example.com/image.png"
}
```

- formát klienta se serverem je taktéž json (následuje ukázka, jak by měla vypadat)

```
{
    "bot_id": "1",
    "language": "en",
    "message": "Test Message",
}
```

### Závislosti

- API od ČNB na získání jednotlivých kurzů v podobě, která fungvala k 17.4.2022 na [https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt](https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt)  (ukázka jak by měl být dormát následuje)

```
14.04.2022 #74
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|16,710
Brazílie|real|1|BRL|4,769
Bulharsko|lev|1|BGN|12,488
Čína|žen-min-pi|1|CNY|3,523
Dánsko|koruna|1|DKK|3,283
EMU|euro|1|EUR|24,420
Filipíny|peso|100|PHP|43,028
Hongkong|dolar|1|HKD|2,863
Chorvatsko|kuna|1|HRK|3,230
Indie|rupie|100|INR|29,491
Indonesie|rupie|1000|IDR|1,565
Island|koruna|100|ISK|17,393
Izrael|nový šekel|1|ILS|7,001
Japonsko|jen|100|JPY|17,914
Jižní Afrika|rand|1|ZAR|1,533
Kanada|dolar|1|CAD|17,874
Korejská republika|won|100|KRW|1,830
Maďarsko|forint|100|HUF|6,486
Malajsie|ringgit|1|MYR|5,306
Mexiko|peso|1|MXN|1,131
MMF|ZPČ|1|XDR|30,691
Norsko|koruna|1|NOK|2,562
Nový Zéland|dolar|1|NZD|15,303
Polsko|zlotý|1|PLN|5,254
Rumunsko|leu|1|RON|4,937
Singapur|dolar|1|SGD|16,577
Švédsko|koruna|1|SEK|2,371
Švýcarsko|frank|1|CHF|23,966
Thajsko|baht|100|THB|66,699
Turecko|lira|1|TRY|1,535
USA|dolar|1|USD|22,451
Velká Británie|libra|1|GBP|29,458
```

- zapezpečení a stejný interface následujících opensource projektů: python, flask, javascript, pytest (pořípadě další)
- poskytování služeb následujících firem: Github, Heroku

## Testování

- 80 procent kódu musí být pokryto testy
- testy jsou automatizovány a navázány na git projekt
- k testování bude využito pytest knihovny pro python

## Rizika

- klient bude mít mnoho požadavků na poslední chvíli
- přepracovanost, kvůli ostatním projektům → nestihnutí deadlineu k dokončení projektu