from django.shortcuts import render
import openpyxl

import pandas as pd
from pandas import DataFrame
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.http import HttpResponse


# Create your views here.

def index(request):
    if "GET" == request.method:
        return render(request, 'maindisp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["User1"]
        print(worksheet)
        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)


        #plot    
        fig=Figure()
        ax=fig.add_subplot(111)
        #put file location here
        data_df = pd.read_csv("file location goes here!!!")
        data_df=pd.DataFrame(data_df)
        data_df.plot(ax=ax)
        
        response=HttpResponse(content_type='image/jpg')
        canvas=FigureCanvas(fig)

        canvas.print_jpg(response)
        #uncomment "return response" for graph display,
        #comment it out for data table display
        #return response
       	return render(request, 'maindisp/index.html', {"excel_data":excel_data})