---
title: "UK Import VAT Explained: When, How Much & How to Reclaim"
description: "Complete guide to UK import VAT covering calculation, Postponed VAT Accounting, C79 certificates, reclaiming VAT, and common mistakes importers make."
pubDate: 2026-04-04
author: "LogisticsEdge"
category: "customs"
tags: ["import-vat", "vat", "postponed-vat-accounting", "pva", "customs", "uk-imports", "hmrc"]
image: "/images/articles/uk-import-vat-explained.jpg"
draft: false
---

## Key Takeaways

- Import VAT is charged at 20% (standard rate) on most goods entering the UK, calculated on the customs value plus any duty and delivery costs to the UK border
- Postponed VAT Accounting (PVA) lets VAT-registered businesses account for import VAT on their VAT return instead of paying it at the border, eliminating the cash flow hit entirely
- You reclaim import VAT either through a C79 certificate (if you paid at the border) or your monthly postponed import VAT statement (if using PVA) — both must be retained as evidence
- Getting the customs value wrong is the single most common cause of incorrect import VAT charges, and HMRC can assess underpayments going back four years
- Some goods attract reduced (5%) or zero-rate (0%) VAT, so checking the correct VAT rate for your commodity code before importing is essential

---

## What is import VAT?

Import VAT is a tax charged by HMRC on goods imported into the UK from outside the country. It works in the same way as domestic VAT — it is a consumption tax ultimately borne by the end consumer — but it is collected at the point of importation rather than at the point of sale.

Since 1 January 2021, import VAT applies to all goods entering the UK, including those from the EU. Before Brexit, goods moving between EU member states were not subject to import VAT. That changed when the UK left the EU's VAT area, and businesses that previously moved goods freely from EU suppliers now face an import VAT liability on every consignment.

Import VAT is separate from [customs duty](/articles/import-duty-uk-complete-guide/). Duty is a tariff based on the type of goods and their country of origin. Import VAT is a broader tax applied on top of the goods' value and any duty charged. A single shipment will typically incur both, and they are calculated and declared as part of the [customs clearance process](/articles/customs-clearance-uk-step-by-step-guide/).

The standard rate of import VAT is **20%**. Some goods attract the reduced rate of **5%** (such as children's car seats and certain energy-saving materials), and others are zero-rated at **0%** (including most food, children's clothing, and printed books). A small number of goods are VAT-exempt entirely. The rate depends on the commodity code assigned to the goods — if you are unsure how classification works, see our [commodity codes guide](/articles/uk-commodity-codes-tariff-classification-guide/).

## How import VAT is calculated

The formula for import VAT is straightforward, but getting the inputs right is where most mistakes happen.

**Import VAT = VAT rate x (customs value + duty + delivery costs to the UK)**

The components break down as follows:

**Customs value.** This is the transaction value of the goods — typically the price paid or payable by the buyer, adjusted for certain additions and deductions under the UK's valuation rules. If you buy goods on an EXW or FCA basis, the customs value is the price of the goods themselves. If you buy on CIF or DDP terms, adjustments may be needed. The Incoterms used in your purchase contract directly affect how customs value is determined.

**Duty.** Any customs duty payable on the goods is added to the customs value before VAT is calculated. This means you pay VAT on the duty — a tax on a tax, effectively.

**Delivery costs.** Transport, insurance, and any other charges incurred in bringing the goods to the UK border are included in the VAT calculation. Costs incurred after the goods arrive in the UK (inland freight, for example) are excluded from the import VAT calculation, though they may attract domestic VAT separately.

### Worked example 1: Standard import

A UK business imports industrial valves from South Korea.

| Component | Amount |
|---|---|
| Invoice value of goods (FOB) | £25,000 |
| Freight to UK port | £1,800 |
| Insurance | £200 |
| **Customs value (CIF)** | **£27,000** |
| Duty rate (commodity code 8481.80) | 2.0% |
| Duty payable | £540 |
| **VAT base (customs value + duty)** | **£27,540** |
| Import VAT at 20% | £5,508 |
| **Total border charges** | **£6,048** |

The business pays £6,048 at importation (or accounts for it via PVA — more on that below). If VAT-registered, the £5,508 import VAT is reclaimable, making the real cost of importing these goods £540 in duty.

### Worked example 2: EU import with zero duty under the TCA

A UK retailer imports furniture from Germany under the EU-UK Trade and Cooperation Agreement.

| Component | Amount |
|---|---|
| Invoice value of goods (DAP) | £42,000 |
| Adjustment: deduct UK inland delivery included in DAP price | -£1,200 |
| Freight to UK border (included in price, allocated) | £2,800 |
| Insurance | £400 |
| **Customs value** | **£44,000** |
| Duty rate (with TCA preference claimed) | 0% |
| Duty payable | £0 |
| **VAT base** | **£44,000** |
| Import VAT at 20% | £8,800 |
| **Total border charges** | **£8,800** |

