# Data-Analytics-Development-Problem
Data Analytics Development Problem of shopify

# problem statement
On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

What to submit: Which metric you would report for this dataset, and its value in dollars.


#solution
Hello :) :)

AOV the  average order value is caluclated as the total revenue divided by the #orders. However, after inspetion of the data, I noticed that there 
are two types of customers. Businesses usally requesting in thousands and normal clients requesting in under a dozen.

After splitting the data into B2B and B2C, I have calculated the AOV for both and got the following results:


#('AOV of B2B is ', 704000.0)
#('AOV of B2C is ', 754.0919125025085)

Seems more reasonable for B2C now.

Thank you for your time and consideration

Sincerely,

Elias Al Homsi
elias.alhomsi@mail.mcgill.ca
