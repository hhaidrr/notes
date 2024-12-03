# Credit Cards
Credit Cards are the latest widely adopted implementation of credit-based payments.

The concept of the card is not related to credit alone. Debit cards also exist for the function of debit.

So we have primitive concepts or functions of debit and credit which have changed implementations over time.

Debit is a direct and immediate transfer of funds from the consumer to the merchant

Credit is an indirect transfer of funds that happens at a later point from the consumer to the merchant.

## Adopters
## Previous Implementation
### Debit
Coins
### Historical Implementations of Credit-based payments
- Credit Cards
- Charge plates
- Possible Paper-based system
Dependent on: Creation of paper, Common population literacy
Pros:
Cons:

- Tally sticks
- Credit-based Bartering

### Abstract
Participants: Merchant, consumer
M -> C: Assesses trustworthiness of consumer. (Inverse: risk for merchant)
M -> C: Gives valuable
M <- C: Gives Credit (Promise of equal valuable)
M * : Tracks value owed
M <- C: Gives equal valuable at a later point in time

#### Pros:
- The ability to trade without immediate payment of the consumer.
- Support for long production processes, where value is produced only after significant prior investment. Large purchases, emergency spending.

#### Cons:

Credit based payments have distinct relationships to value primitives such as time and risk. Differed payment, higher risk. 
TODO: develop functions which capture these relationships 
#### Formulae
Variables:
t = time (in seconds)
r = risk (as a probability)

What are we measuring here? We are trying to see the value a credit based system brings over a debit based system. Value is felt by the adopter of the new
system. So they will have a measurable delta between the old and the new, but not in every case since their circumstance defines whether the system
is optimal for them. There is an effect on value to each participant that adopts the new method.
Vc = value to consumer ()

There is also the relationship of delta between time of merchant sale to time of consumer payment. As this increases, does risk for the merchant increase, while
time available for the consumer increases? 
Tp = time of payment agreed to by both parties (timestamp)
Ts = time of sale (timestamp)
Tc = delta of time given to consumer (in seconds)
Pc = Probability the consumer will pay back the credit (in decimal 0 < Rm < 1)
Rm = Risk to merchant (in decimal 0 < Rm < 1)

Pc = (credit-worthiness)
Rm = 1 - Pc
Tc = Tp - Ts 




# References
https://essuir.sumdu.edu.ua/bitstream-download/123456789/25992/1/Karayew%20.pdf;jsessionid=7C45201508C4FF41BB5BC1634DE00491
