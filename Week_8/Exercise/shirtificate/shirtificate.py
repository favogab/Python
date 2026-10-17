
from fpdf import FPDF
from pathlib import Path


def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Add the certificate title at the top.
    pdf.set_font("Helvetica", style="B", size=30)
    pdf.set_text_color(35, 35, 35)
    pdf.set_y(20)
    pdf.cell(0, 15, text="CS50 Shirtificate", align="C")

    # Center the shirt on the A4 page.
    shirt_width = 180
    shirt_x = (210 - shirt_width) / 2
    shirt_y = 65

    image_path = Path(__file__).with_name("shirtificate.png")
    pdf.image(str(image_path), x=shirt_x, y=shirt_y, w=shirt_width)

    # Overlay the user's name on the shirt.
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(15, 130)
    pdf.cell(180, 12, text=name, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
