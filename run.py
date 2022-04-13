from app import app
if __name__=='__main__':
    try:
        app.run(port=5010)  
    except Exception as e:
        print(e)