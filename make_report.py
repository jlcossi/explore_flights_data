# Generate the html version of the slide deck, as slide_deck.slides.html
import os
os.system("jupyter nbconvert slide_deck.ipynb --to slides --template output_toggle.tpl")
