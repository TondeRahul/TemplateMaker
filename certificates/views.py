# import pandas as pd
# from PIL import Image, ImageDraw, ImageFont
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from .forms import UploadFileForm
# import os
# import zipfile
# from io import BytesIO

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['excel_file']
#             file_name = 'temp.xlsx'
#             file_path = default_storage.save(file_name, ContentFile(excel_file.read())) 
#             file_path = default_storage.path(file_path)  
#             return generate_certificates(file_path)
#     else:
#         form = UploadFileForm()
#     return render(request, 'certificates/upload.html', {'form': form})

# def generate_certificates(file_path):
#     df = pd.read_excel(file_path)
#     template_path = 'template.jpg'  
#     font_size = 30
#     font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", font_size)

#     output_files = []

#     for index, row in df.iterrows():
#         name = row['Name']
#         certificate = Image.open(template_path)
#         draw = ImageDraw.Draw(certificate)
#         text_position = (400, 370)
#         draw.text(text_position, name, font=font, fill="black")
#         output_path = os.path.join('media', f"{name}_certificate.jpg")
#         certificate.save(output_path)
#         output_files.append(output_path)

#     return generate_zip_response(output_files)

# def generate_zip_response(files):
#     response = HttpResponse(content_type='application/zip')
#     response['Content-Disposition'] = 'attachment; filename=certificates.zip'

#     with BytesIO() as buffer:
#         with zipfile.ZipFile(buffer, 'w') as zipf:
#             for file in files:
#                 zipf.write(file, arcname=os.path.basename(file))
#         response.write(buffer.getvalue())

#     return response






# import pandas as pd
# from PIL import Image, ImageDraw, ImageFont
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# from .forms import UploadFileForm
# import os
# import zipfile
# from io import BytesIO

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['excel_file']
#             file_name = 'temp.xlsx'
#             file_path = default_storage.save(file_name, ContentFile(excel_file.read())) 
#             file_path = default_storage.path(file_path)  
#             return generate_certificates(file_path)
#     else:
#         form = UploadFileForm()
#     return render(request, 'certificates/upload.html', {'form': form})

# def generate_certificates(file_path):
#     df = pd.read_excel(file_path)

#     df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d-%m-%Y')

#     template_path = 'template.jpg'  
#     font_size = 30
#     font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", font_size)

#     output_files = []

#     for index, row in df.iterrows():
#         name = str(row['Name'])
#         date = str(row['Date'])  
        
#         certificate = Image.open(template_path)
#         draw = ImageDraw.Draw(certificate)
        
#         name_position = (400, 370)
#         draw.text(name_position, name, font=font, fill="black")
        
#         date_position = (180, 550)
#         draw.text(date_position, date, font=font, fill="black")

#         output_path = os.path.join('media', f"{name}_certificate.jpg")
#         certificate.save(output_path)
#         output_files.append(output_path)

#     return generate_zip_response(output_files)

# def generate_zip_response(files):
#     response = HttpResponse(content_type='application/zip')
#     response['Content-Disposition'] = 'attachment; filename=certificates.zip'

#     with BytesIO() as buffer:
#         with zipfile.ZipFile(buffer, 'w') as zipf:
#             for file in files:
#                 zipf.write(file, arcname=os.path.basename(file))
#         response.write(buffer.getvalue())

#     return response





# name and date at fixed position

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import UploadFileForm
import os
import zipfile
from io import BytesIO

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            file_name = 'temp.xlsx'
            file_path = default_storage.save(file_name, ContentFile(excel_file.read())) 
            file_path = default_storage.path(file_path)  
            return generate_certificates(file_path)
    else:
        form = UploadFileForm()
    return render(request, 'certificates/upload.html', {'form': form})

def generate_certificates(file_path):
    df = pd.read_excel(file_path)

    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d-%m-%Y')

    template_path = 'template.jpg'  
    
    name_font_size = 30
    date_font_size = 20
    
    name_font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", name_font_size)
    date_font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", date_font_size)

    output_files = []

    for index, row in df.iterrows():
        name = str(row['Name'])
        date = str(row['Date'])  
        
        certificate = Image.open(template_path)
        draw = ImageDraw.Draw(certificate)
        
        name_position = (400, 370)
        draw.text(name_position, name, font=name_font, fill="black")
        
        date_position = (180, 570)
        draw.text(date_position, date, font=date_font, fill="black")

        output_path = os.path.join('media', f"{name}_certificate.jpg")
        certificate.save(output_path)
        output_files.append(output_path)

    return generate_zip_response(output_files)

def generate_zip_response(files):
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=certificates.zip'

    with BytesIO() as buffer:
        with zipfile.ZipFile(buffer, 'w') as zipf:
            for file in files:
                zipf.write(file, arcname=os.path.basename(file))
        response.write(buffer.getvalue())

    return response
