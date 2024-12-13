from app import create_app
app = create_app()

#def main(param1, param2):
#    print("text")
#    print(type(param1))
#    print(param1)
#    print("split")
#    print(type(param2))
#    print(param2)
#    app.run(host='0.0.0.0')

if __name__ == "__main__":
    app.run()