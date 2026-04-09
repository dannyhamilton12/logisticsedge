---
title: "How to Export from the UK: Step-by-Step Guide"
description: "Complete guide to UK exports: EORI numbers, CDS declarations, export licences, controlled goods, C1602 forms, and HMRC compliance requirements."
pubDate: 2026-04-09
author: "LogisticsEdge"
category: "trade"
tags: ["UK exports", "export declaration", "CDS", "EORI", "export licence", "HMRC"]
draft: false
---

## Key Takeaways

- Every consignment leaving the UK for destinations outside the common travel area requires an export declaration via CDS
- A valid GB-prefixed EORI number linked to your Government Gateway account is mandatory before declaring
- CHIEF has been replaced by CDS for all UK export declarations as of 2026
- Export supplementary declarations must be submitted within 14 days of goods departure when using simplified procedures
- Controlled goods require export licences declared to HMRC with matching EORI on licence and declaration
- C1602 forms prove export when departure messages are not automatically sent by carriers
- HMRC expects exporters to retain commercial invoices, bills of lading, transport docs, and classification records for 4 years

---

## Exporting from the UK Post-Brexit

The UK's exit from the EU single market transformed export procedures. Where once goods moved freely to EU destinations with minimal paperwork, UK exporters now face customs declarations, licence requirements for controlled goods, and digital compliance systems regardless of destination.

The Customs Declaration Service (CDS) replaced the legacy CHIEF system for all UK imports and exports by 2026. Understanding how CDS works, what documentation HMRC requires, and when export licences apply is essential for any UK business shipping goods abroad — whether to EU customers or global markets.

This guide walks through the export process step by step, from EORI registration through to proof of export and record retention.

## Step 1: Obtain Your EORI Number

Before submitting any export declaration, you need a valid EORI (Economic Operators Registration and Identification) number. HMRC uses this identifier to track all customs activity linked to your business.

### EORI Format and Application

UK EORI numbers follow the format **GB + 12 digits + 3-character suffix** (e.g., GB123456789000ABC). The suffix often matches your VAT registration or is assigned sequentially.

According to HMRC's developer guidance, you must:
1. Hold a Government Gateway account linked to your business UTR (Unique Taxpayer Reference)
2. Apply through the GOV.UK EORI registration service
3. Receive your EORI within 3-5 working days (sometimes faster for VAT-registered businesses)

If you already imported goods into the UK, you likely have an EORI. The same number works for both imports and exports.

### EORI and Declarant Identification

When submitting declarations through CDS, the EORI serves as the primary declarant identifier. HMRC's developer documentation states: "If both EORI and Badge ID are supplied then the EORI will be used as the declarant identifier."

Even if you use a customs broker or freight forwarder under indirect representation, your EORI appears on the declaration as the exporter. You remain legally responsible for declaration accuracy regardless of who submits it on your behalf, according to FreightCode's 2026 CDS guide.

### Common EORI Pitfalls

**Using an EU EORI:** Post-Brexit, EU-issued EORIs (e.g., DE-, FR-, IE-prefixed) do not work for UK export declarations. You need a GB-prefixed EORI.

**Expired or dormant EORIs:** HMRC may deactivate EORIs after prolonged inactivity. Test your EORI with a small declaration before committing to large shipments.

**Mismatched legal entity:** The EORI must match the legal entity exporting the goods. If your company changed names or structure, update your EORI record via HMRC.

For detailed EORI guidance, see our [EORI Number UK Complete Guide](/articles/eori-number-uk-complete-guide/).

## Step 2: Determine If You Need an Export Licence

Not all goods can be exported freely. The UK controls exports of military items, dual-use technologies, certain chemicals, and goods subject to trade sanctions.

### Controlled Goods Categories

The Department for Business and Trade (DBT) maintains lists of controlled goods requiring export licences:

**Military goods:** Firearms, ammunition, military vehicles, weapons systems, and related technology.

**Dual-use items:** Civilian goods with potential military applications — encryption software, high-performance computers, certain sensors, aerospace components.

**Chemical weapons precursors:** Specific chemicals listed under UK chemical weapons regulations.

**Cultural goods:** Artefacts over 50 years old exceeding value thresholds may require export licences from Arts Council England.

**Sanctioned destinations:** Goods destined for countries under UK trade sanctions (e.g., Russia, Belarus, certain Syrian entities) require specific licences regardless of product type.

### Open General Licences (OGL)

Some controlled goods qualify for Open General Licences — pre-published licences allowing exports without individual applications, provided conditions are met. OGLs cover:
- Certain dual-use items to specific destinations
- Temporary exports for exhibitions or repairs
- Low-risk military components to allied nations