Even with zero duty under the TCA, import VAT still applies. Many businesses importing from the EU were caught off guard by this after Brexit. The £8,800 is reclaimable if the business is VAT-registered, but it still represents a significant cash flow impact if paid upfront at the border.

### Worked example 3: Reduced-rate goods

A UK business imports children's car seats from China.

| Component | Amount |
|---|---|
| Customs value (CIF) | £18,000 |
| Duty rate | 3.5% |
| Duty payable | £630 |
| **VAT base** | **£18,630** |
| Import VAT at 5% (reduced rate) | £931.50 |
| **Total border charges** | **£1,561.50** |

The reduced VAT rate applies because children's car seats fall under the 5% category. Checking the applicable VAT rate against the commodity code before importing avoids overpayment.

## Postponed VAT Accounting explained

Postponed VAT Accounting (PVA) is the single most important mechanism available to UK importers for managing import VAT cash flow. It was introduced on 1 January 2021 and is available to all VAT-registered businesses importing goods into the UK.

### How PVA works

Instead of paying import VAT at the border (either directly or through a customs agent's deferment account), you account for it on your VAT return. The import VAT is declared in both **Box 1** (output tax) and **Box 4** (input tax) of your VAT return, meaning the two entries cancel each other out. There is no net payment to HMRC for the import VAT — it is a paper exercise.

The practical effect is significant. Without PVA, a business importing £1 million of goods per month at 20% VAT would need to pay £200,000 at the border and then wait to reclaim it on their next VAT return — potentially tying up cash for weeks or months. With PVA, that £200,000 never leaves the business's bank account.

### How to use PVA

To use PVA, you instruct your customs broker or freight forwarder to select the PVA method of payment when submitting your import declaration. On the customs declaration (C88/SAD or CDS declaration), the method of payment code for PVA is **"G"** in the Additional Information field. You need:

- A valid UK [EORI number](/articles/eori-number-uk-complete-guide/)
- To be registered for UK VAT
- Your customs broker to enter the correct method of payment on the declaration

There is no separate application or approval process. If you are VAT-registered and have an EORI number, you can use PVA immediately.

### Monthly postponed import VAT statements

When you use PVA, HMRC generates a monthly **postponed import VAT statement** (PIVS). This is available to download from your Government Gateway account, usually by the sixth working day of the month following the import. You need these statements to complete your VAT return accurately and to support any HMRC enquiry.

You must download and retain these statements. HMRC makes them available for six months only. After that, they are deleted and cannot be recovered. If you lose them and face a VAT inspection, you will have no evidence to support your input tax claim.

### PVA and partial exemption

If your business is partly exempt (you make both taxable and exempt supplies), PVA still applies, but you can only recover the portion of import VAT that relates to your taxable supplies. The Box 1/Box 4 entries must be adjusted according to your partial exemption method.

## How to reclaim import VAT

VAT-registered businesses can reclaim import VAT as input tax on their VAT return, provided the imported goods are used for making taxable supplies. The mechanism for reclaiming depends on whether you paid at the border or used PVA.

### If you paid at the border

When import VAT is paid at the border — either directly or through a customs agent's deferment account — HMRC issues a **C79 certificate**. This is your evidence of import VAT paid and is required to support your input tax claim.

You reclaim the VAT by entering the amount in **Box 4** of your VAT return for the period in which you receive the C79 certificate. The key point: you claim based on when you receive the C79, not when the goods were imported. This can create timing delays, particularly if your broker uses their own deferment account and the C79 is issued in their name rather than yours.

### If you used PVA

As covered above, PVA entries go into both Box 1 and Box 4 of your VAT return. The net effect is zero, so there is nothing to "reclaim" in the traditional sense — the VAT is accounted for but never actually paid. Your postponed import VAT statement is the supporting document.

### Conditions for reclaiming

Regardless of the method, you must meet these conditions to reclaim import VAT:

- You must be registered for UK VAT
- The goods must be used for making taxable supplies (or intended to be at the time of import)
- You must hold valid evidence: a C79 certificate (for border payments) or a postponed import VAT statement (for PVA)
- You must not be blocked by the partial exemption or capital goods scheme rules from recovering the full amount

Non-VAT-registered businesses cannot reclaim import VAT. The VAT becomes an absolute cost. If you are importing goods regularly and are not VAT-registered, the registration threshold (currently £90,000 in taxable turnover) is worth reviewing carefully.

## C79 certificates and monthly statements

### C79 certificates

A C79 certificate is a monthly statement issued by HMRC showing the import VAT paid on your behalf through customs declarations. It is posted to the address associated with your EORI number and is the only document HMRC accepts as evidence of import VAT paid at the border. Commercial invoices, freight forwarder invoices, and customs entry paperwork are **not** valid substitutes.

C79 certificates are issued monthly, typically arriving two to three months after the import date. They are grouped by the calendar month of import, not by individual shipment. Each certificate lists the entry reference numbers, dates, and VAT amounts.

If your customs broker uses their own deferment account (rather than yours), the C79 may be issued in their name. In that case, you need to arrange for them to provide you with either the original C79 or a copy endorsed to your business. Without it, your VAT reclaim has no supporting evidence.

### Postponed import VAT statements (PIVS)

If you use PVA, your evidence is the monthly postponed import VAT statement, downloadable from your Government Gateway account. These statements show the total import VAT accounted for under PVA during each calendar month, broken down by declaration.

Critical reminders about PIVS:

- Available from the sixth working day of the following month
- Only available for **six months** — download them promptly
- You must retain them for **six years** (standard VAT record-keeping requirement)
- If figures on the statement do not match your records, investigate immediately — declaration errors by your broker may need correcting

## Common mistakes

Import VAT errors are common, and HMRC has the power to assess underpayments going back four years (or twenty years in cases of deliberate understatement). These are the mistakes we see most frequently.

### 1. Wrong customs value

The customs value is the foundation of both duty and VAT calculations. Common errors include failing to add freight and insurance costs, using the wrong exchange rate, excluding royalties or licence fees that should be added, or double-counting costs already included in the invoice price. Even a 5% error on a £500,000 shipment means £5,000 in incorrect VAT.

### 2. Not using PVA

Some businesses are still paying import VAT at the border, either because they do not know PVA exists or because their customs broker defaults to deferment account payment. There is no financial benefit to paying at the border if you are VAT-registered. Switch to PVA and free up the cash.

### 3. Missing or lost C79 certificates

If you pay VAT at the border and lose your C79, you cannot reclaim the VAT. HMRC does not issue duplicates. Businesses that rely on customs brokers to forward C79s are particularly vulnerable — if the certificate goes astray, the VAT is gone. This alone is a strong argument for using PVA instead.

### 4. Claiming the wrong VAT rate

Not all goods are taxed at 20%. Importing zero-rated food at the standard rate overstates your VAT liability (though it also overstates your reclaim, creating a net nil effect but inaccurate records). Importing standard-rated goods at the zero rate understates your liability and will trigger a HMRC assessment. Always verify the VAT rate against the [commodity code](/articles/uk-commodity-codes-tariff-classification-guide/) before making a declaration.

### 5. Failing to download postponed import VAT statements

HMRC deletes these after six months. If you have not downloaded them, you have no evidence for your VAT return. Set a calendar reminder for the seventh working day of every month to download the previous month's statement.

### 6. Incorrect VAT return entries for PVA

PVA requires entries in both Box 1 and Box 4. Some businesses only enter Box 4 (treating it as a normal input tax claim), which understates output tax and will be flagged by HMRC. Others enter the wrong figure. Reconcile your PIVS against your VAT return entries every quarter.

### 7. Forgetting VAT on duty

Import VAT is charged on the customs value **plus** duty. Businesses that calculate VAT on the goods value alone (excluding duty) will underpay. On high-duty goods, this can be a material amount.

## Frequently asked questions

### Do I pay import VAT on goods from the EU?

Yes. Since 1 January 2021, goods imported from the EU are subject to import VAT in exactly the same way as goods from the rest of the world. The EU-UK Trade and Cooperation Agreement can reduce customs duty to zero, but it does not affect import VAT. If you are VAT-registered, you can use PVA or reclaim via a C79 certificate.

### Is there a minimum value below which import VAT does not apply?

For business-to-business (B2B) imports, there is no de minimis threshold — import VAT applies from the first pound. For business-to-consumer (B2C) consignments valued at £135 or less, the overseas seller is required to charge and account for UK VAT at the point of sale (the so-called "low-value consignment" rules), so the VAT is collected before the goods arrive. Above £135, import VAT is charged at the border as normal.

### Can I use PVA if I am not VAT-registered?

No. Postponed VAT Accounting is only available to businesses that are registered for UK VAT and hold a valid [EORI number](/articles/eori-number-uk-complete-guide/). If you are not VAT-registered, you must pay import VAT at the border and cannot reclaim it.

### What happens if I overpay import VAT?

If you paid too much import VAT (for example, because the customs value was overstated or the wrong VAT rate was applied), you can request an amendment to the customs declaration. This is done through your customs broker and must be submitted within three years of the original declaration date. Once the amendment is processed, the overpaid VAT is either refunded or offset against future liabilities. If you used PVA, the correction is made on a subsequent VAT return.

### How long does it take to reclaim import VAT?

If you use PVA, the reclaim happens on the same VAT return as the liability — there is no delay. If you paid at the border, you need to wait for the C79 certificate, which typically arrives two to three months after the goods were imported. You then reclaim on the VAT return for the period in which you receive the C79. In practice, this means cash can be tied up for one to four months depending on your VAT return cycle.
