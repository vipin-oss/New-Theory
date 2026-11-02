#!/usr/bin/env python3
"""Create the requested PDF list; install reportlab to run."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

items = [
('Ivanov and Pandolfi (2009)', 'Heat equation with memory: Lack of controllability to rest', '10.1016/j.jmaa.2009.01.008', 'Highest priority: original full proof.'),
('Fattorini and Russell (1971)', 'Exact controllability theorems for linear parabolic equations in one space dimension', '10.1007/BF00250466', ''),
('Fattorini and Russell (1974)', 'Uniform bounds on biorthogonal functions for real exponentials with an application to the control theory of parabolic equations', '10.1090/qam/510972', 'Check Theorem 1.5 and all hypotheses.'),
('Cannarsa, Martinez and Vancostenoble (2020)', 'Precise estimates for biorthogonal families under asymptotic gap conditions', '10.3934/dcdss.2020082', 'Published version requested; preprint already available.'),
('Ammar Khodja, Benabdallah, González-Burgos and de Teresa (2014)', 'Minimal time for the null controllability of parabolic systems: The effect of the condensation index of complex sequences', '10.1016/j.jfa.2014.07.024', ''),
('Ammar-Khodja, Benabdallah, González-Burgos and de Teresa (2011)', 'The Kalman condition for the boundary controllability of coupled parabolic systems. Bounds on biorthogonal families to complex matrix exponentials', '10.1016/j.matpur.2011.06.005', ''),
('Tenenbaum and Tucsnak (2007)', 'New blow-up rates for fast controls of Schrödinger and heat equations', '10.1016/j.jde.2007.06.019', ''),
('Tenenbaum and Tucsnak (2011)', 'On the null-controllability of diffusion equations', '10.1051/cocv/2010035', ''),
('Halanay and Pandolfi (2015)', 'Approximate controllability and lack of controllability to zero of the heat equation with memory', '10.1016/j.jmaa.2014.12.021', 'Published version requested; preprint available.'),
('Guerrero and Imanuvilov (2013)', 'Remarks on non controllability of the heat equation with memory', '10.1051/cocv/2012013', 'Original PDF has previously been inspected in part.'),
('Almira (2007)', 'Müntz Type Theorems I', None, 'Surveys in Approximation Theory 3, 152–194; arXiv:0710.3570. DOI not verified; preprint available.'),
('González-Burgos and Ouaili (2024)', 'Sharp estimates for biorthogonal families to exponential functions associated to complex sequences without gap conditions', '10.3934/eect.2023044', 'Additional: gap assumptions and generalizations.'),
('Ammar Khodja, Benabdallah, González-Burgos and de Teresa (2013)', 'A new relation between the condensation index of complex sequences and the null controllability of parabolic systems', '10.1016/j.crma.2013.09.014', 'Additional comparison.'),
('Halanay and Pandolfi (2014)', 'Lack of controllability of thermal systems with memory', '10.3934/eect.2014.3.485', 'Additional comparison.'),
('Tucsnak and Weiss (2009)', 'Observation and Control for Operator Semigroups', '10.1007/978-3-7643-8994-9', 'Book; ISBN 978-3-7643-8993-2. Relevant chapters are useful if the whole book is unavailable.'),
]
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fontb='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DejaVu',font));pdfmetrics.registerFont(TTFont('DejaVuBold',fontb))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='ListTitle',fontName='DejaVuBold',fontSize=15,leading=20,alignment=TA_CENTER,spaceAfter=10))
styles.add(ParagraphStyle(name='ListBody',fontName='DejaVu',fontSize=9,leading=13,spaceAfter=3))
styles.add(ParagraphStyle(name='ListHead',fontName='DejaVuBold',fontSize=10,leading=14,spaceBefore=8,spaceAfter=6,textColor=colors.HexColor('#173e65')))
styles.add(ParagraphStyle(name='ListItem',fontName='DejaVu',fontSize=9,leading=13,spaceAfter=1))
output=Path(__file__).with_name('required-papers-and-book.pdf')
doc=SimpleDocTemplate(str(output),pagesize=A4,rightMargin=20*mm,leftMargin=20*mm,topMargin=17*mm,bottomMargin=18*mm,title='Required papers and book for manuscript review',author='Research project',invariant=1)
story=[Paragraph('Required papers and book',styles['ListTitle']),Paragraph('For the independent literature and proof review of the coupled exponential moment manuscript. This document is a list, not the papers themselves. Please provide the full published PDF when available; an author manuscript or preprint is useful if not.',styles['ListBody']),Paragraph('A. Main papers',styles['ListHead'])]
for i,(authors,title,doi,note) in enumerate(items,1):
 if i==12:story.append(Paragraph('B. Additional relevant papers',styles['ListHead']))
 if i==15:story.append(Paragraph('C. Reference book',styles['ListHead']))
 content=[Paragraph(f'<b>{i}. {escape(title)}</b>',styles['ListItem']),Paragraph(escape(authors),styles['ListItem'])]
 if doi:content.append(Paragraph(f'DOI: <link href="https://doi.org/{escape(doi)}" color="#075ca0">{escape(doi)}</link>',styles['ListItem']))
 else:content.append(Paragraph('DOI: not verified.',styles['ListItem']))
 if note:content.append(Paragraph(escape(note),styles['ListItem']))
 content.append(Spacer(1,4));story.append(KeepTogether(content))
story.append(Spacer(1,8));story.append(Paragraph('Suggested first batch: items 1–8, especially 1, 3, 4 and 5. A DOI link opens the publisher record and does not guarantee free access to the full paper.',styles['ListBody']))
doc.build(story)
print(output)