Check the DBT OGL database before assuming individual licences are required. Using an OGL still requires declaring the licence on your CDS export declaration.

### Licence Application Process

For goods not covered by OGLs, apply through the SPIRE (System for Product-related Import and Export) portal:
1. Create SPIRE account linked to your EORI
2. Submit licence application with product specifications, end-user details, and destination
3. Await assessment (typically 20 working days for standard licences)
4. Receive licence with unique reference number

### Declaring Licences on CDS

Strong & Herd's June 2024 guidance highlights a critical compliance point: **the EORI on your export declaration must match the EORI on your licence application.** Mismatches trigger CDS errors requiring HMRC intervention.

When completing CDS declarations:
- Enter the licence reference number in the appropriate document code field
- Ensure the exporter EORI matches the licence holder EORI
- Use direct representation if you hold the licence; indirect representation requires the broker to reference your licence correctly

For broader import licensing requirements (which share similar controlled goods frameworks), see our [Import Licensing UK guide](/articles/import-licensing-uk-controls/).

## Step 3: Prepare Commercial Documentation

Export declarations require supporting commercial documents. HMRC expects exporters to retain these records for 4 years, and the "Get customs data for import and export declarations" service — updated 11 March 2026 — provides access to historical declaration data for EORI holders.

### Commercial Invoice

Every export shipment needs a commercial invoice showing:
- Exporter name and address (matching EORI registration)
- Consignee name and address (customer or delivery party)
- Invoice date and number
- Full description of goods including HS/commodity codes
- Quantity, unit price, and total value in sterling or currency of sale
- Incoterms (e.g., FOB Felixstowe, DDP Berlin)
- Country of origin (where goods were manufactured)
- Exporter's EORI number (recommended though not always mandatory on invoice itself)

HMRC accepts commercial invoices as proof of export for VAT zero-rating purposes, provided they match the CDS declaration.

### Packing List

While not legally required, packing lists are standard practice for international shipments. Include:
- Container or package numbers
- Contents of each package (item-level breakdown)
- Gross and net weights per package
- Dimensions per package
- Total gross weight and volume

Packing lists help customs examiners verify cargo without full unpacking, potentially reducing examination time and costs.

### Transport Documents

Depending on transport mode:
- **Sea freight:** Bill of lading (original or telex release) or sea waybill
- **Air freight:** Air waybill (AWB)
- **Road freight:** CMR consignment note for European destinations
- **Rail freight:** CIM consignment note

These documents prove the contract of carriage and often serve as title documents (particularly bills of lading).

### Additional Certificates

Certain goods or destinations require:
- **Certificates of origin:** For preferential duty treatment under UK trade agreements
- **Phytosanitary certificates:** For plant products, seeds, wood packaging
- **Health certificates:** For animal products, food, pharmaceuticals
- **Dangerous goods declarations:** For hazardous materials (ADR for road, IMDG for sea, IATA for air)

## Step 4: Submit Export Declaration via CDS

The Customs Declaration Service (CDS) is now the sole platform for UK export declarations. CHIEF completed its phased shutdown in 2025-2026, with all exports migrating to CDS.

### Declaration Types

**Full export declaration:** Standard declaration submitted before goods depart. Required for most controlled goods, high-value shipments, and destinations outside the common travel area.

**Simplified declaration:** Pre-shipment advice followed by supplementary declaration within 14 days of departure. Available to traders with appropriate authorisations.

**Pre-shipment advice:** Notifies HMRC of intended export before goods arrive at the port. Used when goods move under duty suspension or special procedures.

### Who Can Submit Declarations

**Self-representation:** Exporters submit their own declarations directly to CDS. Requires:
- CDS enrolled account linked to EORI
- Knowledge of CDS data requirements and commodity code classification
- Software capable of generating CDS-compatible XML (or use GOV.UK manual entry for low-volume traders)

**Direct representation:** Customs broker or freight forwarder submits declarations on your behalf, but you (the exporter) remain legally responsible for accuracy. Most common for SMEs.

**Indirect representation:** Broker submits declarations in their own name but on your behalf. Both exporter and broker share legal liability. Used for complex supply chains or high-risk commodities.

### CDS Data Requirements

HMRC's developer guide specifies key data elements:
- Exporter EORI (mandatory)
- Consignee details (name, address, country)
- Commodity code (10-digit UK Trade Tariff code)
- Customs value (transaction value plus applicable adjustments)
- Net mass (kg) and supplementary units (litres, pieces, etc.)
- Preference indicator (whether claiming preferential duty treatment)
- Document references (licences, certificates, invoices)
- Transport details (container numbers, vessel/flight number, port codes)

