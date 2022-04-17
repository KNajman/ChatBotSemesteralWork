# ChatBotSemesteralWork

## Zadání

### 1. Část klientská

GUI kde jsou vidět zprávy a je možné zobrazit html kód
funkčnost na mobilu i na pc

### 2. Část serverová

nejhorší možné řešení na local hostu, ideálně třeba Docker
rozpoznávání krátkých stringů "time", "your name", "date", atd... nejsou potřeba věty
příkazy k implementování:
-help
-time (jaký je momentální čas)
-what is your name (jak se jmenuje bot)
-kurz eura (dnešní kurz eura)
-historie eura (ode dne nasazení na server) budu si to stahovat každý den kdy výjde kurz
-jazyk implementace libovolný mezi angličtinou a češtinou
-endpoint hash? jednoduché zabezpečení, né jméno a heslo

### Požadavky zákazníka

Serverový chatbot, s přístupem v prohlížečí, který bude  odpovídat na dotazy v anglickém jazyce nebo českém.
Design webové stránky může být libovolný, důležitá je pouze  funkcionalita. Musí však fungovat jak na telefonu, tabletu tak i na PC. Historii chatu si klient nepřeje.

Dotazy budou:

- help (na jaké dotazy dokáže bot odpovědět)
- time (jaký je momentální serverový čas)
- what is your name (jak se jmenuje bot)
- euro exchange rate (dnešní kurz eura vůči české koruně)

Dotazy má být možno jednoduše přidat a také modifikovat např. z EUR udělat USD apod.

## DSP (Dokument specifikace požadavků)
[DSP dokument na tomto odkaze](./DSP.md)

> @KNajman 2022
