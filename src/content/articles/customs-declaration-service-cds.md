---
title: "UK Customs Declaration Service (CDS): The Complete Guide for Importers and Exporters"
description: "Comprehensive guide to CDS — HMRC's modern customs platform replacing CHIEF. Key differences, data requirements, procedure codes, and compliance essentials for UK trade."
pubDate: 2026-04-06
author: "LogisticsEdge"
category: "customs"
tags: ["cds", "customs declaration service", "chief", "customs declarations", "hmrc", "import declarations", "export declarations", "post-brexit customs", "eori", "customs procedure codes"]
image: "/images/articles/customs-declaration-service-cds.jpg"
draft: false
---

## Key Takeaways

- **CDS is now mandatory** — CHIEF fully closed for imports (September 2022) and exports (June 2024)
- **More data required** — CDS uses 60+ data elements vs CHIEF's simpler format
- **Real-time tracking** — Get instant declaration status updates and notifications
- **Integrated payments** — Duty deferment, cash accounts, and guarantees in one system
- **Procedure codes matter** — H1 (standard import), H2 (warehouse), H3 (inward processing), and more

---

The Customs Declaration Service (CDS) is now the sole platform for submitting import and export declarations in the United Kingdom. Following the complete decommissioning of the legacy CHIEF (Customs Handling of Import and Export Freight) system, every business moving goods across UK borders must understand how CDS works — whether handling declarations in-house or working with a customs agent.

This guide covers everything UK traders need to know: what changed from CHIEF, how to access CDS, the specific data requirements, common errors to avoid, and practical steps for compliance.

## What Is the Customs Declaration Service?

The Customs Declaration Service is HMRC's modern digital platform for processing customs declarations. Unlike CHIEF, which had been in operation since 1994, CDS was built using contemporary technology and aligns with the EU's Union Customs Code (UCC) data model.

CDS manages the complete lifecycle of a customs declaration:

- **Submission** — Initial declaration entry via portal, software, or API
- **Validation** — Automatic checks against tariff data, licences, and restrictions
- **Clearance** — Risk assessment and customs checks
- **Payment** — Duty and VAT calculation with integrated payment options
- **Post-clearance** — Amendments, audits, and dispute resolution

### Why CHIEF Had to Go

CHIEF served UK trade for nearly 30 years, but it faced fundamental limitations:

| Issue | Impact |
|-------|--------|
| **Legacy technology** | Built on 1990s architecture; costly to maintain and update |
| **Limited data model** | Couldn't support modern customs requirements or UCC alignment |
| **Brexit complexity** | Insufficient flexibility for post-EU customs arrangements |
| **Separate systems** | Duty payments, deferments, and guarantees ran on disconnected platforms |
| **End of life** | NCTS Phase 5 transition made CHIEF incompatible with EU transit systems |

## CDS Timeline — When Everything Changed

Understanding the phased transition helps explain why CDS is now the only option:

### Phase 1: Northern Ireland (2021)
- **31 October 2021** — All imports from Rest of World to Northern Ireland required CDS
- **31 December 2021** — Full Northern Ireland Protocol implementation

### Phase 2: Great Britain Imports (2022)
- **30 September 2022** — CHIEF closed for new import declarations in Great Britain
- **November 2023** — Complete switch-off of CHIEF import functionality

### Phase 3: Export Transition (2024)
- **4 June 2024** — CHIEF closed for export declarations
- **Late 2024** — Full CHIEF decommissioning

**Current status:** As of 2026, CHIEF no longer exists. All UK customs declarations must use CDS.

## CDS vs CHIEF: Detailed Comparison

| Feature | CHIEF | CDS |
|---------|-------|-----|
| **Data format** | SAD (Single Administrative Document) | WCO data model with 60+ data elements |
| **Commodity codes** | 8-digit acceptable | 10-digit required for imports |
| **Procedure codes** | 7-digit single code | 4-digit + up to 99 3-digit codes |
| **Real-time status** | Limited visibility | Full tracking and notifications |
| **Post-clearance amendments** | Paper-based, slow | Digital self-service |
| **Payment integration** | Separate systems | Cash accounts, deferment, guarantees unified |
| **API connectivity** | Restricted | Modern REST APIs |
| **Security** | Basic authentication | Government Gateway + MFA |