A 10-digit commodity code identifies goods per the HMRC Tariff, according to UK Trade Info's CDS data descriptions.

### Declaration Supplementary Information

When using simplified procedures, you must submit an export supplementary declaration within **14 days of goods departure**, per GOV.UK guidance. This supplements the pre-shipment advice with final quantities, values, and transport details.

Missing the 14-day deadline risks compliance flags and potential penalties.

## Step 5: Prove Export Left the UK

HMRC requires proof that goods actually departed the UK to validate export declarations and support VAT zero-rating.

### Departure Messages

For most containerised and bulk cargo, the carrier (shipping line, airline, haulier) sends an electronic departure message to HMRC when goods physically leave UK territory. This automatically closes the export declaration in CDS.

However, departure messages are not universal:
- Some smaller carriers lack systems integration with HMRC
- Road freight via Eurotunnel or ferry may not generate automatic departures
- Technical failures can prevent message transmission

### C1602 Form: Manual Proof of Export

When departure messages are not sent, exporters must submit a **C1602 form** to notify HMRC that goods have left the UK. This is mandatory when:
- Excise duty suspended goods are exported without a departure message
- You need to discharge customs special procedures
- Commercial evidence alone is insufficient for VAT zero-rating

The C1602 includes:
- Exporter EORI
- Declaration reference number (MRN)
- Date of export
- Transport details
- Supporting evidence (commercial invoice, CMR, bill of lading)

Submit C1602 forms to the National Clearance Hub via email or post. Retain copies with your export records.

### Commercial Evidence for VAT Zero-Rating

HMRC accepts commercial evidence as proof of export for VAT zero-rating in many cases. Acceptable documents include:
- Signed CMR consignment notes (for road freight to EU)
- Bills of lading showing on-board notation and discharge port
- Air waybills showing flight departure and destination
- Freight forwarder certificates of shipment

The evidence must clearly show:
- Goods description matching the invoice
- Exporter name (you)
- Consignee name and destination outside the UK
- Date of dispatch/departure

For detailed VAT treatment of exports, consult HMRC's VAT Notice 703.

## Step 6: Keep Records for HMRC Compliance

HMRC expects exporters to retain documentation supporting declarations for **4 years** from the date of export. The "Get customs data for import and export declarations" service — in Public Beta as of 11 March 2026 — allows EORI holders to download historical declaration data, but you remain responsible for retaining underlying commercial documents.

### Required Records

HMRC's guidance and UK Trade Info documentation specify retention of:
- **Commercial invoices:** Showing transaction value and goods description
- **Bills of lading / air waybills / CMRs:** Proving shipment and destination
- **Transport documents:** Booking notes, freight invoices, carrier instructions
- **Supplier statements of origin:** Supporting preferential origin claims
- **Export licences:** For controlled goods, including OGL references
- **Classification memos:** Internal records explaining commodity code decisions
- **CDS declaration copies:** MRN references and full declaration data
- **C1602 forms:** If submitted for manual export proof

### Record-Keeping Best Practices

**Digital archiving:** Scan all paper documents and store in structured folders by shipment reference or MRN. Cloud storage with backup ensures accessibility during HMRC audits.

**Cross-referencing:** Link invoices, packing lists, declarations, and transport docs by shipment reference. Auditors appreciate coherent audit trails.

**Retention calendar:** Set reminders to retain records for full 4-year period. Premature deletion risks compliance failures if HMRC requests historical files.

**Access controls:** Restrict editing rights to archived records. Audit trails should show who accessed or modified files.

## Simplified Procedures and Pre-Shipment Advice

Authorised traders can use simplified export procedures to reduce administrative burden.

### Pre-Shipment Advice (PSA)

A PSA notifies HMRC of intended export before goods reach the port. Benefits include:
- Earlier risk assessment by HMRC
- Faster release at the port if no examination required
- Ability to move goods under duty suspension before full declaration

PSAs require:
- Exporter EORI
- Intended commodity codes and values
- Expected departure date and port
- Transport reference (booking number, container number)

After PSA submission, goods can move to the port. A supplementary declaration follows within 14 days of actual departure.

### Simplified Declaration Procedure (SDP)

SDP allows traders to submit initial declarations with reduced data, followed by supplementary declarations within set timeframes. Requires HMRC authorisation demonstrating:
- Satisfactory compliance history
- Adequate record-keeping systems
- Financial solvency

SDP suits high-volume exporters with predictable supply chains.

## Using a Customs Broker vs Self-Representation

Choosing between self-representation and broker assistance depends on volume, complexity, and internal expertise.

### Self-Representation Pros and Cons

**Advantages:**
- Direct control over declaration timing and accuracy
- No broker fees (typically £30-£80 per declaration)
- Internal visibility of commodity codes and classification decisions
- Faster amendments when errors found

