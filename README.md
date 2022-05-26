# ChatBotSemesteralWork

[![codecov](https://codecov.io/gh/KNajman/ChatBotSemesteralWork/branch/main/graph/badge.svg?token=WI6FCA78OV)](https://codecov.io/gh/KNajman/ChatBotSemesteralWork)

## Zadání

### 1. Část klientská

GUI v kterém jsou vidět zprávy a je možné zobrazit html kód
funkčnost na mobilu i na pc

### 2. Část serverová

sever běžící přes Render.com na Dockeru s podporou Flask
rozpoznávání krátkých stringů "time", "your name", "date", atd... nejsou potřeba věty
jazyky implementace: angličtina

Implementované příkazy:

- help
- time (jaký je momentální čas)
- what is your name (jak se jmenuje bot)
- kurz eura (dnešní kurz eura)
- historie eura (ode dne nasazení na server) budu si to stahovat každý den kdy výjde kurz
- endpoint hash? jednoduché zabezpečení, né jméno a heslo

## DSP (Dokument specifikace požadavků)

[DSP dokument na tomto odkaze](./DSP.md)
[Rozšíření DSP na tomto odkaze](.DSP_extension.md)
> @KNajman 2022
