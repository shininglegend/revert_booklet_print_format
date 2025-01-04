import PyPDF2
from PyPDF2 import PageObject
import os

def split_and_reorder_pdf(input_path, output_path):
    """
    Split a landscape PDF vertically and create a single PDF with right halves 
    appearing after left halves in reverse order.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path for the output PDF
    """
    try:
        # Open the input PDF
        with open(input_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Create new PDF writer for the combined output
            writer = PyPDF2.PdfWriter()
            
            left_pages = []
            right_pages = []
            
            # Process each page
            for page in reader.pages:
                # Get original page dimensions
                original_width = float(page.mediabox.width)
                original_height = float(page.mediabox.height)
                
                # Create new page objects for left and right halves
                left_page = PageObject.create_blank_page(
                    width=original_width/2,
                    height=original_height
                )
                right_page = PageObject.create_blank_page(
                    width=original_width/2,
                    height=original_height
                )
                
                # Scale and crop the original page for left half
                left_page.merge_page(page)
                left_page.mediabox.upper_right = (
                    original_width/2,
                    original_height
                )
                
                # Scale and crop the original page for right half
                right_page.merge_page(page)
                right_page.mediabox.lower_left = (
                    original_width/2,
                    0
                )
                right_page.mediabox.upper_right = (
                    original_width,
                    original_height
                )
                
                # Store pages in lists
                left_pages.append(left_page)
                right_pages.append(right_page)

            # Combine the left and right pages in the desired order
            # For the first n / 2 pages, we add the right side first
            for i in range(len(left_pages)):
                if i % 2 == 0:
                    writer.add_page(right_pages[i])
                else:
                    writer.add_page(left_pages[i])

            # Now for n / 2 pages, we count backwards and add the left side first
            for j in range(len(left_pages) - 1, -1, -1):
                if j % 2 == 0:
                    writer.add_page(left_pages[j])
                else:
                    writer.add_page(right_pages[j])
            
            # Save the output PDF
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            print(f"Successfully created split and reordered PDF: {output_path}")
            print(f"Total pages in output: {len(writer.pages)}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage
    input_pdf = input("Enter the first pdf name: ")
    output_pdf = input("Enter the name for the output pdf: ")
    if input_pdf == "" or output_pdf == "":
        print("Please enter valid input and output pdf names.")
        exit()
    if input_pdf == output_pdf:
        print("Input and output pdf names should be different.")
        exit()
    if input_pdf[-4:] != ".pdf":
        input_pdf += ".pdf"
    if output_pdf[-4:] != ".pdf":
        output_pdf += ".pdf"
    if not os.path.exists(input_pdf):
        print("Input pdf file does not exist. Put it in the same folder as this script and give only the name of the pdf.")
        exit()
    if os.path.exists(output_pdf):
        print("Output pdf file already exists. Please give a different name.")
        exit()
    
    split_and_reorder_pdf(input_pdf, output_pdf)