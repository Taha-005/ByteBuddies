"""Generate me/about_business.pdf, the full Byte Buddies profile, using fpdf2.

Run once:  python make_pdf.py
Note: the built-in Helvetica font only supports basic Latin characters,
so the text below sticks to plain ASCII (no curly quotes or em dashes).
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos

OUTPUT = "me/about_business.pdf"

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()


# --- Small helpers so the content below stays readable ---------------------
def heading(text):
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(30, 70, 160)
    pdf.cell(0, 9, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(0, 0, 0)


def subheading(text):
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def para(text):
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)


def bullets(items):
    pdf.set_font("Helvetica", "", 11)
    for item in items:
        pdf.multi_cell(0, 6, "  -  " + item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)


# --- Title -------------------------------------------------------------------
pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 12, "Byte Buddies", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.set_font("Helvetica", "I", 12)
pdf.cell(0, 8, "Weekend Coding & Robotics for Kids Aged 8-14  |  Hamra, Beirut",
         new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
pdf.cell(0, 8, "Company Profile", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

# --- Story -------------------------------------------------------------------
heading("Our Story")
para("Byte Buddies started in 2023 when Lina Haddad, a software developer, kept "
     "getting the same question from friends: where can my kid learn to code "
     "properly, with real projects and real feedback? Together with Karim "
     "Mansour, a physics teacher who coached FIRST LEGO League teams, she opened "
     "a small weekend studio in Hamra with 12 students. Today Byte Buddies "
     "teaches more than 150 kids every term.")

heading("Mission and Values")
para("Our mission is to help kids become confident creators with technology, "
     "not just users of it.")
bullets([
    "Learn by building: every class ends with something that works.",
    "Mistakes are part of coding: we celebrate debugging, not perfection.",
    "Small groups: at most 8 kids per instructor, so nobody gets lost.",
    "Parents in the loop: written progress notes twice a term and a Demo Day.",
])

# --- Programs ----------------------------------------------------------------
heading("Programs")
subheading("Byte Starters (ages 8-10)")
para("Block-based coding with Scratch and first robots with LEGO SPIKE kits. "
     "Kids learn sequences, loops, and events by making animated stories, simple "
     "games, and robots that follow lines and react to touch sensors.")
subheading("Byte Builders (ages 11-12)")
para("The jump to text-based coding with Python, plus electronics with micro:bit "
     "boards, LEDs, buzzers, and sensors. Example projects: a step counter, a "
     "reaction-time game, and a plant-watering alarm.")
subheading("Byte Makers (ages 13-14)")
para("Bigger Python projects, simple 2D game development with Pygame, and "
     "competition-style robotics challenges. Students plan a project, work in "
     "pairs, use version control basics, and present a finished game or robot "
     "at Demo Day.")
para("No prior experience is needed for any program. Students can move up a "
     "level between terms when their instructor recommends it.")

heading("A Typical Class (2 hours)")
bullets([
    "15 min - Warm-up puzzle or unplugged activity.",
    "75 min - Project time: build, test, and debug with instructor support.",
    "10 min - Snack break.",
    "20 min - Show-and-tell: kids demo what they built and give feedback.",
])

# --- Schedule ----------------------------------------------------------------
heading("Terms and Schedule")
para("Classes run on Saturdays and Sundays only. Each student attends one "
     "2-hour class per week, in one of three time slots:")
bullets(["9:30 - 11:30", "12:30 - 14:30", "15:00 - 17:00"])
para("We run three terms a year: Fall (October - December), Winter (January - "
     "March), and Spring (April - June). Each term has 10 weekly classes and "
     "ends with Demo Day. The studio is closed in July and August.")

# --- Pricing -----------------------------------------------------------------
heading("Pricing")
pdf.set_font("Helvetica", "", 11)
with pdf.table(col_widths=(60, 40, 50), text_align="CENTER") as table:
    for row in [
        ("Program", "Ages", "Price per term"),
        ("Byte Starters", "8-10", "$180"),
        ("Byte Builders", "11-12", "$200"),
        ("Byte Makers", "13-14", "$220"),
    ]:
        r = table.row()
        for value in row:
            r.cell(value)
pdf.ln(3)
bullets([
    "Prices cover all 10 classes of a term and all equipment use.",
    "New students pay a one-time registration fee of $20.",
    "Every new student can book one free trial class before enrolling.",
    "Payment is made in full at registration, by cash or bank transfer.",
])

# --- Team --------------------------------------------------------------------
heading("The Team")
bullets([
    "Lina Haddad - Co-founder and Head of Curriculum. Computer engineer, "
    "six years as a software developer. Designs all coding lessons.",
    "Karim Mansour - Co-founder and Head of Robotics. Former physics teacher "
    "and FIRST LEGO League coach. Leads the robotics track.",
    "Maya Khoury - Studio Manager. Handles enrollment, scheduling, and "
    "parent questions at the front desk.",
    "Instructors - University engineering and computer science students, "
    "trained and supervised by Lina and Karim.",
])

# --- Safety ------------------------------------------------------------------
heading("Safety and Facilities")
bullets([
    "Laptops, robot kits, and electronics are provided and stay at the studio.",
    "Kids under 12 must be picked up by a registered adult.",
    "The studio is nut-free. Kids bring their own water bottle and snack.",
    "The building has an elevator, and parents can wait in our lounge.",
])

# --- Enrollment --------------------------------------------------------------
heading("How to Enroll")
bullets([
    "1. Book a free trial class by email or at the front desk.",
    "2. Your child attends the trial in the program that fits their age.",
    "3. Register and pay for the term (plus the $20 registration fee).",
    "4. Receive a welcome pack with the term schedule and Demo Day date.",
])

# --- FAQ ---------------------------------------------------------------------
heading("Frequently Asked Questions")
faq = [
    ("Does my child need a laptop?",
     "No. All laptops and kits are provided at the studio."),
    ("Does my child need coding experience?",
     "No. Every program starts from the basics for its age group."),
    ("Can parents stay during class?",
     "Parents can wait in the lounge and are invited to Demo Day."),
    ("What if my child misses a class?",
     "They get a catch-up worksheet, and can join another slot the same "
     "weekend if there is space."),
    ("Do kids get a certificate?",
     "Yes, every student receives a certificate at the end of each term."),
    ("Do you prepare kids for competitions?",
     "Byte Makers students can try out for our FIRST LEGO League team."),
]
for q, a in faq:
    subheading(q)
    para(a)

# --- Contact -----------------------------------------------------------------
heading("Contact")
para("Studio: 2nd floor, Cedar House, Bliss Street, Hamra, Beirut\n"
     "Front desk hours: Fridays 14:00-18:00, Saturdays and Sundays 9:00-17:00\n"
     "Email: hello@bytebuddies.lb")

pdf.output(OUTPUT)
print(f"Saved {OUTPUT}")
