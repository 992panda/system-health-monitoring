import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'The application is UP: {response.status_code}')
        else:
            print(f'The application is DOWN: {response.status_code}')
    except requests.ConnectionError:
        print('The application is DOWN: Unable to connect')

def main():
    url = input("Enter the application URL to check: ")
    check_application_status(url)

if __name__ == "__main__":
    main()