### Key Data Differences

CDS requires significantly more information than CHIEF:

**New or Expanded Requirements:**
- Additional procedure codes (second part)
- Comprehensive consignor/consignee details
- Detailed freight and insurance breakdowns
- Specific document references (not just "LIC99")
- Location of goods and border crossing points
- Guarantees and security references where applicable

**Validation Changes:**
- CDS validates commodity codes in real-time against the UK Trade Tariff
- Procedure codes must align precisely with intended use
- Prohibitions and restrictions require explicit declaration

## How to Access CDS

There are three primary methods for submitting declarations:

### 1. CDS Exporter/Importer Portal (Free)

HMRC's web-based portal for businesses making their own declarations.

**Best for:** Low-volume traders with simple, straightforward imports

**Access requirements:**
- Government Gateway account
- UK EORI number (GB + 12 digits)
- CDS subscription

**Limitations:**
- Manual data entry required
- No bulk upload functionality
- Limited integration with business systems
- Not suitable for high volumes

### 2. Commercial Software

Third-party customs declaration software that connects to CDS via API.

**Best for:** Regular importers/exporters with established customs processes

**Features typically include:**
- Address book for regular suppliers/customers
- Template declarations for common shipments
- Integration with ERP and warehouse systems
- Automated validation before submission
- Management reporting and audit trails

**Popular providers:**
- CustomsWare
- Descartes CustomsInfo
- Agency Manager (ASM)
- iCustoms
- AEB customs software

### 3. Customs Intermediary

Using a customs broker, freight forwarder, or agent to submit declarations on your behalf.

**Best for:** Businesses without customs expertise or those importing occasionally

**What they handle:**
- Classification of goods and commodity codes
- Completion of declarations
- Payment of duties and taxes
- Liaison with HMRC on queries
- Post-clearance amendments

**Important note:** You remain legally responsible for the accuracy of declarations, even when using an agent.

## Getting Started: CDS Registration

Before submitting declarations, you must complete these steps:

### Step 1: Obtain an EORI Number

All UK businesses trading goods internationally need an Economic Operator Registration and Identification (EORI) number.

**Format:** GB followed by 12 digits (e.g., GB123456789012)

**Application:**
- Apply online via HMRC website
- Most VAT-registered businesses receive EORI within hours
- Non-VAT businesses may take 3-5 working days

### Step 2: Subscribe to CDS

Log into your Government Gateway account and:

1. Navigate to "Get access to a tax, duty or scheme"
2. Select "Customs Declaration Service"
3. Enter your EORI number
4. Complete the subscription process

### Step 3: Set Up Payment Methods

**Option A: CDS Cash Account**
- Pre-fund account with HMRC
- Duty and VAT deducted at declaration
- Suitable for occasional importers

**Option B: Duty Deferment Account**
- Defer payment to monthly direct debit
- Requires Customs Comprehensive Guarantee or bank guarantee
- Best for regular importers with cash flow considerations

### Step 4: Authorise Your Agent (If Applicable)

If using a customs intermediary:

1. Log into your HMRC account
2. Navigate to "Customs Declare Service"
3. Select "Manage who can access your customs account"
4. Add your agent using their EORI number
5. Set authorisation level (submit declarations, view only, etc.)

## CDS Declaration Types and Procedure Codes

Every CDS declaration requires a procedure code that defines what's happening to the goods. Understanding these codes is essential for correct classification.

### Import Procedure Codes

**H1 — Release for Free Circulation**
- Standard import where goods enter UK market
- Duty and VAT payable immediately or deferred
- Most common procedure code

**H2 — Customs Warehousing**
- Goods stored in authorised warehouse
- Duty suspended until removal
- Useful for bulk importers and distributors

**H3 — Inward Processing**
- Goods imported for processing/manufacturing
- Must be re-exported or placed on market after processing
- Duty relief on import; duty payable if diverted to UK market

**H4 — Temporary Admission**
- Goods imported temporarily (exhibitions, repairs, events)
- Full duty and VAT relief
- Must be re-exported within specified period

**H5 — End-Use Relief**
- Reduced or zero duty for specific purposes
- Examples: aircraft parts, research equipment, charity goods
- End-use must be declared and monitored

