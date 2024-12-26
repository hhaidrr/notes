# IoT payments

### **2. Parking Lots and Garages**
- **Scenario:** Payment terminals for parking are often located at exit gates or kiosks, requiring consumers to get out of their car or lean out of the window.
- **Effort Involved:** Reaching out or walking to a kiosk if the terminal is poorly positioned.

---

### **3. Toll Booths**
- **Scenario:** Drivers may need to slow down or stop at manual toll booths to pay.
- **Effort Involved:** Reaching out of the car window or preparing cash/cards ahead of time.

---

### **4. Public Transport Stations**
- **Scenario:** Ticket vending machines or reload stations for transit cards may be located at entry points or away from seating areas.
- **Effort Involved:** Walking to the terminal, often while carrying luggage or commuting items.

---

### **5. Self-Checkout Stations**
- **Scenario:** In retail stores, self-checkout kiosks often require customers to walk to a designated area, even if purchasing only a single item.
- **Effort Involved:** Navigating to the station and sometimes bending to scan items or make payments.

---

### **6. Vending Machines**
- **Scenario:** Consumers must approach the machine to insert cash or card, or to scan their mobile wallet.
- **Effort Involved:** Walking to the machine, potentially in crowded or tight spaces.

---

### **7. Ticket Booths at Events**
- **Scenario:** Event venues often place ticket kiosks or terminals at a central location, requiring attendees to queue and walk to make payments.
- **Effort Involved:** Standing in line and reaching the terminal.

---

### **8. Hotel Check-Ins and Check-Outs**
- **Scenario:** POS systems at the reception desk require guests to physically approach the counter.
- **Effort Involved:** Walking across the lobby or navigating luggage to access the terminal.

---

### **9. Car Wash Stations**
- **Scenario:** Some automated car wash systems require users to pay at an outdoor kiosk before entering the wash bay.
- **Effort Involved:** Exiting the car or leaning out of the window to interact with the terminal.

---

### **10. Delivery or Curbside Pickup**
- **Scenario:** When receiving deliveries, customers might need to approach the delivery person to use their mobile POS terminal.
- **Effort Involved:** Walking outside to meet the delivery person.

---

### **11. Public Charging Stations**
- **Scenario:** At EV charging stations, users often need to interact with a terminal to start charging their vehicle.
- **Effort Involved:** Exiting the car and walking to the station, which can be inconvenient in bad weather.

---

### **12. Amusement Parks**
- **Scenario:** Payment terminals at rides or kiosks often require visitors to navigate crowds and physically reach a terminal.
- **Effort Involved:** Standing in line or walking to a designated location.

---

### **Common Challenges**
1. **Accessibility:** These scenarios can be particularly difficult for individuals with disabilities or limited mobility.
2. **Weather Conditions:** Outdoor terminals may require effort in rain, heat, or snow.
3. **Ergonomics:** Poorly designed terminal placement can increase the physical effort required (e.g., leaning too far or bending down).
4. **Queueing:** Long lines or poorly managed spaces add to the physical and mental effort required.

---

To reduce such efforts, solutions like contactless payments, mobile wallets, app-based payments, and integrated systems (e.g., license plate recognition at tolls) are increasingly being implemented.



Need a networked way of processing payment while consumer can stay in their vehicle.
This method should be more secure than physical POS
This method should offer benefit to merchant as well.
This method should have as many payment method options as POS as well.

We want to decouple from physical constraints.

The reason card not present is less secure because we lose the security factor of "something we have" and there is a window where card details can be stolen or fabricated between the consumer and the merchant.

This leads to the question, why can't the consumer user their card details directly with their phones as a POS device. This acts as a card present transaction which is also more secure than taking a card to a physical POS that is detached from the merchant since it inherits the security features of mobile phones. 

The short answer, POS systems provide specialized hardware for security, and resilience, which phones are not made for.

So the closer the consumer is to the physical POS the better the security, however the closer the POS gets to the consumer, the harder it is physically in available supporting form factors.


There is the PCI SPoC standard for alternative POS devices such as smartphones https://blog.pcisecuritystandards.org/new-pci-software-pin-entry-on-cots-standard

However for PIN entry, separate hardware is required, to keep PIN and card details separata

Could we use phone as the handler of card data, while the car is the PIN reader SCRP?


This idea was greenlit by my father who has 20+ years in the industry and says this is an idea of value.

Next step is to study past implementation attempts and creating a prototype.

## Prototype
We want to enable tap capability within the vehicle. We have two pieces of hardware existing within
the vehicle:
- User smartphone 
- Car infotainment console

Technical requirements
- Card NFC tap reading capability within the vehicle
but a card reader dongle is designed for a merchant to capture other cards
the cardholder already has capability to store card details e.g. in a digital wallet.
so I don't think the answer is nfc because that constrains us to haveing a physical reciever nearby
or in the car. 

The customer already securely has the card data, we need to just transmit it over air to the target terminal.

All card present solutions involve physical proximity
- Work with any external payment terminal or POS

Security requirement

Abstract requirements
- Card presence

- PIN transactions can be reduced to providing any set of details which verify the cardholder, however for our use case of tap amount transactions, we don't need the PIN, or need to replace the PIN.

So we only need to replace Card present, tap methods with something else. However the overlap is such that PIN replacement methods or CVMs are convenient enough to compete with the convenience of tap, while being more secure that it. Still satisfying our lesser needs, but as a side effect also enables reduced risk over tap.

We need a way of identifying the cardholder. This has been explored via consumer devices and is called customer device cardholder verification method (CDCVM). So now it comes down to getting card choice captured. This can be done through a digital wallet? Typically digital wallet transmits to a terminal via NFC rather than online. Can it perform action through ultra wide band or through an online connection? 

