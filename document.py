""" 
document.py 
Module that creates output document of different types 
Created by Adam Harney 
Nov 28, 2018 
""" 
 
from fpdf import FPDF 
 
 
class DocumentCreator: 
    """ 
    Provides functions to create different types of documents 
    """ 
 
    def create_pdf(direction_dict): 
        """ 
        Creates a pdf document 
        """ 
        pdf = FPDF() 
        pdf.add_page() 
        pdf.set_font('Arial', 'B', 14) 
        pdf.multi_cell(180, 10, 'Directions from ' + direction_dict['start_address'][0] + ' to ' + direction_dict['end_address'][0]) 
        pdf.set_font('Arial', '', 12) 
        pdf.multi_cell(180, 10, 'Distance: ' + direction_dict['distance'][0]) 
        pdf.multi_cell(180, 10, 'Duration: ' + direction_dict['duration'][0]) 
        pdf.multi_cell(180, 10, '') 
        for instruction in direction_dict['instructions']: 
            pdf.multi_cell(180, 10, instruction) 
        pdf.output('tuto1.pdf', 'F') 
 
    def open_document(): 
        """ 
        Opens previously created document. 
        """ 