**I1 — Simplified Declaration**
- Reduced data at frontier
- Supplementary declaration required within set timeframe
- For authorised traders with simplified procedures

### Export Procedure Codes

**B1 — Export with outright sale**
- Standard export with permanent transfer of ownership
- Most common export procedure

**B2 — Export under outward processing**
- Goods exported for processing/repair
- Re-imported with duty relief on added value only

## Data Requirements for CDS Declarations

A complete CDS import declaration contains 60+ data elements. The key fields include:

### Mandatory Core Data

**EORI Numbers**
- Declarant (agent or business submitting)
- Importer/exporter (if different)

**Commodity Codes**
- 10-digit codes for imports (from UK Trade Tariff)
- 8-digit codes for exports
- Must be accurate to product specifications

**Customs Procedure Codes**
- Primary procedure code (4 digits)
- Additional procedure codes (3 digits each)
- Must align with intended goods use

**Valuation**
- Customs value (transaction value + freight + insurance)
- Currency code (GBP, USD, EUR, etc.)
- Method of valuation (1-6)

**Origin**
- Country of origin code
- Preference indicator (if claiming trade agreement benefits)
- Evidence of origin where required

### Supplementary Data

**Transport Information**
- Mode of transport at border
- Port of entry/exit
- Carrier details
- Expected arrival/departure

**Location and Warehousing**
- Location of goods
- Warehouse reference (if applicable)
- Supervising office

**Documents and Licences**
- Commercial invoice reference
- Packing list
- Import/export licences
- Certificates of origin
- Preference documents (EUR.1, supplier declarations)

**Financial Guarantees**
- Deferment account number
- Guarantee reference
- Security reference where required

## Common CDS Errors and How to Avoid Them

Even experienced traders encounter CDS rejections. Here are the most common issues:

### 1. Incorrect Commodity Codes

**Problem:** Using an 8-digit code where 10 digits are required, or misclassifying products.

**Impact:** Declaration rejected or incorrect duty calculation.

**Solution:**
- Use the UK Trade Tariff tool for classification
- Consider binding tariff information (BTI) for uncertain classifications
- Consult customs broker for complex products

### 2. Procedure Code Mismatches

**Problem:** Import procedure codes used for exports, or vice versa.

**Impact:** Immediate rejection.

**Solution:**
- Double-check code before submission
- Maintain reference document with common codes for your products

### 3. Missing or Incorrect Origin Evidence

**Problem:** Claiming preferential duty rates without proper documentation.

**Impact:** Full duty charged; potential penalties.

**Solution:**
- Obtain EUR.1 movement certificates or supplier declarations
- Ensure origin criteria are met (typically 50%+ originating content)
- Keep evidence for at least 3 years

### 4. Incomplete Consignor/Consignee Details

**Problem:** CDS requires full address details where CHIEF accepted minimal information.

**Impact:** Declaration rejected pending additional data.

**Solution:**
- Collect complete supplier/customer details
- Maintain accurate address book in customs software

### 5. Document Reference Errors

**Problem:** Using "LIC99" (CHIEF convention) instead of specific document references.

**Impact:** CDS requires explicit declaration of all prohibitions and restrictions.

**Solution:**
- List specific licence numbers
- Reference relevant certificates and authorisations

### 6. Incorrect Valuation

**Problem:** Omitting freight or insurance costs from customs value.

**Impact:** Underpayment of duty; potential penalties and interest.

**Solution:**
- Include all costs up to UK border
- Use Incoterms to determine appropriate additions
- Maintain calculation worksheets

## CDS Costs and Practical Considerations

### Software Costs

If using commercial software:

- **Entry-level:** £50-200 per month (basic declaration capability)
- **Mid-range:** £200-500 per month (templates, reporting, some integration)
- **Enterprise:** £500+ per month (full ERP integration, advanced analytics)

### Agent Fees

Customs intermediary charges typically:

- **Simple declarations:** £25-45 per entry
- **Complex declarations:** £50-150+ per entry
- **Annual contracts:** Often include volume discounts

### Duty Deferment Costs

- **Customs Comprehensive Guarantee:** 0% cash cover for established traders
- **Bank guarantee:** Typically 1-3% of guarantee value annually
- **Monthly administration fee:** £15-50 per deferment account

