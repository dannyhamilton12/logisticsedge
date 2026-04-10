---
title: "Customs Declaration Service (CDS): Complete UK Guide"
description: "Complete guide to HMRC's Customs Declaration Service (CDS). Learn how to register, file declarations, understand data elements, and avoid common mistakes when importing to the UK."
pubDate: 2026-04-09
author: "LogisticsEdge"
category: "customs"
tags: ["CDS", "customs declarations", "HMRC", "UK imports", "CHIEF"]
draft: false
---

## Key Takeaways

- CDS replaced CHIEF as HMRC's primary customs declaration platform for imports, requiring up to 78 data elements depending on your goods
- You need a Government Gateway account, EORI number, and duty deferment account (optional) to access CDS fully
- CDS uses a different procedure code structure than CHIEF: a 4-digit code plus up to 99 three-digit additional codes per item
- Monthly Customs Declaration Statements replace the old monthly Postponed VAT Accounting statements, with payment due by the 15th working day
- Northern Ireland movements have special CDS requirements from April 2026 under the Windsor Framework
- Common mistakes include incorrect commodity codes, missing procedure codes, and wrong valuation methods — all can trigger delays or penalties

---

## What Is CDS and Why It Matters

The Customs Declaration Service (CDS) is HMRC's digital platform for submitting import and export declarations in the UK. It replaced the legacy CHIEF (Customs Handling of Import and Export Freight) system, which had been in use since 1992. CDS was developed to meet the requirements of the EU's Union Customs Code (UCC), which mandates more detailed data collection and electronic processing of customs information.

CDS handles significantly more data than CHIEF. Import declarations require up to 78 data elements, while export declarations need up to 65 elements, depending on the nature of your goods and their origin. This increased data requirement gives HMRC better visibility over goods moving through UK borders but places greater responsibility on traders to ensure accuracy.

The transition from CHIEF to CDS was completed for imports by the end of 2025. Some export declarations still use CHIEF in 2026, but HMRC has announced full migration timelines. If you're importing goods into Great Britain from outside the UK, you must use CDS. The platform integrates with other HMRC systems including the Trade Tariff tool and the duty deferment scheme.

Using CDS correctly matters because errors or omissions can lead to customs delays, storage charges at ports, and potential penalties. According to HMRC guidance, inaccurate declarations may result in compliance assessments or civil penalties under the Finance Act 2003. Getting your CDS declarations right from the start protects your supply chain and avoids unnecessary costs.

## Getting Access to CDS

Accessing CDS requires several steps. Complete them before your first shipment arrives.

First, you need a Government Gateway account. This is HMRC's primary authentication system for online services. You can create one at gov.uk using your email address and a password. Government Gateway credentials give you access to multiple HMRC services including CDS, VAT returns, and duty deferment accounts.

Second, you need an EORI (Economic Operators Registration and Identification) number. Your EORI number identifies you to customs authorities across the UK and EU. For UK traders, it takes the format GB followed by 12 digits and a three-digit suffix (for example, GB123456789000). You apply for an EORI number through gov.uk/eori, and HMRC typically issues it within 3-5 working days. Without an EORI number, you cannot submit customs declarations through CDS. See our complete guide to [EORI numbers](/articles/eori-number-uk-complete-guide/) for detailed registration steps.

Third, you must enrol for CDS specifically. Having a Government Gateway account and EORI number does not automatically give you CDS access. You enrol through the HMRC online services portal, selecting "Customs Declaration Service" from the list of available services.

Fourth, consider setting up a duty deferment account. This is optional but recommended for regular importers. A duty deferment account lets you pay customs duty and import VAT monthly rather than per declaration. You apply through HMRC using form CDS120. Approved accounts have a monthly limit based on your typical duty and VAT liability. With a deferment account, you receive a Customs Declaration Statement each month showing all charges due, payable by the 15th working day.

Finally, you need CDS-compatible software or a customs broker. HMRC does not provide a free web interface for filing declarations. You must use commercial customs software that connects to CDS via API, or appoint a customs broker who files on your behalf. Major software providers include Clearit, CustomsLink, and Descartes. Not sure whether to use a broker or forwarder? Read our comparison of [customs brokers vs freight forwarders](/articles/customs-broker-vs-freight-forwarder/).

