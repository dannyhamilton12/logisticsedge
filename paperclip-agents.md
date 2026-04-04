# Paperclip Agent Configuration — LogisticsEdge

## Project 1: Content Production Agent (Sonnet)

**Purpose:** Write new SEO-optimised articles from the content plan.
**Model:** Sonnet
**Cadence:** 3-4 articles per week
**Priority order:** Work through content-plan.md, High priority first

### Heartbeat Procedure

1. Wake up, check inbox for new tasks
2. Pick the next unwritten High-priority article from content-plan.md
3. Write the article as a markdown file in `src/content/articles/{slug}.md`
4. Run `./scripts/fetch-image.sh "{relevant search terms}" "{slug}"` to download a hero image
5. Ensure frontmatter includes all required fields:
   - title, description, pubDate (today's date), author ("LogisticsEdge"), category, tags, image, draft (false)
6. Include minimum 3 internal links using the linking map in content-plan.md
7. Git add, commit with message: "Add article: {title}"
8. Push to main
9. Update task status in Paperclip
10. Move to next article

### Article Template

```markdown
---
title: "{Title}"
description: "{SEO description, 150-160 chars}"
pubDate: {YYYY-MM-DD}
author: "LogisticsEdge"
category: "{category}"
tags: ["{tag1}", "{tag2}", "{tag3}"]
image: "/images/articles/{slug}.jpg"
draft: false
---

## Key Takeaways

- {3-5 bullet points summarising the most important points}

---

## {First main section}

{Content — practical, direct, UK-focused}

## {Second main section}

{Content with examples, data, or tables where relevant}

## {Third main section}

{Content}

## Frequently Asked Questions

**{Question 1}**
{Answer}

**{Question 2}**
{Answer}

**{Question 3}**
{Answer}
```

### Writing Rules

- UK English spelling throughout (organisation, colour, authorised, etc.)
- Lead with practical value, not theory
- Include specific UK data, thresholds, and HMRC references where relevant
- Tables for comparison content (rates, options, features)
- No filler phrases ("In today's fast-paced world", "It's important to note that")
- Every article must link to at least 3 other articles on the site
- Target 1,500-2,500 words
- Include a FAQ section with 3-5 questions targeting "People Also Ask" snippets

---

## Project 2: Content Refresh Agent (Haiku)

**Purpose:** Audit existing articles for outdated info, broken links, and missing internal links.
**Model:** Haiku
**Cadence:** Weekly scan of all published articles

### Heartbeat Procedure

1. Wake up, scan all files in `src/content/articles/`
2. For each article, check:
   - Are any dates, thresholds, or regulatory references outdated?
   - Does it have at least 3 internal links to other articles on the site?
   - Are all internal links pointing to valid slugs that exist?
   - Is the `updatedDate` field set if content was modified?
3. If issues found:
   - Fix missing internal links by adding relevant cross-references
   - Flag outdated content in a Paperclip issue for human review
   - Add `updatedDate` to frontmatter when making changes
4. Git add, commit: "Refresh: update internal links and references in {slug}"
5. Push to main

### Link Injection Rules

When adding internal links, place them naturally within the text. Examples:

- "You will need an EORI number — see our [complete EORI guide](/articles/eori-number-uk-complete-guide/) for how to apply."
- "The duty rate depends on your goods' commodity code. Our [commodity codes guide](/articles/uk-commodity-codes-tariff-classification-guide/) walks through classification step by step."
- "If you are using a third-party logistics provider, read our [3PL guide](/articles/what-is-3pl-definitive-uk-guide/) to understand what to look for."

---

## Project 3: Internal Linking Agent (Haiku)

**Purpose:** Ensure every article on the site is properly cross-linked for SEO.
**Model:** Haiku
**Cadence:** Runs after every new article is published

### Heartbeat Procedure

1. Wake up when notified of a new article publication
2. Read the new article to identify its topics and keywords
3. Scan all OTHER articles on the site
4. For each existing article:
   - If it mentions a topic covered by the new article AND doesn't already link to it, add a natural contextual link
   - Maximum 1 new link added per existing article per run
5. For the new article:
   - Verify it links to at least 3 existing articles
   - If not, add links where relevant
6. Git add, commit: "SEO: add cross-links for {new-article-slug}"
7. Push to main

---

## Repository Structure Reference

```
src/content/articles/     — All article markdown files
src/content/products/     — Product markdown files
public/images/articles/   — Article hero images (800x400 JPEG)
scripts/fetch-image.sh    — Image download script
content-plan.md           — Master content plan with all targets
```

## Categories (use exactly these values)

- customs
- logistics
- trade
- supply-chain
- warehousing
- compliance
