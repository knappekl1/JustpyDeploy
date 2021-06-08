import justpy as jp
app = jp.app

def my_web():

    wp = jp.WebPage()
    h1 = jp.Div(a=wp, text="Hello world", classes="text-center w-1/2 bg-red-400")
    return wp

jp.justpy(my_web)
