from logging import exception
from statistics import mean
import exchange_rate as er

def purchase_recommendation(currency : str):
    if len(currency)!=3:
        raise ValueError("Currency code must be 3 characters long")
    
    dates=er.past_5_dates()
    exchange_rates=list()
    for d in dates:
        if len(exchange_rates)<1:
            exchange_rates.append(er.exchange_rate(d,currency))
        else:
            rate_to_append=er.exchange_rate(d,currency)
            if(rate_to_append not in exchange_rates):
                exchange_rates.append(rate_to_append)    
     
    exchange_rate_mean=mean(float(str(ex).replace(",",".")) for ex in exchange_rates)   
    crit_reason=" unknown"
    
    old_rate=0.0
    for rate in exchange_rates:
        #klesá
        rate = float(str(rate).replace(",","."))
        if old_rate < rate: 
            old_rate = rate
            crit_reason="Buy euro because exchange rate is droping"
            
    #nestoupá o více jak 10 %            
    if float(str(exchange_rates[-1]).replace(",",".")) < exchange_rate_mean*1.1:
        prah = rate/exchange_rate_mean*1.1
        crit_reason = "Buy euro because exchange rate doesn't rise more than 10 % but only by " + "{:.2f}".format(prah) + " % \n"
                
    elif float(str(exchange_rates[-1]).replace(",",".")) >= exchange_rate_mean*1.1:
        prah = rate/exchange_rate_mean*1.1
        crit_reason = "Don't buy euro because rate rise more than 10 % it increased by "  + "{:.2f}".format(prah) + " % \n" 
            
    return crit_reason
    

if __name__ == "__main__":
    #print(purchase_recommendation("EUR"))
    pass