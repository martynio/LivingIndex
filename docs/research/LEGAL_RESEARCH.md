# LI-002 — Data rights and website legal-readiness research

**Checked:** 2026-11-10 · **Status:** preliminary official-source review only. **This is not legal advice, a compliance certification, or a publishable Privacy Policy/Terms of Use.**

## Dataset reuse findings

| Publisher | Primary policy / record | Preliminary conclusion | Gate |
| --- | --- | --- | --- |
| CBS | [CBS copyright](https://www.cbs.nl/en-gb/over-ons/website/copyright); [`71905ned` metadata](https://dataportal.cbs.nl/detail/CBS/71905ned) | CBS website content generally CC BY 4.0 unless specified; `71905ned` metadata explicitly states CC BY 4.0 | Attribute CBS, identify changes and dataset, do not use its logo/style or imply endorsement; check each dataset individually |
| GUS / Statistics Poland | [BIP reuse terms](https://bip.stat.gov.pl/en/contact-with-the-office/reuse-of-public-sector-information/) | Reuse of public-sector information is provided under national reuse law; source, creation/acquisition time and processing information should be disclosed | Record exact download and transformation provenance; verify any product-specific exclusions and rights |
| Eurostat | [Copyright notice and free re-use](https://ec.europa.eu/eurostat/help/copyright-notice) | Statistical data generally reusable with attribution for commercial and non-commercial uses; individual/third-party conditions may override | Cite DOI/dataset code and access date, indicate modifications, verify exceptions and access restrictions |
| CBS microdata | [Budget survey microdata listing](https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen/microdatabestanden/budgetonderzoek-bestedingen-particuliere-huishoudens) | Public listing **does not authorize redistribution of microdata** | Keep out of public repo; review access/derived disclosure rules separately |

**No raw files or numeric series have been redistributed as part of LI-002.** An attribution statement must name the *exact* table and source version; an institution link alone is inadequate.

## Website regulatory research (Netherlands/EU)

- [European Commission — information for individuals](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en): where personal data is processed, give concise understandable notice of purpose, controller, rights and relevant processing details under GDPR transparency rules.
- [Dutch government — cookies](https://business.gov.nl/regulations/cookies/), [Dutch AP — cookie policy](https://autoriteitpersoonsgegevens.nl/themas/internet-slimme-apparaten/cookies/cookies-en-uw-organisatie-zorg-voor-een-goed-beleid): functional or strictly limited privacy-friendly analytics may not require prior opt-in; tracking does. Notice and actual settings matter. **Do not deploy a cookie banner by default before confirming technologies.**
- [Dutch government — business website](https://business.gov.nl/starting-your-business/first-steps/creating-a-business-website/) and [business correspondence / website identity](https://business.gov.nl/regulations/rules-business-correspondence/): operator/business identity information requirements vary with the actual activity; a neutral product brand must not be mistaken for an assurance of legal anonymity.
- [European Data Protection Board — FAQs](https://www.edpb.europa.eu/contact/frequently-asked-questions_en): access to terminal storage and personal-data tracking can trigger consent rules; processing cannot be treated as absent solely because there are no account forms.

## Decisions required **before LI-003 website publication**

1. Choose **actual** host, domain and deployment location; identify the responsible site operator/controller according to actual project organization and legal status.
2. Inventory every frontend/third-party request: hosting access logs, analytics, fonts, CDN, embedded media, error collection, forms, language preference storage and external data requests.
3. Determine whether any cookies/local storage/tracking are used and which require consent. Test before and after consent if relevant.
4. Confirm the legal contact route and legally required operator details for the **actual activity**; avoid inventing address/company/VAT numbers.
5. Write real **Privacy Notice**, **Cookie Information** (where relevant), **Terms/Disclaimer**, **Data Sources/Methodology** based on measured behavior; arrange appropriate review before publication.
6. Keep code license separate from source data terms and source provider trademarks; do not imply public GitHub visibility means an open-source grant.
7. Confirm retention periods, processors, relevant international transfers, user-rights contact path, and any consent records if personal data is processed.

## Not established

- No hosting or analytics setup was inspected.
- No deployed site request/cookie scan has occurred.
- No contact/operator details, privacy notice, cookie banner, website terms, or legal pages are approved.
- No dataset redistribution or special microdata release clearance has been completed.

**Gate:** this is a requirements checklist, not confirmation of GDPR compliance. Review the actual deployed behavior in LI-003 before publication.
