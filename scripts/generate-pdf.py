#!/usr/bin/env python3
"""
Generate branded PDF documents for LogisticsEdge products.

Usage:
  python3 scripts/generate-pdf.py input.md output.pdf [--title "Document Title"]

Converts markdown to a styled, branded PDF using reportlab.
Supports: headings, paragraphs, bullet lists, tables, bold, italic, horizontal rules.
"""

import sys
import os
import re
import argparse
import markdown
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, ListFlowable, ListItem
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Brand colours
NAVY = HexColor('#0f172a')
ACCENT = HexColor('#3b82f6')
TEXT = HexColor('#1e293b')
TEXT_LIGHT = HexColor('#64748b')
BORDER = HexColor('#e2e8f0')
BG_SOFT = HexColor('#f8fafc')
WHITE = HexColor('#ffffff')


def create_styles():
    """Create branded paragraph styles."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'BrandTitle',
        parent=styles['Title'],
        fontSize=24,
        textColor=NAVY,
        spaceAfter=6 * mm,
        leading=30,
    ))

    styles.add(ParagraphStyle(
        'BrandH1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=NAVY,
        spaceBefore=10 * mm,
        spaceAfter=4 * mm,
        leading=24,
    ))

    styles.add(ParagraphStyle(
        'BrandH2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=NAVY,
        spaceBefore=8 * mm,
        spaceAfter=3 * mm,
        leading=20,
    ))

    styles.add(ParagraphStyle(
        'BrandH3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=NAVY,
        spaceBefore=6 * mm,
        spaceAfter=2 * mm,
        leading=16,
        fontName='Helvetica-Bold',
    ))

    styles.add(ParagraphStyle(
        'BrandBody',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT,
        spaceAfter=3 * mm,
        leading=15,
    ))

    styles.add(ParagraphStyle(
        'BrandBullet',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT,
        leftIndent=8 * mm,
        spaceAfter=1.5 * mm,
        leading=14,
        bulletIndent=3 * mm,
    ))

    styles.add(ParagraphStyle(
        'BrandFooter',
        parent=styles['Normal'],
        fontSize=7,
        textColor=TEXT_LIGHT,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        'BrandSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=TEXT_LIGHT,
        spaceAfter=8 * mm,
        leading=16,
        alignment=TA_CENTER,
    ))

    return styles


def header_footer(canvas, doc):
    """Add header and footer to every page."""
    canvas.saveState()

    # Header line
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(2)
    canvas.line(20 * mm, A4[1] - 15 * mm, A4[0] - 20 * mm, A4[1] - 15 * mm)

    # Header text
    canvas.setFont('Helvetica-Bold', 8)
    canvas.setFillColor(NAVY)
    canvas.drawString(20 * mm, A4[1] - 13 * mm, 'LogisticsEdge')

    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(ACCENT)
    canvas.drawRightString(A4[0] - 20 * mm, A4[1] - 13 * mm, 'logisticsedge.co.uk')

    # Footer
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)

    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(TEXT_LIGHT)
    canvas.drawString(20 * mm, 10 * mm, f'LogisticsEdge — UK Logistics Intelligence')
    canvas.drawRightString(A4[0] - 20 * mm, 10 * mm, f'Page {doc.page}')

    canvas.restoreState()


def md_to_flowables(md_text, styles):
    """Convert markdown text to reportlab flowables."""
    flowables = []
    lines = md_text.split('\n')
    i = 0
    in_table = False
    table_rows = []

    while i < len(lines):
        line = lines[i].rstrip()

        # Skip empty lines
        if not line:
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^-{3,}$|^\*{3,}$|^_{3,}$', line):
            flowables.append(Spacer(1, 3 * mm))
            flowables.append(HRFlowable(width='100%', thickness=1, color=BORDER))
            flowables.append(Spacer(1, 3 * mm))
            i += 1
            continue

        # Headings
        h_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if h_match:
            level = len(h_match.group(1))
            text = process_inline(h_match.group(2))
            style_name = f'BrandH{level}'
            if style_name in [s.name for s in styles.byName.values()]:
                flowables.append(Paragraph(text, styles[style_name]))
            else:
                flowables.append(Paragraph(text, styles['BrandH3']))
            i += 1
            continue

        # Table row
        if '|' in line and not line.startswith('```'):
            cells = [c.strip() for c in line.split('|')]
            cells = [c for c in cells if c]  # Remove empty from leading/trailing |

            # Skip separator rows
            if all(re.match(r'^[-:]+$', c) for c in cells):
                i += 1
                continue

            if not in_table:
                in_table = True
                table_rows = []

            table_rows.append(cells)
            i += 1

            # Check if next line is still table
            if i >= len(lines) or '|' not in lines[i]:
                # Render table
                in_table = False
                if table_rows:
                    flowables.extend(render_table(table_rows, styles))
                    table_rows = []
            continue

        # Bullet list
        bullet_match = re.match(r'^[-*]\s+(.+)$', line)
        if bullet_match:
            text = process_inline(bullet_match.group(1))
            flowables.append(Paragraph(f'\u2022  {text}', styles['BrandBullet']))
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^(\d+)\.\s+(.+)$', line)
        if num_match:
            num = num_match.group(1)
            text = process_inline(num_match.group(2))
            flowables.append(Paragraph(f'{num}.  {text}', styles['BrandBullet']))
            i += 1
            continue

        # Checkbox list
        check_match = re.match(r'^-\s+\[[ x]\]\s+(.+)$', line)
        if check_match:
            text = process_inline(check_match.group(1))
            flowables.append(Paragraph(f'\u2610  {text}', styles['BrandBullet']))
            i += 1
            continue

        # Blockquote
        quote_match = re.match(r'^>\s+(.+)$', line)
        if quote_match:
            text = process_inline(quote_match.group(1))
            quote_style = ParagraphStyle(
                'Quote',
                parent=styles['BrandBody'],
                leftIndent=10 * mm,
                textColor=TEXT_LIGHT,
                fontName='Helvetica-Oblique',
            )
            flowables.append(Paragraph(text, quote_style))
            i += 1
            continue

        # Regular paragraph
        para_lines = [line]
        while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r'^[#\-*>|]|^\d+\.', lines[i + 1]):
            i += 1
            para_lines.append(lines[i].rstrip())

        text = process_inline(' '.join(para_lines))
        flowables.append(Paragraph(text, styles['BrandBody']))
        i += 1

    return flowables


def process_inline(text):
    """Convert markdown inline formatting to reportlab XML tags."""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<font face="Courier" size="9">\1</font>', text)
    # Links — just show text
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'<u>\1</u>', text)
    # Escape XML entities
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Restore our tags
    text = text.replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
    text = text.replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>')
    text = text.replace('&lt;u&gt;', '<u>').replace('&lt;/u&gt;', '</u>')
    text = text.replace('&lt;font', '<font').replace('&lt;/font&gt;', '</font>')
    text = re.sub(r'&gt;(")', r'>\1', text)  # fix closing font tag
    return text


def render_table(rows, styles):
    """Render a markdown table as a reportlab Table."""
    flowables = []

    if not rows:
        return flowables

    # Normalize column count
    max_cols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < max_cols:
            r.append('')

    # Convert to paragraphs
    table_data = []
    for ri, row in enumerate(rows):
        table_row = []
        for cell in row:
            text = process_inline(cell.strip('*'))
            if ri == 0:
                style = ParagraphStyle('TH', parent=styles['BrandBody'], fontSize=8,
                                       textColor=WHITE, fontName='Helvetica-Bold')
            else:
                style = ParagraphStyle('TD', parent=styles['BrandBody'], fontSize=9)
            table_row.append(Paragraph(text, style))
        table_data.append(table_row)

    col_width = (A4[0] - 40 * mm) / max_cols
    t = Table(table_data, colWidths=[col_width] * max_cols)

    table_style = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, BG_SOFT]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]

    t.setStyle(TableStyle(table_style))
    flowables.append(Spacer(1, 3 * mm))
    flowables.append(t)
    flowables.append(Spacer(1, 5 * mm))
    return flowables


def build_pdf(input_path, output_path, title=None):
    """Build a branded PDF from a markdown file."""
    with open(input_path, 'r') as f:
        content = f.read()

    # Strip YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()

    styles = create_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
    )

    flowables = []

    # Title page
    if title:
        flowables.append(Spacer(1, 40 * mm))
        flowables.append(Paragraph(title, styles['BrandTitle']))
        flowables.append(Paragraph(
            'LogisticsEdge — UK Logistics, Customs &amp; Supply Chain Intelligence',
            styles['BrandSubtitle']
        ))
        flowables.append(HRFlowable(width='60%', thickness=2, color=ACCENT))
        flowables.append(Spacer(1, 10 * mm))
        flowables.append(Paragraph(
            'logisticsedge.co.uk',
            styles['BrandSubtitle']
        ))
        flowables.append(PageBreak())

    # Content
    flowables.extend(md_to_flowables(content, styles))

    # Build
    doc.build(flowables, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f'Generated: {output_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate branded LogisticsEdge PDF')
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('output', help='Output PDF path')
    parser.add_argument('--title', help='Document title for cover page', default=None)
    args = parser.parse_args()

    build_pdf(args.input, args.output, args.title)