## Understanding CDS Data Elements

CDS requires significantly more data than the old CHIEF system. Import declarations can require up to 78 data elements, though not all apply to every shipment.

The 78 data elements are organised into eight groups:

**Group 1: Message Identification** includes the declaration type (import or export), the declaration category (standard, simplified, or supplementary), and the unique consignment reference.

**Group 2: Parties and Addresses** covers everyone involved in the transaction. You must provide the declarant's EORI number, the importer's details, the exporter's details, and any representatives acting on your behalf.

**Group 3: Totals and Invoicing** includes the total number of items, the total invoice value, the currency code, and any discounts or additions to the invoice price.

**Group 4: Transport and Borders** covers how the goods are moving and where they enter or leave the UK. You need the mode of transport, the vessel or flight number, the port or airport code, and the expected arrival date.

**Group 5: Goods Location** specifies where the goods are physically located at the time of declaration. For imports, this is usually the port of entry.

**Group 6: Goods Identification** is the most detailed group. It includes the commodity code (up to 10 digits), the goods description, the net mass in kilograms, the quantity in supplementary units, the country of origin, and any certificates or licences required.

**Group 7: Procedure and Relief** covers the customs procedure you're using, including the procedure code, any special procedures like inward processing or customs warehousing, and any duty reliefs or exemptions.

**Group 8: Additional Information** captures document references (such as bill of lading numbers), any previous customs declarations related to the goods, and free-text notes.

Not every declaration needs all 78 elements. A straightforward import of standard goods might use 40-50 elements. Complex shipments involving special procedures, preferential duty rates, or controlled goods will need more.

According to HMRC's CDS technical specifications, missing or incorrect data elements are the most common cause of declaration rejections. Software providers typically validate your data before submission, but you're responsible for accuracy.

## Filing Your First Declaration

Filing a CDS declaration involves a structured process. Whether you use software directly or work through a broker, understanding the steps helps you verify that declarations are correct.

Start by gathering your commercial documents. You need a commercial invoice showing the seller, buyer, goods description, unit prices, total value, currency, and Incoterms. You need a packing list showing the number of packages, their weights, and dimensions. For certain goods, you need certificates of origin, health certificates, or import licences. Understanding your Incoterms is critical — see our [Incoterms visual guide](/articles/incoterms-explained-visual-uk-guide/) for clarity on who handles customs formalities under each term.

Next, determine the correct commodity code for your goods. The commodity code is a 10-digit number that classifies your goods for customs purposes. The first six digits are the Harmonized System (HS) code used worldwide. Digits seven and eight are the Combined Nomenclature (CN) code. Digits nine and ten are the UK-specific Taric codes. You can look up commodity codes using HMRC's Trade Tariff tool at trade-tariff.service.gov.uk. Getting the commodity code right is critical — it determines your duty rate, any import restrictions, and whether you need licences.

Calculate the customs value of your goods. For most imports, this is the transaction value — what you actually paid or will pay. Add any costs not included in the invoice price: freight to the UK border, insurance, loading and handling charges, and any royalties or licence fees related to the goods. Do not include UK delivery costs after import or import VAT itself.

Determine the correct procedure code. For standard imports into free circulation, you'll typically use code 40 000. If you're importing goods for inward processing (to be processed and re-exported), you'll use a different code.

Enter all data elements into your CDS software. The software will guide you through each group of data elements. Double-check the commodity code, customs value, and procedure code — these are the most common sources of errors.

Submit the declaration. Your software sends the declaration to CDS via API. CDS validates the data and returns a response. If accepted, you receive a Unique Consignment Reference (UCR). If rejected, CDS returns an error code explaining what went wrong.

Pay any duty and VAT due. If you have a duty deferment account, the charges are added to your monthly statement. If not, you must pay immediately. Postponed VAT Accounting is available for most imports, letting you account for import VAT on your VAT return rather than paying at the border.

Keep records. HMRC requires you to keep customs declaration records for at least four years. This includes the declaration itself, commercial invoices, transport documents, and any certificates or licences.

## CDS Procedure Codes Explained

CDS uses a different procedure code structure than the legacy CHIEF system.

Under CHIEF, procedure codes were seven digits: a two-digit "request" code followed by a five-digit "previous procedure" code. For example, code 40 00000 meant "release for free circulation" with no previous procedure.

