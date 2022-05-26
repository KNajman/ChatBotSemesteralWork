# DSP extension

## Přídání nového funkčního požadavku

| Požadavek | Klíčové slovo/klíčová slova | Odpověď serveru | Specifikace odpovědi |
| --- | --- | --- | --- |
| doporučení nákupu EUR | "purchase", "recommendation" a "eur" | Buy / Don't buy euro because + $crit_reason | $crit_reason se vyhodnocuje pozitivně pokud kurz 3 dny klesá nebo jeho hodnotnota nestoupá o 10 % oproti 3 dennímu průměru. K odpovědi přidá vypočítaný prah ve tvaru aktuální kurz)/průměrný % |

### Závislosti funkcionality

metoda je závislá na dříve implemetovaných funkcích a to **exchange_rate** a **rate_history**

## Rozšíření funkcionality help o nový příkaz

'purchase recommendation eur'

## Předpokládané problémy implementace

- víkendový kurz a kurz o svátcích je stejný jako přecházející den, při výpočtu průměrného kurzu je tedy potřeba tyto dny nebrat v potaz