**Disadvantages:**
- Requires CDS enrolment and software investment
- Staff training on commodity classification and CDS data requirements
- Full legal liability for errors rests with you
- Time burden for low-volume exporters

### Broker Representation Pros and Cons

**Advantages:**
- Expertise in commodity classification and licence requirements
- Established CDS connectivity and processes
- Reduced internal resource burden
- Brokers often catch errors before submission

**Disadvantages:**
- Per-declaration fees add up for high-volume exporters
- Less direct control over timing
- Communication delays if broker manages multiple clients
- You remain legally responsible even if broker makes errors

### Hybrid Approach

Many exporters use brokers for complex shipments (controlled goods, high-value, new destinations) while self-declaring routine, low-risk exports. This balances cost control with risk management.

## VAT Zero-Rating and Proof of Export

UK exports are generally zero-rated for VAT purposes — you charge 0% VAT but can reclaim input VAT on related costs. HMRC requires proof of export to justify zero-rating.

### Conditions for VAT Zero-Rating

To zero-rate exports:
1. Goods must physically leave the UK within prescribed time limits (typically 3 months from sale)
2. You must hold commercial evidence of export (invoice, transport docs)
3. For EU destinations: evidence the customer is a taxable person (VAT number validation via VIES)
4. For non-EU destinations: customs declaration showing export

### When VAT Becomes Chargeable

If goods do not leave the UK within the allowed timeframe, or if proof of export is insufficient, HMRC may assess output VAT at the standard rate (20%). This can create significant unexpected liabilities.

Maintain robust tracking of export shipments and follow up on missing departure messages promptly.

## Common Mistakes to Avoid

**Incorrect commodity codes:** Misclassification leads to wrong licence requirements, incorrect duty treatment, and potential penalties. Use the UK Trade Tariff tool and consider binding tariff information (BTI) rulings for high-value or frequently exported products. See our [Commodity Code Classification guide](/articles/commodity-code-classification-tips/) for detailed classification tips.

**Missing licence declarations:** Failing to declare export licences on CDS triggers compliance holds. Always cross-check controlled goods against current OGL and individual licence requirements.

**EORI mismatches:** Ensure the EORI on declarations matches the EORI on licences, invoices, and transport docs. Inconsistencies cause CDS rejections.

**Late supplementary declarations:** The 14-day deadline for supplementary declarations is strict. Set internal reminders tied to shipment departure dates.

**Inadequate record-keeping:** HMRC audits can reach back 4 years. Missing documents complicate audits and may support penalty assessments.

**Assuming EU exports are "domestic":** Post-Brexit, exports to EU countries require full export declarations. The common travel area (UK, Ireland, Channel Islands, Isle of Man) is the only exception.

## Frequently Asked Questions

**Do I need an export declaration for goods going to the EU?**
Yes. Post-Brexit, all goods leaving the UK for EU destinations require export declarations via CDS. The only exceptions are goods moving within the common travel area (UK, Ireland, Channel Islands, Isle of Man).

**How long does it take to get an EORI number?**
HMRC typically issues EORI numbers within 3-5 working days for VAT-registered businesses. Non-VAT registered entities may take longer. Apply before you need to export — you cannot submit declarations without a valid EORI.

**What happens if I miss the 14-day supplementary declaration deadline?**
Late supplementary declarations trigger compliance flags in CDS. Repeated failures may result in HMRC audits, penalties, or suspension of simplified procedure authorisations. Submit late declarations immediately upon realising the delay.

**Can I use my EU EORI for UK exports?**
No. UK export declarations require a GB-prefixed EORI. EU-issued EORIs (DE-, FR-, IE-, etc.) are not valid for UK customs purposes post-Brexit.

**Do I need an export licence for ordinary consumer goods?**
Generally no. Most consumer goods (clothing, furniture, non-electronic items) do not require export licences. Licences apply to military goods, dual-use technologies, certain chemicals, cultural artefacts, and goods destined for sanctioned countries.

**What is the C1602 form used for?**
Form C1602 manually notifies HMRC that goods have left the UK when automatic departure messages are not sent. It is mandatory for excise duty suspended goods exported without departure messages and useful for proving export for VAT zero-rating when carrier systems fail.

**How long must I keep export records?**
HMRC requires exporters to retain all export-related documentation for 4 years from the date of export. This includes invoices, transport documents, declarations, licences, and classification records.

**Can my freight forwarder submit export declarations on my behalf?**
Yes. Freight forwarders and customs brokers can submit declarations under direct or indirect representation. Under direct representation, you remain legally responsible for accuracy. Under indirect representation, both you and the broker share liability.
