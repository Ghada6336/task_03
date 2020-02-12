from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
     "my_list": [
            {
                "restaurant_name":"hayat",
                "food_type":"traditional",
            },
            {
                "restaurant_name":"Dyaha",
                "food_type":"Fast food",
            },
            {
                "restaurant_name":"MacDonalds",
                "food_type":"fast food",
            },
        ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":
           {
               "restaurant_name":"omar house",
               "food_type":"traditional food",
           }

    }
    return render(request, 'detail.html', context)
