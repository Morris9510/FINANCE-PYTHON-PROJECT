from django.shortcuts import render
from .forms import StockForm
from .utils import fetch_stock_data  # Assuming you have a utility function to fetch and process data



def stock_analysis(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker_symbol']
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            stock_data, plot_url = fetch_stock_data(ticker, start, end)  # Fetch and process the data
            return render(request, 'result.html', {'stock_data': stock_data, 'plot_url': plot_url})
    else:
        form = StockForm()
    return render(request, 'stock_analysis.html', {'form': form})