Under CDS, procedure codes have two parts. The first part is a four-digit code representing the requested procedure. The second part consists of up to 99 three-digit codes representing additional procedures or previous procedures.

For standard imports into free circulation with no special procedures:
- First part: 40 00 (release for free circulation)
- Second part: 000 (no additional procedure)

So the full code appears as 40 00 000 in CDS, compared to 40 00000 in CHIEF.

If you're importing goods under inward processing:
- First part: 51 00 (inward processing)
- Second part: varies depending on the specific relief

For temporary admission:
- First part: 53 00 (temporary admission)
- Second part: varies

The three-digit additional codes can indicate:
- 100: Standard import without special conditions
- 200: Goods subject to anti-dumping duties
- 300: Goods under customs warehousing

You can use up to 99 additional codes per item line. This lets you capture complex scenarios where goods are subject to multiple procedures or reliefs simultaneously.

HMRC publishes a full list of CDS procedure codes in the CDS Import and Export Notice on gov.uk. The notice is updated regularly. Software providers typically maintain updated code lists, but verify that your software is current.

Getting the procedure code wrong can have serious consequences. If you use a procedure code for inward processing but don't actually process and re-export the goods, you may owe back duty plus interest. Always verify the correct procedure code for your situation.

## Duty Deferment and Payment

CDS integrates with HMRC's duty deferment scheme, which lets approved traders pay customs duty and import VAT monthly rather than per declaration.

To use duty deferment, you must apply for a deferment account using form CDS120. HMRC assesses your creditworthiness and sets a monthly limit based on your typical duty and VAT liability. The limit covers both customs duty and import VAT.

Once approved, you receive a deferment account number. You reference this number in your CDS declarations. When you file a declaration, the duty and VAT are allocated to your deferment account rather than requiring immediate payment.

Each month, HMRC issues a Customs Declaration Statement showing all charges allocated to your account during the previous month. The statement lists each declaration, the duty amount, the VAT amount, and any other charges. You receive the statement around the 6th working day of the month.

Payment is due by the 15th working day of the month. For example, charges accrued in March appear on the statement issued in early April, and payment is due by the 15th working day of April. HMRC collects payment via Direct Debit from your nominated bank account.

If you don't have a deferment account, you must pay duty and VAT for each declaration at the time of filing. Most CDS software integrates with payment systems to facilitate this. Postponed VAT Accounting is available regardless of whether you have a deferment account.

Postponed VAT Accounting works by recording the import VAT on your CDS declaration. You then include both the import VAT (as input tax) and the corresponding output tax on your VAT return. HMRC provides monthly statements showing all imports where you used Postponed VAT Accounting — you need these for your VAT records.

According to HMRC's guidance, failure to pay deferment charges on time can result in the suspension or revocation of your deferment account. Late payment penalties may also apply.

## Common Mistakes and How to Avoid Them

CDS declarations are complex, and errors are common — especially for traders new to the system.

**Incorrect commodity codes** are the most common error. The commodity code determines your duty rate, so getting it wrong can mean overpaying or underpaying duty. Always verify the commodity code using HMRC's Trade Tariff tool. If your goods are complex, consider getting a Binding Tariff Information (BTI) ruling from HMRC.

**Wrong customs valuation** is another frequent problem. The customs value must include all costs up to the UK border: the goods price, freight to the UK, insurance, and certain other charges. Traders sometimes exclude freight costs or include UK delivery costs (which should be excluded). Review HMRC's valuation guidance and ensure your commercial invoices clearly separate UK delivery costs from international freight.

**Missing or incorrect procedure codes** can trigger compliance reviews. Using the wrong procedure code may mean you're not claiming reliefs you're entitled to, or you're claiming reliefs you haven't actually earned. Always verify the correct procedure code for your situation.

**Incomplete data elements** cause declaration rejections. CDS validates all required data elements before accepting a declaration. Missing information — such as an absent EORI number, missing country of origin, or incomplete address details — results in immediate rejection.

**Incorrect origin declarations** affect preferential duty rates. If you claim preferential duty under a UK trade agreement, you must have proof of origin. This can lead to duty demands for the difference between the preferential rate and the standard rate, plus interest. Only claim preference if you hold valid proof of origin.