### Training Requirements

Staff need training on:

- CDS data requirements and validation
- Commodity code classification
- Procedure code selection
- Documentation standards

**Training providers:**
- British International Freight Association (BIFA)
- Institute of Export & International Trade
- HMRC webinars and guidance
- Software vendor training programmes

## Post-Transition Challenges

Businesses still adapting to CDS face ongoing challenges:

### Integration Issues

Connecting existing ERP systems to CDS requires:

- API development or middleware
- Data mapping from internal formats to CDS requirements
- Testing and validation before going live

**Timeline:** 3-6 months for complex integrations

### Data Quality

CDS validates more rigorously than CHIEF. Common quality issues:

- Inconsistent product descriptions
- Outdated supplier/customer records
- Missing preference documentation
- Incorrect units of measurement

### Brexit-Related Complexity

Post-EU trade adds layers:

- Rules of origin calculations
- Additional documentation for EU goods
- Divergent UK/EU tariff rates
- Dual NI/GB considerations

## Northern Ireland Considerations

The Northern Ireland Protocol creates unique CDS requirements:

### Dual Tariff System

- **Green lane:** Goods staying in NI — simplified procedures
- **Red lane:** Goods at risk of entering EU — full customs declarations

### Trader Support Service (TSS)

Free service for Northern Ireland traders:

- Completes declarations on behalf of traders
- Helps with goods at risk determinations
- Provides tariff and duty calculation

## CDS Benefits Beyond Compliance

Despite the transition challenges, CDS offers genuine advantages:

### Real-Time Visibility

- Instant declaration status updates
- Email/SMS notifications for clearance, queries, and rejections
- Dashboard view of all declarations and financial positions

### Financial Management

- Single view of cash accounts, deferments, and guarantees
- Detailed transaction history
- Easier reconciliation and auditing

### Compliance Improvements

- Better audit trails
- Reduced manual errors through validation
- Easier post-clearance amendments
- Enhanced security and fraud prevention

### Future-Proofing

- Built to accommodate new trade agreements
- Regular HMRC updates and improvements
- Integration with emerging border technologies

## Getting Help with CDS

### HMRC Resources

- **CDS guidance pages:** gov.uk/guidance/customs-declaration-service
- **Trade Tariff tool:** trade-tariff.service.gov.uk
- **Trader support helpline:** 0300 322 9434
- **Webinars:** Regular free sessions on CDS topics

### Industry Support

- **British International Freight Association (BIFA):** bifa.org
- **Institute of Export:** export.org.uk
- **Make UK:** makeuk.org
- **British Chambers of Commerce:** bcc.org.uk

### Professional Advice

For complex situations:

- Customs consultants
- Trade lawyers
- Specialist brokers
- Big four accountancy firms (for enterprise scale)

## Action Checklist for CDS Compliance

### Immediate Actions

- [ ] Verify EORI number is active and correct
- [ ] Subscribe to CDS via Government Gateway
- [ ] Set up payment method (cash account or deferment)
- [ ] If using an agent, complete authorisation

### System Preparation

- [ ] Choose access method (portal, software, or agent)
- [ ] If software: complete integration and testing
- [ ] Train relevant staff on CDS requirements
- [ ] Create internal procedures and documentation

### Ongoing Management

- [ ] Maintain accurate commodity code database
- [ ] Keep supplier/customer details up to date
- [ ] Monitor declaration rejections and errors
- [ ] Review and optimise processes quarterly

## Conclusion

The Customs Declaration Service represents a fundamental modernisation of UK customs infrastructure. While the transition from CHIEF required significant adjustment, CDS provides a more robust, flexible, and internationally aligned platform for managing UK trade declarations.

For most businesses, working with a customs intermediary offers the smoothest path to CDS compliance. For larger traders, investing in compliant software and internal expertise pays dividends in efficiency and control.

The key to CDS success is data accuracy, staff training, and choosing the right access method for your trade volume and complexity. With CHIEF now fully retired, mastering CDS isn't optional — it's essential for any UK business trading internationally.

---

*Last updated: April 2026*

*For the latest CDS guidance and updates, visit [HMRC's official CDS page](https://www.gov.uk/guidance/customs-declaration-service)*