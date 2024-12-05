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
Value Algorithms applied:
- standardization
Pros:
- smaller, durable, embossed with customer ID info
- Merchants could quickly imprint the plate onto a sales slip using a mechanical device, 
speeding up the transaction process and reducing errors.
- **Standardized** the format for credit transactions, allowing merchants to use a single process across customers. (compatibility, reduced (time, energy, risk from errors))
This [standardization](../../../value-algorithms/standardization.md) laid the groundwork for broader, networked credit systems like modern credit cards.
- The embossed metal design made charge plates harder to forge than handwritten or printed paper records. (increased security, decreased risk)
- Only authorized users could access credit tied to a plate, as merchants would verify the identity of the holder against the plate details.
Cons:
- Paper-based system
Dependent on: Creation of paper, Common population literacy
Pros:
Cons:
- Paper credit systems required manual recording of transactions by the merchant, which was time-consuming and prone to human error.
- Consumers often had to carry physical paper records or account books for verification.
- Lacked uniformity; each merchant or business could have their own credit note system.
- Consumers often had to maintain separate credit agreements or records with each merchant.
- Paper records could be easily forged or tampered with, posing a security risk for merchants.
- Paper was also vulnerable to loss or damage.
- Limited in scope, as they required extensive bookkeeping for each customer.
- Managing a large number of credit accounts was labor-intensive for businesses.

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

note: We have a bit of an ongoing dillema. We know that the more time a merchant gives the customer to pay, the more risk the merchant incurs and the better off
the consumer is. However, we can't really plug this into the value equation directly yet. Figuring out what we are missing.

V = 1/time+energy+capital+risk

The more time there is to pay. The more risk the merchant has, and the less risk the consumer has.




# References
https://essuir.sumdu.edu.ua/bitstream-download/123456789/25992/1/Karayew%20.pdf;jsessionid=7C45201508C4FF41BB5BC1634DE00491