**Late or missing supplementary declarations** occur when traders use simplified procedures but forget to file the supplementary declaration within the required timeframe. Simplified declarations let you import goods with minimal data, but you must file a full supplementary declaration within 14 days.

To avoid these mistakes, invest time in training. HMRC offers free webinars and guidance on CDS. Work with experienced customs brokers or software providers who can validate your declarations. Keep detailed records of every shipment.

## CDS for Northern Ireland

Northern Ireland has special CDS requirements under the Windsor Framework. From 13 April 2026, updated CDS procedures apply to movements between Great Britain and Northern Ireland.

Goods moving from Great Britain to Northern Ireland that are "not at risk" of entering the EU do not require full customs declarations. Instead, traders use the UK Internal Market Scheme (UKIMS) to declare goods as not at risk. You apply for UKIMS authorisation through HMRC.

Goods moving from Northern Ireland to Great Britain generally do not require import declarations, as Northern Ireland remains part of the UK customs territory for this direction of trade.

For goods moving from outside the UK into Northern Ireland, full CDS declarations are required, just as for imports into Great Britain. However, EU customs duties may apply if goods are "at risk" of entering the EU (via the Republic of Ireland).

CDS handles Northern Ireland movements using specific destination codes and procedure codes. When filing declarations for NI movements, you must indicate whether goods are at risk or not at risk, and whether you're using the UK Internal Market Scheme.

HMRC publishes detailed guidance on CDS requirements for Northern Ireland movements. The guidance is complex and subject to updates. If you regularly move goods between Great Britain and Northern Ireland, consider specialist advice.

## Getting Help with CDS

CDS is complex, and you don't have to navigate it alone.

**HMRC guidance** is the primary reference. The gov.uk website hosts comprehensive CDS documentation including the CDS Import and Export Notice, data element specifications, procedure code lists, and valuation guidance. For complex classification or valuation issues, you can apply for Binding Tariff Information (BTI) or Binding Origin Information (BOI) rulings.

**Customs software providers** offer technical support for their systems. Major providers including Clearit, CustomsLink, and Descartes have help desks and knowledge bases.

**Customs brokers and freight forwarders** can file declarations on your behalf. Brokers handle the entire declaration process and take responsibility for accuracy. Check that your broker is authorised by HMRC and uses CDS-compatible systems.

**Trade associations** offer sector-specific guidance. Organisations such as the British International Freight Association (BIFA), the UK Warehousing Association (UKWA), and the Institute of Export and International Trade provide training and guidance notes for members.

**HMRC's Customs and International Trade helpline** handles general enquiries. Contact details are on gov.uk.

Remember that you're responsible for the accuracy of your declarations even if you use a broker. HMRC holds the importer liable for duty and VAT, and penalties can apply for incorrect declarations regardless of who filed them.

## Frequently Asked Questions

**Do I need to use CDS for every import?**
Yes, if you're importing goods into Great Britain from outside the UK, you must submit a customs declaration through CDS. The only exceptions are goods moving from Northern Ireland to Great Britain and certain low-value goods under £135 where VAT is collected at point of sale.

**What happens if my CDS declaration is rejected?**
CDS validates declarations on submission and returns error codes for rejected declarations. Common errors include invalid commodity codes, missing EORI numbers, or mismatched data elements. Your software will show the error code and description. Fix the error and resubmit.

**Can I use CDS without a duty deferment account?**
Yes, a duty deferment account is optional. Without one, you must pay duty and VAT for each declaration at the time of filing. Most CDS software integrates with payment systems to facilitate this.

**How long do I need to keep CDS records?**
HMRC requires you to keep customs declaration records for at least four years from the date of import. This includes the declaration itself, commercial invoices, transport documents, certificates of origin, and any licences or permits.

**What's the difference between CDS and the Trade Tariff tool?**
CDS is the declaration platform where you submit import and export declarations. The Trade Tariff tool (trade-tariff.service.gov.uk) is a separate HMRC system used to look up commodity codes, duty rates, and import requirements for specific goods.

**Can I file CDS declarations myself or do I need a broker?**
You can file CDS declarations yourself if you have CDS-compatible software and understand the requirements. HMRC does not provide free filing software, so you must subscribe to a commercial system. Alternatively, you can appoint a customs broker or freight forwarder to file on your behalf.
